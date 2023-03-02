import scrapy
import scrapy
import scrapy
import scrapy
from urllib.parse import urlparse
from pymongo import MongoClient
import certifi
ca = certifi.where()
import pymongo
import scrapy
    

class DumfriesSpider(scrapy.Spider):
    name = 'Dumfries'
    # allowed_domains = ['a.com']
    # start_urls = ['http://a.com/']
    
    

    def __init__(self):
        self.key = 0
        self.num = 0
        self.planning = None
        self.alp = []
        self.streetl = []
        self.li = {}
        self.pllinks = 0
        self.tot_len = 0

    def start_requests(self):
        #moray,perth,west dunbarnton
        ii = ['https://eaccess.dumgal.gov.uk/online-applications/search.do?action=property&type=atoz']
        #connecting to mongo
        URI = 'mongodb://5.tcp.eu.ngrok.io:16872'
        client = MongoClient(URI)

        db = client.get_database('scotland')
        self.planning = db.Dumfries_Galloway_Council
        count = 0
        while True:
            try:
                self.planning.create_index([('Check', pymongo.ASCENDING)], unique=True)
                print('Dumfries Connected successfully')
                sts = True
            except:
                count += 1
                print(f'Failed ...retrying {count} times')

                URI = 'mongodb://5.tcp.eu.ngrok.io:16872'
                client = MongoClient(URI)

                db = client.get_database('scotland')
                self.planning = db.Dumfries_Galloway_Council
                sts = False

            if sts:
                break
        #end

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
                if 'http' not in i:
                    i = f'{h}{i}'
                    yield scrapy.Request(url=i,meta={'h':h},callback=self.street)
                else:
                    yield scrapy.Request(url=i,meta={'h':h},callback=self.street)
            

        

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

        print(len(self.streetl))
        print(len(self.streetl))
        print(len(self.streetl))
        print(len(self.streetl))
        print('before')
    

        for i in list(set(self.streetl)):
            if 'http' in i:

                yield scrapy.Request(url=i,callback=self.pty,meta={'h':h},dont_filter=False)
            else:
                i = f'{h}{i}'
                yield scrapy.Request(url=i,callback=self.pty,meta={'h':h},dont_filter=False)

        print('length')
        print(len(self.streetl))
        print(len(self.streetl))
        print(len(self.streetl))        
    
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

        link = response.xpath("//div[@id='relatedItems']/div")
        if link:
            for i in link[0:1]:
                title = i.xpath('.//@id').get()
                li = i.xpath(".//ul/li/a/@href").getall()
                if li:
                    tl = len(li)
                    self.pllinks = 0
                    self.li = {}
                    while tl > 0:
                        i = li[self.pllinks]
                        self.pllinks += 1
                        tl -= 1
                        

                        if i:
                            a_li = f'{h}{i}'
                            
                            pl_app = f'Planning_application{self.pllinks}'
                            print(pl_app)
                            
                            yield scrapy.Request(url=a_li,meta={'h':h,'t':title,'u':u,'pl':pl_app,'tl':tl,'status':'not marked','uul':uul,'ptaddr':ptaddr,'pthis':pthis,'cc':self.li},callback=self.getplan,dont_filter=True)
                        
                    
                    
                    self.pllinks=0
                    yield scrapy.Request(url=lirl,meta={'h':h,'t':title,'u':u,'pl':pl_app,'tl':tl,'uul':uul,'ptaddr':ptaddr,'pthis':pthis,'status':'marked','cc':self.li},callback=self.getplan,dont_filter=True)
                    
                    
                    
                    
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

    def getplan(self,response):
        pl = response.meta['pl']
        h = response.meta['h']
        u = response.meta['u']
        self.li = response.meta['cc']
        uul = response.meta['uul']
        ptaddr = response.meta['ptaddr']
        pthis = response.meta['pthis']
        lirl = response.url
        
       
        status = response.meta['status']
        if status == 'not marked':


            app =  {}

            title = response.xpath("//table[@id='simpleDetailsTable']/tr/th/descendant::text()").getall()
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
        
            self.li[pl] = app
            
        elif status == 'marked':
            
        
            yield scrapy.Request(url=lirl,meta={'h':h,'u':u,'pl':pl,'uul':uul,'ptaddr':ptaddr,'pthis':pthis,'c':self.li},callback=self.last,dont_filter=True)
            self.li = {}
            print('li is now empty!')
            print('li is now empty!')
            print('li is now empty!')
                    

    def last(self,response):
        h = response.meta['h']
        u = response.meta['u']
        uul = response.meta['uul']
        ptaddr = response.meta['ptaddr']
        pthis = response.meta['pthis']
        copy = response.meta['c']
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

    