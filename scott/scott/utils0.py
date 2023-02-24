from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

def cookies_parse():
    cookie_string = ' JSESSIONID=0Kfkd4DkyzGkuV1nXMpAo_FHqe9IXKAgVJfzS-TI.pawebhst25a; citrix_ns_id_.aberdeencity.gov.uk_%2F_wat=AAAAAAWNxtGdYLeVNxjZYaWgmEbpGWHog0AKX76W9yUTc236pT0DZNkk0rzPlk-sNL9VBV5EPTejZ-e5e3nRJTYDTkaV#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsea():
    cookie_string = ' JSESSIONID=5AlwHc7ZdWnzWU3bWAi2gz39W2gMWeHVjdBuXwDF.absvapp026c; __utma=215625555.836780687.1677231574.1677231574.1677231574.1; __utmc=215625555; __utmz=215625555.1677231574.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=215625555.8.10.1677231574'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseb():
    cookie_string = ' JSESSIONID=ND472KEzaW04OYx2KpMAa_szdw800ZpuSK3QbE7h.dcepidx002'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parsec():
    cookie_string = 'JSESSIONID=Q3VfaeW2Ydem00-7VFefnr4aaBH4LwglvmgSG3DS.idoxweb; __utma=149224802.289350750.1677233761.1677233761.1677233761.1; __utmc=149224802; __utmz=149224802.1677233761.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=149224802.2.10.1677233761'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsed():
    cookie_string = 'JSESSIONID=3CQ4aGBDQO33iMSzifN8QdJ6DFH0EgBOzYqWUBX4.pawebhst39a; citrix_ns_id_.clacks.gov.uk_%2F_wat=AAAAAAU3t4DqXAH-AnDN4hk7Sj46ENXmsgnPEeUtWuqaiAvd293Cw2UcwAxicRTi5faawsQrZ7mL8tmui4azxzYFlTCn#MKWRAxvxfrLD5WG+jw7Oiw2P/gUA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

# def params():
#     param = 'searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.4009301328125%2C%22east%22%3A-73.5549828671875%2C%22south%22%3A40.45035852051812%2C%22north%22%3A40.96047101556829%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A100000%2C%22max%22%3A500000%7D%2C%22monthlyPayment%22%3A%7B%22min%22%3A323%2C%22max%22%3A1617%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=5'
#     cookie = SimpleCookie()
#     cookie.load(param)
#     parsed_cookie = {}
#     for key,morsel in cookie.items():
#         parsed_cookie[key] = morsel.value

#     encoded_cookie = urlencode(parsed_cookie)
#     return encoded_cookie

    
# def parse_new_url(url, page_number):
#     url_parsed = urlparse(url)
#     query_string = parse_qs(url_parsed.query)
#     search_query_state = json.loads(query_string.get('searchQueryState')[0])
#     search_query_state['pagination'] = {"currentPage": page_number}
#     query_string.get('searchQueryState')[0] = search_query_state
#     encoded_qs = urlencode(query_string, doseq=1)
#     new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
#     return new_url


    