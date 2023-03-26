from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

global cook
cook ='JSESSIONID=HxONPhQnL8_nXyYic2SY1l4GuGv178ixRcIvOBRK.pawebhst25a; citrix_ns_id_.aberdeencity.gov.uk_%2F_wat=AAAAAAW9ibEh6Zp6YlyTDBayUG3yS7YcYfLCt6jwBg2w1gbP7Sq5JojSPbv-Zi2sSMlPkc8BUn8O8NKQWe5BPm6KIkS3#guYNW/k4KwVU9addMBooLYQJNuQA&'
def cookies_parse():
    cookie_string = 'JSESSIONID=c-wXxYreJ_8xcsW86d8kQzw5_fiR71-JzjkKhLZ5.pawebhst25a; citrix_ns_id_.aberdeencity.gov.uk_%2F_wat=AAAAAAWVaKZ2JUoY1Nn7Xh0mgEcSIox4pctPOiAdKaTs-W8bL6SR9pKc8CFBYnbkSTqI61j3OBQ2KJIQwc4uKgKHnWTd#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseabs():
    cookie_string = 'JSESSIONID=ka_Qfh_RgPajiS9MxwsIESRtfmUScvbWHHGkPMSR.absvapp026c; __utmc=215625555; __utmz=215625555.1679449546.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=215625555.18175734.1679449546.1679751644.1679756357.5; __utmt=1; __utmb=215625555.1.10.1679756357'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseang():
    cookie_string = 'JSESSIONID=hNfILIIKza2nU53ubs9d5GS3KPXVnMTh-YaBtRAC.dcepidx002'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parseclk():
    cookie_string = 'JSESSIONID=sc0lK5ezLiJQC-cbkgZThCMDnkaFJNlhCuDdAv5n.pawebhst39a; citrix_ns_id_.clacks.gov.uk_%2F_wat=AAAAAAU2RpQrZ81FIns9jSrf1EPOBG2wnBgC9ABjgbVL4SgCxi5_c9TopHJkppF4u6ITzTBtgPAjD-T5-7FRPmyWUtSE#MKWRAxvxfrLD5WG+jw7Oiw2P/gUA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsedum():
    cookie_string = 'JSESSIONID=IcVirKIbE8nROoITqvfNxk8-3dRlw1SCzbpzniPf.pawebhst26a; citrix_ns_id_.dumgal.gov.uk_%2F_wat=AAAAAAXwJBzZos5N7_ob8wqlifs15YekzD709L472eIElVUp9YuJ62t77l4UbNFNDXU2x8CKFYivAGfyuGr3pSOSw3F5#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsedun():
    cookie_string = 'JSESSIONID=StyfpokY4CZ7SpsF6nZ4E6EHwkmlWKO9-m1cRzR5.2012-idox-iis; __utmc=49359486; __utmz=49359486.1679736213.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=49359486.1559562858.1679736213.1679736213.1679757044.2; __utmt=1; __utmb=49359486.1.10.1679757044'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseeas():
    cookie_string = 'JSESSIONID=jL15KiPgarvrhuVV99O3cw9Y2I6CJhMvn0M3jf1Z.edmsweb03; CookieControl={"necessaryCookies":[],"optionalCookies":{"analytics":"accepted"},"statement":{"shown":true,"updated":"29/11/2019"},"consentDate":1679666751326,"consentExpiry":90,"interactedWith":true,"user":"4A6CFBA8-25EE-4789-9948-9641E4A1FA9B"}'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseead():
    cookie_string = 'JSESSIONID=bzqZM8JCXBisxVhPu3DAUoaAEdagehe_kqhejY8x.plan-web-1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseeal():
    cookie_string = 'JSESSIONID=xUrr9-II_rkfFuKY-UcME39rJOHN3zjFO8ORtvva.cotton'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseear():
    cookie_string = 'JSESSIONID=aSjS3i5Gwn3yFoJLrC0un6NMlbS19nSWFbO8t4iy.idoxweb-live'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parseedb():
    cookie_string = 'JSESSIONID=b-ecyZ5fLmh4Xk77A3A9sagOJ01BekTDxFmAcHfy.lap-pubacc2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseflk():
    cookie_string = 'JSESSIONID=vSpLGToMG074vWz54Q1UD3GQE0g_QdmRUAgYI9X7.s-fk-ep-paweb'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsefif():
    cookie_string = 'JSESSIONID=aSjS3i5Gwn3yFoJLrC0un6NMlbS19nSWFbO8t4iy.idoxweb-live'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseglg():
    cookie_string = 'JSESSIONID=jCT1vT65RIPxoJYh1rDP_g1Fspu6MDvudImNQcEu.gcwgnclidxl01'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsehig():
    cookie_string = 'JSESSIONID=h5e7fYe_eTeRFHcJfzStIQDCyWS4IjtL9-zobXEf.pawebhst17a; citrix_ns_id_.highland.gov.uk_%2F_wat=AAAAAAWFGPfIsbWHrG8pnOUQTvK_idweiSEvTPgIpIZUW1QaJWsqD4MFxqnKAIp88DXstlDvTw2YpX6nASYvOr7s-Zui#O5/8TkatWotXuO7O313UTD03u3oA&; CookieControl={"necessaryCookies":[],"optionalCookies":{},"statement":{"shown":true,"updated":"09/07/2020"},"consentDate":1679692845768,"consentExpiry":90,"interactedWith":true,"user":"59D4446B-F49E-43F9-8C6D-3D4CE276C3CE"}'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseinv():
    cookie_string = 'JSESSIONID=wy8NhIrq6qGepSrydFC6HFrWXzPgKc-OnoVtZ6ed.invidoxweb2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parselol():
    cookie_string = 'JSESSIONID=ll3Gl-UsKHbulHAr4lsiEZmwHYP-Ihu5gnWl0XcN.idoxweb; __utmc=250927186; __utmz=250927186.1679706843.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=250927186.1848098484.1679706843.1679706843.1679759865.2; __utmt=1; __utmb=250927186.2.10.1679759865'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsemid():
    cookie_string = f'JSESSIONID=oG4JaWw4vCAiCXezstozCAYbpzKwVbYsQQujfrbi.pawebhst49a; citrix_ns_id_.midlothian.gov.uk_%2F_wat=AAAAAAWWkxxzIafEfsonoa_lU5Aas8HdBRIunnksXFqqRLMHyPfIneZQpT0eval4h8P_zwzzGAJFGhWciTICT13mj_f8#dcLYf+bC79jQY1XncvhA9CvOlKsA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsemor():
    cookie_string = 'JSESSIONID=lwo7Cddtlto0P5BUmzeHDq3XVTsHG8G6a0pBsTec.mvs237'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parsenoa():
    cookie_string = 'JSESSIONID=G6XTLJKkhLV1KM2R1mcjlkfQ-_huEatWe6Z_HsHg.naveplanwam2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parsenol():
    cookie_string = 'JSESSIONID=aEk17DCLl7mGREaFh_Y8QJGGAG59qTVfU1uMilhr.ukspnlanipawb01'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie


