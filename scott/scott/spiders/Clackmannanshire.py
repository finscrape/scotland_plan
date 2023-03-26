from scrapy.selector import Selector
import scrapy
import scrapy
from urllib.parse import urlparse
from pymongo import MongoClient
import certifi
ca = certifi.where()
import pymongo
import scrapy
import pandas as pd
from scrapy_selenium import SeleniumRequest
from scott.utils0 import cookies_parseclk
codes = pd.read_csv('unique_postcodes.csv')

pcode = list(codes['postcode'])
    
from scott.utils import string

class ClackmannanshireSpider(scrapy.Spider):
    name = 'Clackmannanshire'
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
        ii = ['https://publicaccess.clacks.gov.uk/publicaccess/propertySearchResults.do?action=firstPage']


        #connecting to mongo
        URI = string
        client = MongoClient(URI)
        
        db = client.get_database('scotland')
        self.planning = db.Clackmannanshire_Councils
        count = 0
        while True:
            try:
                self.planning.create_index([('Check', pymongo.ASCENDING)], unique=True)
                print('Clackmannanshire Connected successfully')
                sts = True
            except:
                count += 1
                print(f'Failed ...retrying {count} times')


                URI = string
                client = MongoClient(URI)
                
                db = client.get_database('scotland')
                self.planning = db.Clackmannanshire_Councils
                sts = False
            if sts:
                break
        #mongo end connect

        for i in ii[0:]:
            xx = 0
            head = urlparse(i).netloc
            h = f'https://{head}'
        
            for p in pcode[50000:100000]:
                    
                    xx += 1
                    print(f'Scraped {xx} links......{p}')
                    print(f'Scraped {xx} links......{p}')
                    
                    tx = f'_csrf=b70ca703-6f1c-4e74-a4df-8888edc90d80&searchCriteria.uprn=&searchCriteria.propertyNameNumber=&searchCriteria.streetName=&searchCriteria.locality=&searchCriteria.town=&searchCriteria.postCode={p}&searchType=Property'
                    yield scrapy.Request(url=i,meta={'f':i,'p':p,'h':h},dont_filter= True,callback=self.parse,cookies=cookies_parseclk(),method='POST',body=tx)

    def parse(self, response):
        # pgs = 'Empty'
        h = response.meta['h']
            

        # driver = response.meta['driver']


        # inp = driver.find_element_by_xpath("//input[@name='searchCriteria.postCode']")

        # inp.send_keys(p)

        # sub = driver.find_element_by_xpath("//input[@value='Search']")

        # sub.click()

        # pgs = driver.page_source

        # htmx = Selector(text=pgs)

        box = response.xpath("//ul[@id='searchresults']")

        if box:
            link = response.xpath("//ul[@id='searchresults']/li/a/@href").getall()
            for i in link:
                i_next = f'{h}{i}'
                yield scrapy.Request(url=i_next,callback=self.each,meta={'h':h})

        else:
            pass
        
        
        
        next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
        if next:
            ab_next = f'{h}{next}'
            yield scrapy.Request(url=ab_next,callback=self.parse,meta={'h':h})
        else:
            pass


    # def next(self,response):
    #     h = response.meta['h']

    #     link = response.xpath("//ul[@id='searchresults']/li/a/@href").getall()
    #     for i in link:
    #         i_next = f'{h}{i}'
    #         yield scrapy.Request(url=i_next,callback=self.each,meta={'h':h})

    #     next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
    #     if next:
    #         ab_next = f'{h}{next}'
    #         yield scrapy.Request(url=ab_next,callback=self.next,meta={'h':h})
    #     else:
    #         pass




    def each(self,response):

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
            
            lirl = response.url
            self.key = f'{urpn}-{lirl}'
            one_result = {
                'URPN':urpn,
                'URPN_Link':urpn_url,
                'Address':address,
                'Property_History':None,
                'Planning_Applications':None,
                'Check':self.key
            }
            try:
                self.planning.insert_one(one_result)
                yield one_result
            except:
                print(f'{urpn} exists in database!')


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
            
            for i in link:

                if 'http' not in i:
                    ii = f'{h}{i}'
                else:
                    ii = i
                yield scrapy.Request(url=ii,callback=self.new,meta={'h':h,'u':u,'uul':uul,'ptaddr':ptaddr,'pthis':pthis,'cc':link,'dd':0})     

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

            if 'nairaland' in one and len(self.li) > 1:
                one = self.li[1]
                one_link = f'{h}{one}'
            elif 'nairaland' not in one:
                 one_link = f'{h}{one}'
            
            
            else:
                one = self.li[0]
                one_link = f'{one}'

            


            
            
           
            print(one_link)
            print(one_link)
            print(one_link)
            if one_link == 'https://www.nairaland.com/' and len(self.li) == 1 :
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
    

