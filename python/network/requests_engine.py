import requests
from requests.cookies import  RequestsCookieJar
from .http_common import *

'''
requests

    1、Get请求
        requests.get(url)　
        requests.get(url, params={"param1":"hello"})　# requests会自动将参数添加到url后面
　　　　
    2、Post请求
        requests.post(url, data={"key":"value"}) # 默认使用 application/x-www-form-urlencoded 
        requests.post(url, json={"key":"value"})　# 使用 application/json
        　　
    3、添加headers和cookie信息
        headers = {"name":"value"}
        cookie = {"name":"value"}
        requests.get(url, headers=header, cookie=cookie)
        requests.post(url, headers=header, cookie=cookie)
    
    4、使用requests.get/post后会返回requests.Response对象，其存储了服务器的响应内容
        resp.request        　 　 # 获取requests.PreparedRequest对象
        resp.url　　　　　　　　    # 获取请求url
        resp.status_code　　　　　 # 响应状态码
        resp.reason　　　　　　　　 # 响应状态码内容
        resp.headers　　　　   　  # 以字典形式存储服务器响应头。但是这个字典不区分大小写，若key不存在，则返回None
        resp.cookies　　　　　　   # 返回响应中包含的cookie，cookies.RequestsCookieJar对象
        resp.encoding            # 获取当前编码
        resp.encoding='utf8'     # 设置编码
        resp.text　　    　　　　  # 以encoding解析返回内容。字符串形式的响应体会自动根据响应头部的编码方式进行解码
        resp.content    　　　　  # 以字节形式（二进制）返回。字节方式的响应体，会自动解析gzip和deflate压缩
        resp.json()  　　　　　　  # requests中内置的json解码器。以json形式返回，前提是返回的内容确实是json格式的，否则会报错
        resp.raise_for_status()　# 失败请求抛出异常
        resp.history　　　　　　   # 返回重定向信息。我们可以在请求时加上allow_redirects=False 来阻止重定向
        resp.elapsed　　　　　　   # 返回timedelta，响应所用的时间 
'''


'''
自定义全局session：

    1、设置统一的headers、cookies
    2、自动将response返回的Set-cookie值携带到request请求头的cookie中
    3、主要用于同一域名下接口测试
'''

sess = None

def __init_session():

    global sess
    sess = requests.Session()
    # 设置 headers
    sess.headers = headers
    # 设置 cookies
    cookie_jar = RequestsCookieJar()
    if cookie_list:
        for item in cookie_list:
            cookie_jar.set(item['name'],item['value'],domain=item['domain'])
    sess.cookies = cookie_jar
    # 设置代理
    # sess.proxies = {'http': 'http://127.0.0.1:8888/','https': 'https://127.0.0.1:8888/'}


def requests_session(url:str,method:str,**kwargs):

    req_method = method.upper()

    if 'GET' != req_method and 'POST' != req_method:
        return

    try:
        if sess is None:
            __init_session()
        func = sess.get if 'GET' == req_method else sess.post
        with func(url,**kwargs) as resp:
            __http_log(resp.request,resp)
    except requests.exceptions.RequestException as e:
        log_error(e)
    except:
        raise


'''
requests请求工具
    1、使用Get、Post请求
    2、每个请求设置独立的headers、cookies
    3、主要用于测试单个接口
'''


__switcher = {
    "GET": requests.get,
    "POST": requests.post
}

def requests_utils(url:str,method:str,**kwargs):

    req_method = method.upper()

    if req_method not in __switcher.keys():
        return

    try:
        func = __switcher.get(req_method)
        # 设置 cookies
        cookie_jar = RequestsCookieJar()
        if cookie_list:
            for item in cookie_list:
                cookie_jar.set(item['name'],item['value'],domain=item['domain'])
        cookie_list.clear()
        # 每次请求都是独立的，需要设置请求头
        with func(url,headers=headers,cookies=cookie_jar,timeout=10,**kwargs) as resp:
            __http_log(resp.request,resp)
    except requests.exceptions.RequestException as e:
        log_error(e)
        raise e
    except:
        raise


'http日志信息'


def __http_log(req:requests.PreparedRequest = None,resp:requests.Response = None):

    if req is not None:

        log_info("------request header-------")
        log_info('url:'+req.url)
        log_info('method:'+req.method)
        for header in req.headers.items():
            log_info(': '.join(header))

        if req.body is not None:
            log_info("------request body-------")
            if 'Content-Type' in req.headers and 'application/json' == req.headers['Content-Type']:
                log_info('body:'+req.body.decode('utf-8'))
            else:
                log_info('body:'+req.body)

    if resp is not None:

        log_info("------response header-------")
        log_info("%s %s"%(resp.status_code,resp.reason))
        for header in resp.headers.items():
            log_info(': '.join(header))

        log_info("------response body-------")
        log_info(resp.text)
        resp.raise_for_status()