def cookies_parseoid():
    cookie_string = 'JSESSIONID=In8dHqzuNsUFdQycWnZfqkY9PCmyoflKcXnSbs-5.oic-vedrms-web2'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parseper():
    cookie_string = 'JSESSIONID=ul9mJveH-ga_u21NALZLBnY3b7TI_a-ffCXGGYqI.perwebidoxpa; _ga=GA1.1.820367051.1678376383; _ga_PB86DF8R71=GS1.1.1679788360.2.1.1679788369.0.0.0'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parseref():
    cookie_string = 'JSESSIONID=jypoGBuKB0g11gAe7gHC1wnKn3zjASp0j1th0h2U.vmsgofw-unipal; TS013efb75=018d8f6012789678ee212ee3a74be0e49175347be30c637ddf1acaf1125de6fce60f70568a8d460b8dbddcdeba611df3c3560f288c82cf2e579463427aa6bcd910a97d3d61; TS014f6f63=018d8f601215371de070c300d4b788e24a0a090b56a7e2a4a07cf03c37f86864749b374f9b65b2b099f0b03f8d88114fc3b06a4dce'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsesco():
    cookie_string = 'JSESSIONID=Nsu-bDs_OuqXtCTtFNiMs_P516CVkH3REdvoeZlC.hq-pa-web; cookiesession1=678B286E975DC7BEEAADB8484B95904B'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parseshi():
    cookie_string = 'JSESSIONID=11unC5GvBhxKvYZ9kzYJQpv3YNFCt6k_5g37d0_O.uniformpa19; cookiesession1=678A3E2A5E1FAD39B02301BCD2843A6D'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsesoa():
    cookie_string = 'JSESSIONID=IOqtMAlAfFpRNauXg5gtADPVh053NjzxIk6Cc9Uc.pawebhst45a; citrix_ns_id_.south-ayrshire.gov.uk_%2F_wat=AAAAAAX6KeuivUzVPn0iu-8lucF5zprKXWn-dosKBhAbYUnFLs07RjyShbjBFQyhslAMMQRwJ_t2oDrGz-b3IP2BKS5L#guYNW/k4KwVU9addMBooLYQJNuQA&'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parsesol():
    cookie_string = 'JSESSIONID=UecRTealjOvSw5EX-EFw8-ftssVl7jjDCFCKK-Wp.ceridxpweblv'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parsesti():
    cookie_string = 'JSESSIONID=OYobiJPAb3Y7HiHCwHts1LSsH_oZyTr5lDKKeaan.paweblive'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsewed():
    cookie_string = 'JSESSIONID=TVne1Kxu7ArTiCYTPnjwl3n-FIS-vLe1uEmOeA9T.paweblive'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parsewel():
    cookie_string = 'JSESSIONID=EiDnS-mx4qkSj0mk_12vp3Uevs1KGc_yR2XHLiYX.ext-pa2web-02; _ga=GA1.3.1230909570.1679768054; _gid=GA1.3.341067379.1679768054; _gat=1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parsewei():
    cookie_string = 'JSESSIONID=IkQloHbcm8fFcX_t6bbFq87SVhZYzhJ_D5MaoJ41.idox-pa-web; __utmc=137587185; __utmz=137587185.1677490480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=137587185.1495777887.1677490480.1679768066.1679786960.3; __utmt=1; __utmb=137587185.2.10.1679786960'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsecan():
    cookie_string = 'JSESSIONID=wN69ZNNUXxMhb7AXth2zOy7ywlY2QHLRP8FEiWY4.idoxweb; __utma=149224802.562058197.1679706215.1679706215.1679706215.1; __utmc=149224802; __utmz=149224802.1679706215.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=149224802.2.10.1679706215'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie
def cookies_parsemor():
    cookie_string = 'JSESSIONID=q1n0HPxfzsXCPkVd8vuSGril2QTl6morcCTWmpBn.mvs237'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    parsed_cookie = {}
    for key,morsel in cookie.items():
        parsed_cookie[key] = morsel.value
    
    return parsed_cookie

def cookies_parsemdl():
    cookie_string = 'JSESSIONID=BKZZoh0C3EYwd8-bA4hYnTeakG2Ww4SrWMhDALnw.pawebhst49a; citrix_ns_id_.midlothian.gov.uk_%2F_wat=AAAAAAVBfm03gjNE52XNRLPDNQqWLMfmVAiivEa09Kgjv6JDg8FrkUJ_7drOq2tOaHMIKs37NVGyxXuOxgaQdXbAuqZA#dcLYf+bC79jQY1XncvhA9CvOlKsA&'
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


    