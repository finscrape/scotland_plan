#proxies
import pandas as pd
#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import choice

plist = pd.read_csv('scott\data1.csv')

proxy = plist['ips'].to_list()



# Scrapy settings for scott project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scott'
SPIDER_MODULES = ['scott.spiders']
NEWSPIDER_MODULE = 'scott.spiders'


FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # This is the first provider we'll try
    'scrapy_fake_useragent.providers.FakerProvider',  # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # Fall back to USER_AGENT value
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 15

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 15#South_Lanarkshire_Council
CONCURRENT_REQUESTS_PER_IP =15
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
from w3lib.http import basic_auth_header 
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,fa;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "no-cache",
    'Proxy-Authorization':basic_auth_header('bengabp', 'bengabplusProxies')
}
#, tlsCAFile=ca

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scott.middlewares.ScottSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

ROTATING_PROXY_LIST = proxy
ROTATING_PROXY_CLOSE_SPIDER = False
ROTATING_PROXY_PAGE_RETRY_TIMES = 3
RETRY_HTTP_CODES = [429,500, 502, 503, 504, 400, 408]

DOWNLOADER_MIDDLEWARES = {
    #'scott.middlewares.CustomProxyMiddleware': 350,
    
   'scott.middlewares.ScottDownloaderMiddleware': 543,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scott.middlewares.TooManyRequestsRetryMiddleware': 543,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
  #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400, 
   #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
   #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,   
     #'scrapy_selenium.SeleniumMiddleware': 800

}
#mongodump mongodb://6.tcp.eu.ngrok.io:13312/ -d scotland -o C:\Users\stagnator\Desktop\newdump


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scott.pipelines.ScottPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = False
# The initial download delay
#AUTOTHROTTLE_START_DELAY = False
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [301,302]
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
REDIRECT_ENABLED = False

from shutil import which

# SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
# SELENIUM_DRIVER_ARGUMENTS=['-dless']  # '--headless' if using chrome instead of firefox

FEED_EXPORT_ENCODING = 'utf-8'

FEED_EXPORTERS = {
    'xlsx': 'scrapy_xlsx.XlsxItemExporter',
}

from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--adless']  # '--headless' if using chrome instead of firefox

FEED_EXPORT_ENCODING = 'utf-8'
