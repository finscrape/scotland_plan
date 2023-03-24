from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

def cookies_parse():
    cookie_string = 'JSESSIONID=c-wXxYreJ_8xcsW86d8kQzw5_fiR71-JzjkKhLZ5.pawebhst25a; citrix_ns_id_.aberdeencity.gov.uk_%2F_wat=AAAAAAWVaKZ2JUoY1Nn7Xh0mgEcSIox4pctPOiAdKaTs-W8bL6SR9pKc8CFBYnbkSTqI61j3OBQ2KJIQwc4uKgKHnWTd#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseabs():
    cookie_string = 'JSESSIONID=lMR8pvbdcq-i8vyj2Vxf7hQCq7-63tI4LrS53K-m.absvapp026c; __utma=215625555.979542160.1679662322.1679662322.1679662322.1; __utmc=215625555; __utmz=215625555.1679662322.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=215625555.3.10.1679662322'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseang():
    cookie_string = 'JSESSIONID=MbqAPk16tAbMgMRPm6fgq1KQWEJXuqDs2EXt34hN.dcepidx002'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parseclk():
    cookie_string = 'JSESSIONID=VNvob9goWueTBbBOkn-1Zj3_LwOm6qhV-mC9Tjfx.pawebhst39a; citrix_ns_id_.clacks.gov.uk_%2F_wat=AAAAAAUC3cna6maFBrl7Mg_5SpASiJoxZUPFZOYNrxhO82bHex-C7ozbzl15andtu5TGU72cl5eVgXnUecdZpbmUbjN4#MKWRAxvxfrLD5WG+jw7Oiw2P/gUA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsedum():
    cookie_string = 'JSESSIONID=M8yFJL3XYEArQNPJzUUp41j2K9EXbrfLDzi-h6C7.pawebhst26a; citrix_ns_id_.dumgal.gov.uk_%2F_wat=AAAAAAX46KWtiPCBqFCtdl0tGgTqZeyZNgBpzXdujQu5h7dhu-T_akvo9g8iehtUUgU1sMOQTNlNXkNT-FQ68ATxrAth#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsedun():
    cookie_string = 'JSESSIONID=WJ3_eseNfg3zITpuCDc0EpPxn7_Jh1EiBy6DkfjS.2012-idox-iis; __utma=49359486.506477386.1679665633.1679665633.1679665633.1; __utmc=49359486; __utmz=49359486.1679665633.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=49359486.2.10.1679665633'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseeas():
    cookie_string = 'JSESSIONID=dlXauzRvzRTXUNxFLadOI4cgIuXJ-Fp5WnYM_446.2012-idox-iis; __utma=49359486.2198430.1677246846.1677246846.1677246846.1; __utmc=49359486; __utmz=49359486.1677246846.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=49359486.2.10.1677246846'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseead():
    cookie_string = 'JSESSIONID=3ZoQIe4KY_JjjYHECWjVerWgajs2hA2exLArowJr.plan-web-1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseeal():
    cookie_string = 'JSESSIONID=ejWapLAJJ2ObIhAPK8bc6GrgalxvvbcPR6KTy8Ik.cotton'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseear():
    cookie_string = 'JSESSIONID=UbjB_gixAo1xdCasYmS0CzYmrrIErzbFmTTincM4.idoxweb-live'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parseedb():
    cookie_string = 'JSESSIONID=_tQcp_oUbmL4PgUdap8Wf_oRcnCs2aRe8U-p2Kd1.lap-pubacc2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseflk():
    cookie_string = 'JSESSIONID=YBPPXd3wyYv91Pr55sKcfxdHTgA6oi0kQs0S2FL4.s-fk-ep-paweb'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsefif():
    cookie_string = 'JSESSIONID=CrYel940YuGBRL5xwVxOTcqA9K3c3TU4Ou92p3P3.gcwgnclidxl01'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseglg():
    cookie_string = 'JSESSIONID=x9-1MRdLjX5W7IVQ50-os6-mcWIP7e2s-mY1ZrYs.gcwgnclidxl01'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsen():
    cookie_string = 'JSESSIONID=L92q3H63bkCAZE8QonBDa9GnC8DMvb4RtOTbAr-9.invidoxweb2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseo():
    cookie_string = 'JSESSIONID=YUV-3WQP93hbciQAheAvaeHfCV5CHgVw5GBbKcfw.idoxweb; __utma=250927186.418910463.1677255242.1677255242.1677255242.1; __utmc=250927186; __utmz=250927186.1677255242.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=250927186.4.10.1677255242'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsep():
    cookie_string = 'JSESSIONID=ovsJeH5qqAU6fiBn2CzYOhGK34Hx6bC2Ij_6ijVE.pawebhst49a; citrix_ns_id_.midlothian.gov.uk_%2F_wat=AAAAAAVPHZ1V1oujBbWRjuUxntk4_sMwhmw8pa9hZVFHCvdhgcJKkBSV6KEgivrrDc2X6SEbqnxPb-U9zEzs4Hv1O2MY#dcLYf+bC79jQY1XncvhA9CvOlKsA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseq():
    cookie_string = 'JSESSIONID=uKkRY02TYJpQgxmglxlPKMYQXs8P-gMkHaoxy7r_.dcepidx002'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parser():
    cookie_string = 'JSESSIONID=QYAjaBiV8xaBLJuhf-S0o524NhXl2_DCEYER1U1s.oic-vedrms-web2'
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


    