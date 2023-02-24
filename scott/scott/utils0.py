from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

def cookies_parse():
    cookie_string = 'JSESSIONID=kNUKq54myYT2OO0Kx0cDQ6FvNXzfXuLvBPKkbuSp.pawebhst25a; citrix_ns_id_.aberdeencity.gov.uk_%2F_wat=AAAAAAVycSCoY-cWtMtclwuOZetKza_B2kN2lCFFA9mQOd8a_srNIXls1AXRdFy37d4JltW0yBzLiSPG0GtQDvSFKWfR#guYNW/k4KwVU9addMBooLYQJNuQA&'
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

def cookies_parseg():
    cookie_string = 'JSESSIONID=w_s-Jz-nYBxwdnrhJ-wXax2RPXkXHlk1cu3GyNwM.edmsweb03'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseh():
    cookie_string = 'JSESSIONID=6K4dD369FYRaT4kE_JSvgK0qhq39ZFD8BpfCECSz.cotton'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsei():
    cookie_string = 'JSESSIONID=szyDnhW9Ss5GKN_1mzarTg5CDTohXbehNDoSg_pe.idoxweb-live'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parsej():
    cookie_string = 'JSESSIONID=ipaxdrjhR-g2fJTbT70OjIChpGu4A3TmtDUnIxH5.lap-pubacc2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsek():
    cookie_string = 'JSESSIONID=nxlodzwHcPUVQrW0jnEtV-lV2MCofG3ryqaya1Ya.s-fk-ep-paweb'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsel():
    cookie_string = 'JSESSIONID=CrYel940YuGBRL5xwVxOTcqA9K3c3TU4Ou92p3P3.gcwgnclidxl01'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsem():
    cookie_string = 'JSESSIONID=Ywp80z4LqkaY_FyyLYYhxfM2nnlkQeppkqS-l4hb.pawebhst17a; citrix_ns_id_.highland.gov.uk_%2F_wat=AAAAAAXOFH0-40vPF2lM3_uJyfE02nbYNwgGC4TYjzpgAQHb4ibSQATDLyLCFKBRfOCLAKYcAYES_YUpqXRrGYg4UCL-#O5/8TkatWotXuO7O313UTD03u3oA&; CookieControl={"necessaryCookies":[],"optionalCookies":{},"statement":{"shown":true,"updated":"09/07/2020"},"consentDate":1677253425915,"consentExpiry":90,"interactedWith":true,"user":"CFAF744A-B2A4-4FFB-B212-D0015654200E"}'
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
