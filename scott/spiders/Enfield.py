from scott.utils import string
import scrapy
import scrapy
from urllib.parse import urlparse
from pymongo import MongoClient
import certifi
ca = certifi.where()
import pymongo
import scrapy

    


class EnfieldSpider(scrapy.Spider):
    name = 'Enfield'
    # allowed_domains = ['a.com']
    # start_urls = ['http://a.com/']

    
    def __init__(self):
        self.key = 0
        self.num = 0
        self.planning = None
        self.alp = []
        self.streetl = []
        self.li = []
        self.pllinks = 0
        self.tot_len = 0
        self.all_pl = {}

    def start_requests(self):
        #moray,perth,west dunbarnton
        ii = ['https://publicaccess.aberdeencity.gov.uk/online-applications/search.do?action=property&type=atoz']

        #mongo connect
        URI = string
        client = MongoClient(URI)
        db = client.get_database('scotland')

        self.planning = db.Enfield_City_Council

        count = 0
        while True:
            try:
                self.planning.create_index([('Check', pymongo.ASCENDING)], unique=True)
                print('Enfield Connected successfully')
                sts = True
                
            except:
                count += 1
                print(f'Failed ...retrying {count} times')
                URI = string

                client = MongoClient(URI)

                db = client.get_database('scotland')
                
                self.planning = db.Enfield_City_Council
                sts = False
            
            if sts:
                break

        #mongo end connect

        for i in ii:
        
            yield scrapy.Request(url=i,meta={'f':i})

    def parse(self, response):
        fir = response.meta['f']
        head = urlparse(fir).netloc
        h = f'https://{head}'
        
        
        first = f'{fir}&letter=A'
        l = response.xpath("//li/a[contains(@title,'Streets beginning with the letter')]/@href").getall()
        l.append(first)
        for i in l:
            if 'http' not in i:
                i = f'{h}{i}'
            
                yield scrapy.Request(url=i,dont_filter=True,callback=self.each,meta={'h':h})
            else:
                yield scrapy.Request(url=i,dont_filter=True,callback=self.each,meta={'h':h})
    def parse(self, response):
        fir = response.meta['f']
        head = urlparse(fir).netloc
        h = f'https://{head}'
        
        
        first = f'{fir}&letter=A'
        l = response.xpath("//li/a[contains(@title,'Streets beginning with the letter')]/@href").getall()
        l.append(first)
        for i in l:
            if 'http' not in i:
                i = f'{h}{i}'
                yield scrapy.Request(url=i,dont_filter=True,callback=self.each,meta={'h':h})
            else:
                yield scrapy.Request(url=i,dont_filter=True,callback=self.each,meta={'h':h})
        
        

    def each(self,response):
        
        h = response.meta['h']
        next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
        l = response.xpath("//ul[@id='streetlist']/li/a/@href").getall()
        self.alp += l

        
            

        if next:

            ab_next = f'{h}{next}'
            yield scrapy.Request(url=ab_next,callback=self.each,meta={'h':h},dont_filter=True)
            print('mooooooooooooooooooooooving one battch')
        else:
            for i in self.alp:
                a = i
                self.alp.remove(a)
                alen = len(self.alp)
                if 'http' not in i:
                    i = f'{h}{i}'
                    yield scrapy.Request(url=i,meta={'h':h,'alen':alen},callback=self.street)
                else:
                    yield scrapy.Request(url=i,meta={'h':h,'alen':alen},callback=self.street)
            

        

    def street(self,response):
            

        h = response.meta['h']
        urp = response.xpath("//th[text()='UPRN:']/following-sibling::td/text()").get()
        next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
        link = response.xpath("//ul[@id='searchresults']/li/a/@href").getall()
        if link:
            self.streetl += link
        elif urp is not None:
            current = response.url
            self.streetl.append(current)
            #yield scrapy.Request(url=current,callback=self.pty,meta={'h':h},dont_filter=True)

        
        
        
        if next:
            ab_next = f'{h}{next}'
            yield scrapy.Request(url=ab_next,callback=self.street,meta={'h':h})
        else:
            pass

        # print(len(self.streetl))
        # print(len(self.streetl))
        # print(len(self.streetl))
        # print(len(self.streetl))
        # print('before')
    

        for i in list(set(self.streetl)):
            #self.streetl.remove(i)
            if 'http' in i:

                yield scrapy.Request(url=i,callback=self.pty,meta={'h':h})
            else:
                i = f'{h}{i}'
                yield scrapy.Request(url=i,callback=self.pty,meta={'h':h})

        # print('length')
        # print(len(self.streetl))
        # print(len(self.streetl))
        # print(len(self.streetl))



            
    def pty(self,response):
        h = response.meta['h']
        address = {}
        urpn = response.xpath("//th[text()='UPRN:']/following-sibling::td/text()").get()
        urpn_url = response.url
        if urpn:
            title = response.xpath("//table[@id='propertyAddress']/tr/th/descendant::text()").getall()
            value = response.xpath("//table[@id='propertyAddress']/tr/td/descendant::text()").getall()
            for a,b in zip(title,value):
                address[a] = b

        link = response.xpath("//li/a[contains(span/text(),'Property History')]/@href").get()
        if link:
            a_link = f'{h}{link}'
            yield scrapy.Request(url=a_link,meta={'h':h,'u':urpn,'uul':urpn_url,'ptaddr':address,'pthis':a_link},callback=self.info,dont_filter=True)
        else:
            
            yield scrapy.Request(url=urpn_url,meta={'h':h,'u':urpn,'uul':urpn_url,'ptaddr':address,'pthis':None},callback=self.info,dont_filter=True)


    def info(self,response):
        h = response.meta['h']
        u = response.meta['u']
        uul = response.meta['uul']
        ptaddr = response.meta['ptaddr']
        pthis = response.meta['pthis']
        lirl = response.url

        link = response.xpath("//div[@id='relatedItems']/div[1]/ul/li/a/@href").getall()
        if link:
            self.pllinks = 0
            link.append('https://www.nairaland.com/')
            yield scrapy.Request(url=lirl,callback=self.new,meta={'h':h,'u':u,'uul':uul,'ptaddr':ptaddr,'pthis':pthis,'cc':link,'dd':0})        
        else:
            if u:

                pl_app = None
                self.key = f'{u}-{lirl}'
                one_result = {
                    'URPN':u,
                    'URPN_Link':uul,
                    'Address':ptaddr,
                    'Property_History':pthis,
                    'Planning_Applications':pl_app,
                    'Check':self.key
                }
                try:
                    self.planning.insert_one(one_result)
                    yield one_result
                except:
                    print(f'{u} exists in database!')
            else:
                yield scrapy.Request(url=uul,callback=self.street,meta={'h':h})

    def new(self,response):
        h = response.meta['h']
        u = response.meta['u']
        self.li = response.meta['cc']
        self.pllinks = response.meta['dd']
        uul = response.meta['uul']
        ptaddr = response.meta['ptaddr']
        pthis = response.meta['pthis']
        lirl = response.url
        try:
            self.all_pl = response.meta['aa']
        except:
            self.all_pl = {}


        #checking table
        title = response.xpath("//table[@id='simpleDetailsTable']/tr/th/descendant::text()").getall()
        if title:
            self.pllinks += 1
            pl_app = f'Planning_Application{self.pllinks}'
            app =  {}

            value = response.xpath("//table[@id='simpleDetailsTable']/tr/td/descendant::text()").getall()
            for a,b in zip(title,value):
                    aa = a.strip()
                    if b:
                        bb = b.strip()
                    else:
                        bb = ''
                    app[aa] = bb
            
            doc = response.xpath("//li[contains(a/span/text(),'Documents')]/a/@href").get()
            if doc:
                docu = f'{h}{doc}'
            else:
                docu = None

            rela = response.xpath("//li[contains(a/span/text(),'Related')]/a/@href").get()
            if rela:
                related = f'{h}{rela}'
            else:
                related = None

            cont = response.xpath("//li[contains(a/span/text(),'Contact')]/a/@href").get()
            if cont:
                contacts = f'{h}{cont}'
            else:
                contacts = None

            app['Document_link'] = docu 
            app['Related_cases'] = related 
            app['Contacts_link'] = contacts
            print(app)

            self.all_pl[pl_app] = app
        
        else:
            pass
        
        
            
            
        if len(self.li) > 0:
            one = self.li[0]
            if 'nairaland' in one:
                one_link = f'{one}'
            
            else:
                one_link = f'{h}{one}'
            
            print(one_link)
            print(one_link)
            print(one_link)
            if one_link == 'https://www.nairaland.com/':
                copy = self.all_pl
                yield scrapy.Request(url=lirl,dont_filter=True,callback=self.last,meta={'h':h,'u':u,'pl':copy,'uul':uul,'ptaddr':ptaddr,'pthis':pthis,'c':self.li})
                self.all_pl = {}
                self.pllinks =0
        
                print('Empty set')
                self.li = []
            
            else:
                self.li.remove(one)
            
                yield scrapy.Request(url=one_link,dont_filter=True,callback=self.new,meta={'h':h,'u':u,'uul':uul,'ptaddr':ptaddr,'pthis':pthis,'cc':self.li,'dd':self.pllinks,'aa':self.all_pl})
            

            

            
            
        


    
            
    def last(self,response):
        h = response.meta['h']
        u = response.meta['u']
        uul = response.meta['uul']
        ptaddr = response.meta['ptaddr']
        pthis = response.meta['pthis']
        copy = response.meta['pl']
        lirl = response.url

                
        
        
        self.key = f'{u}-{lirl}'
        if u:
            onee_result = {
                'URPN':u,
                'URPN_Link':uul,
                'Address':ptaddr,
                'Property_History':pthis,
                'Planning_Applications':copy,
                'Check':self.key

            }
            print(onee_result)
            try:
                self.planning.insert_one(onee_result)
                yield onee_result
                

            except:
                print(f'{u} exists in database!')
        else:
            yield scrapy.Request(url=uul,callback=self.street,meta={'h':h})

    