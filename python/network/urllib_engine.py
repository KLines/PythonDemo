import json,ssl
from http import cookiejar
from http.client import HTTPResponse
from urllib import request, parse, error
from socket import timeout

from .http_common import *


'''
自定义全局opener：

    1、设置代理服务器
    2、设置debug模式
    3、添加headers、cookie
    4、异常信息：  
        校验SSL证书：
            ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]       
        解决方法：
            1、使用ssl创建未经验证的上下文，在urlopen中传入上下文参数：context = ssl._create_unverified_context()
            2、关闭证书验证：ssl._create_default_https_context = ssl._create_unverified_context
        
        服务器根据 UA 来判断拒绝了 python 爬虫：
            http.client.RemoteDisconnected: Remote end closed connection without response
'''


opener = None

my_cookiejar = None

def __init_opener():

    global opener,my_cookiejar
    # 创建opener
    opener = request.build_opener()

    # 忽略ssl证书验证
    ssl._create_default_https_context = ssl._create_unverified_context

    # 设置http请求debug模式
    http_handler = request.HTTPHandler(debuglevel=1)

    # 设置代理服务器
    proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:8888/','https': 'https://127.0.0.1:8888/'})

    # 设置cookie
    my_cookiejar = cookiejar.CookieJar()   # 创建cookie管理器
    if cookie_list:
        for item in cookie_list:
            # 多个Cookie对象中name若一致，则只会添加一个Cookie对象
            cookie = cookiejar.Cookie(0,item['name'],item['value'], None, None, item['domain'],
                                      None, None, '/', None, None, None, None, None, None, None, False)
            my_cookiejar.set_cookie(cookie)
    cookiejar_handler = request.HTTPCookieProcessor(my_cookiejar)  # 创建cookie处理器
    opener.add_handler(cookiejar_handler)

    # 设置headers
    opener.addheaders = headers.items() # 默认是 [('User-agent', 'Python-urllib/3.7')]

    # 设置全局opener
    request.install_opener(opener)


'urllib请求工具'


def urllib_utils(url:str,method:str,params=None,json_data=None):

    req_method = method.upper()

    if 'GET' != req_method and 'POST' != req_method:
        return

    try:

        if opener is None:
            __init_opener()

        if params is not None:
            # 去掉 None
            if None in params.values():
                for key,value in params.items():
                    if None == value:
                        params.pop(key)
                        break
            # 拼接参数
            params = parse.urlencode(params)
            if 'GET' == req_method:
                url = '?'.join([url,params])
                params = None
            else:
                params = params.encode('utf-8') # 变成byte类型

        req = request.Request(url)

        if json_data is not None:
            params = json.dumps(json_data).encode('utf-8')
            req.add_header('Content-Type', 'application/json')

        with opener.open(req,data=params,timeout=10) as resp:
            __http_log(req,resp)

    except error.URLError as e: # HTTPError是 URLError的子类
        log_error(e)
        # if hasattr(e,'code'):
        #     print('code: '+str(e.code))
        # if hasattr(e,'reason'):
        #     print('reason'+e.reason)
        # if hasattr(e,'headers'):
        #     print('headers',e.headers)
    except timeout as e:
        log_error('socket.timeout:'+str(e))
    except:
        raise

    for item in my_cookiejar:
        print(item)


'http日志信息'


def __http_log(req:request.Request = None,resp:HTTPResponse = None):

    if req is not None:

        log_info("------request header-------")
        log_info('url:'+req.full_url)
        log_info('method:'+req.get_method())
        for header in req.header_items():
            log_info(': '.join(header))

        if req.data is not None:
            log_info("------request body-------")
            log_info(req.data.decode('utf-8'))

    if resp is not None:

        log_info("------response header-------")
        log_info("%s %s"%(resp.code,resp.msg))
        for header in resp.headers.items():
            log_info(': '.join(header))

        log_info("------response body-------")
        log_info(__decode_data(resp))


'解码response中的数据'


def __decode_data(resp:HTTPResponse):
    type = resp.getheader('Content-Encoding')
    if 'gzip'==type:
        from io import BytesIO
        import gzip
        buff = BytesIO(resp.read())
        f = gzip.GzipFile(fileobj=buff)
        return f.read().decode('utf-8')
    elif 'br' == type:
        import brotli
        f = brotli.decompress(resp.read())
        return f.decode('utf-8')
    else:
        return resp.read().decode('utf-8') # 返回的数据为byte类型，使用utf-8解码
