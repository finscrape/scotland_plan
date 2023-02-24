from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

def cookies_parse():
    cookie_string = 'JSESSIONID=-a75qzsrtrU5rY5z_G9rqrOqGjyeH8_bQNykteR9.pawebhst25a; citrix_ns_id_.aberdeencity.gov.uk_%2F_wat=AAAAAAX-fxbTjbZnSuIOoYiD-hQCqWn8CVA3NnOW48pKmJgDfvF_qU4s1Bq3I9QLGTbwsrqFzUehTzL24T_V_Kv7ucJ2#guYNW/k4KwVU9addMBooLYQJNuQA& '
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsea():
    cookie_string = 'JSESSIONID=6WUh4OniHbSmAlW8cz6FXFv1U_0UAvWKJ_usBHsN.absvapp026c; __utmc=215625555; __utmz=215625555.1677231574.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=215625555.836780687.1677231574.1677231574.1677240011.2; __utmt=1; __utmb=215625555.7.10.1677240011'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseb():
    cookie_string = '_csrf=91729362-3ae8-4617-acb8-da7b290206d0&searchType=Application&searchCriteria.caseStatus=&searchCriteria.simpleSearchString=1000&searchCriteria.simpleSearch=true'
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
    cookie_string = 'JSESSIONID=YXsz29o5QsoWxvUUjsucO_-lUrmNRyIelANltDIa.pawebhst39a; citrix_ns_id_.clacks.gov.uk_%2F_wat=AAAAAAUHD3J1ff5YtSL1vPRbCszM0XU6w21NJkZMFG3EtXM7RQwwZjAx9v0fdtcHnc-KprdxKwhT2EYb9Spz1cl7HNrA#MKWRAxvxfrLD5WG+jw7Oiw2P/gUA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsee():
    cookie_string = 'JSESSIONID=PJMMEdcU3I3t-Zj7m4efXVBlgOn-CFRuMe880fV6.pawebhst26a; citrix_ns_id_.dumgal.gov.uk_%2F_wat=AAAAAAUhfHY3b0xwCHXFCP5LI8n4nbQ6-Se-kLrwtsV_vWIsuIEOw70g0Qsls-CCbl4yvR4c0d9rbYRuNscFGZTqitHd#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsef():
    cookie_string = 'JSESSIONID=dlXauzRvzRTXUNxFLadOI4cgIuXJ-Fp5WnYM_446.2012-idox-iis; __utma=49359486.2198430.1677246846.1677246846.1677246846.1; __utmc=49359486; __utmz=49359486.1677246846.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=49359486.2.10.1677246846'
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


    