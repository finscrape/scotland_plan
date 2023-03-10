import scrapy
from scott.utils import string
import scrapy
from urllib.parse import urlparse
from pymongo import MongoClient
import certifi
ca = certifi.where()
import pymongo
import scrapy
import json
    
from scott.utils0 import cookies_parse

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings




class MoraySpider(scrapy.Spider):
    name = 'Moray'
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
        ii = ['https://publicaccess.aberdeencity.gov.uk/online-applications/search.do?action=property&type=atoz']
        #connecting to mongo
        URI = string
        client = MongoClient(URI)

        db = client.get_database('scotland')
        self.planning = db.Moray_Council
        self.planning.create_index([('Check', pymongo.ASCENDING)], unique=True)
        #end

        
        
        numb = list(range(1000,1000000))
        for i in numb:
            ii = ['https://publicaccess.aberdeencity.gov.uk/online-applications/simpleSearchResults.do?action=firstPage']
            head = 'https://publicaccess.aberdeencity.gov.uk'
            
            pay = f'org.apache.struts.taglib.html.TOKEN=3922b9138e445cc16a712c2d08e78c4a&_csrf=71c39399-a62b-4fa9-b16b-b34463afdab4&searchType=Application&searchCriteria.caseStatus=&searchCriteria.simpleSearchString={i}&searchCriteria.simpleSearch=true'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,fa;q=0.7',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'publicaccess.aberdeencity.gov.uk',
                'Origin': 'https://publicaccess.aberdeencity.gov.uk',
                'Pragma': 'no-cache',
                'Referer': 'https://publicaccess.aberdeencity.gov.uk/online-applications/search.do?action=simple'

            }

            yield scrapy.Request(url=ii[0],method='POST',body =pay,headers=headers,cookies=cookies_parse(),meta={'h':head},dont_filter=True)
            
        


        
    def parse(self, response):
        h = response.meta['h']
        ref = response.xpath("//th[contains(text(),'Reference')]/following-sibling::td/text()").get()
        next = response.xpath("(//a[text()='Next']/@href)[1]").get()
        
        link = response.xpath("//ul[@id='searchresults']/li/a/@href").getall()
        if link:
            for i in link:
                ii = f'{h}{i}'
                yield scrapy.Request(url=ii,callback=self.pty,meta={'h':h})
                print(f'link:{ii}')
        elif ref is not None:
            current = response.url
            yield scrapy.Request(url=current,callback=self.pty,meta={'h':h},dont_filter=True)

        
        
        
        if next:
            ab_next = f'{h}{next}'
            yield scrapy.Request(url=ab_next,callback=self.parse,meta={'h':h})

                    
    def pty(self,response):
        h = response.meta['h']
        link = response.xpath("//li/a[@id='tab_relatedCases']/@href").get()
        if link:
            a_link = f'{h}{link}'
            yield scrapy.Request(url=a_link,meta={'h':h},callback=self.info,dont_filter=True)

    def info(self,response):
        h = response.meta['h']
        
        link = response.xpath("//div[@id='relatedItems']/div[@id='Property']/descendant::a/@href").get()
        a_li = f'{h}{link}'
        yield scrapy.Request(url=a_li,meta={'h':h},callback=self.las,dont_filter=True)

    def las(self,response):
        h = response.meta['h']
        urpn = response.xpath("//th[text()='UPRN:']/following-sibling::td/text()").get()
        link = response.xpath("//li/a[contains(span/text(),'Property History')]/@href").get()
        if link:
            a_link = f'{h}{link}'
            yield scrapy.Request(url=a_link,meta={'h':h,'u':urpn},callback=self.infoo)

    def infoo(self,response):
        h = response.meta['h']
        u = response.meta['u']
        
        link = response.xpath("//div[@id='relatedItems']/div[@id='Application']")
        for i in link[0:1]:
            title = i.xpath('.//@id').get()
            li = i.xpath(".//ul/li/a/@href").getall()
            if li:
                for i in li:
                    if i:
                        a_li = f'{h}{i}'
                        yield scrapy.Request(url=a_li,meta={'h':h,'t':title,'u':u},callback=self.last)



    def last(self,response):
        
        dic = {}
        urpn = response.meta['u']
        title = response.meta['t']
        h = response.meta['h']
        curl = response.url

        #dic['urpn'] = urpn
        #dic['title'] = title
        
        attr = response.xpath("//table[@id='simpleDetailsTable']/tr")
        if attr:
            reference = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[1]/td/descendant::text())").get()    
            #a_reference = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[2]/td/descendant::text())").get()    
            #a_received = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[3]/td/descendant::text())").get()    
            a_validated = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[2]/td/descendant::text())").get()    
            addr = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[3]/td/descendant::text())").get()    
            propose = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[4]/td/descendant::text())").get()    
            stat = response.xpath("//table[@id='simpleDetailsTable']/tr[5]/td/descendant::text()").getall()
            status = ''.join(stat)    
            st = status.strip()
            #decision = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[8]/td/descendant::text())").get()    
            #did = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[9]/td/descendant::text())").get()    
            a_status = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[6]/td/descendant::text())").get()    
            a_decision = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[7]/td/descendant::text())").get()    
            lbbs = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[8]/td/descendant::text())").get()    
            lbbd = response.xpath("normalize-space(//table[@id='simpleDetailsTable']/tr[9]/td/descendant::text())").get()    
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

            cont = response.xpath("//li[contains(a/span/text(),'Contacts')]/a/@href").get()
            if cont:
                contacts = f'{h}{cont}'
            else:
                contacts = None

            self.num += 1
            self.key = f'{urpn}-{reference}-{addr}'

            result = {
                'Title':title,
                'URPN':urpn,
                'Reference':reference,
                #'Alternative_reference':a_reference,
                #'Application_received':a_received,
                'Application_validated':a_validated,

                'Address':addr,
                'Proposal':propose,
                'Status':st,
                #'Decision':decision,
                #'Decision_issued_date':did,
                'Appeal_status':a_status,
                'Appeal_decision':a_decision,
                'Local Review Body Status':lbbs,
                'Local Review Body Decision':lbbd,
                'Source_link':curl,
                'Document_link':docu,
                'Related_cases':related,
                'Contacts':contacts,
                'Check':self.key
                
            }
            try:
                #self.planning.insert_one(result)
                yield result
            except:
                print(f'{reference} exists in database!')


