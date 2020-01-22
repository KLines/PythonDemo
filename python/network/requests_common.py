import logging
import requests

from . import headers

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




'''网络请求工具'''


__switcher = {
    "GET": requests.get,
    "POST": requests.post
}

def requests_utils(url:str,method:str,**kwargs):

    try:
        request_method = method.upper()
        if request_method not in __switcher.keys():
            return
        func = __switcher.get(request_method)
        request_headers = headers
        with func(url,headers=request_headers,**kwargs) as resp:
            __http_log(resp.request,resp)
    except requests.exceptions.RequestException as e:
        logging.error(e)
    except:
        raise




'''http日志信息'''


def __http_log(req:requests.PreparedRequest = None,resp:requests.Response = None):

    if req is not None:

        logging.info("------request header-------")
        logging.info('url:'+req.url)
        logging.info('method:'+req.method)
        for header in req.headers.items():
            logging.info(': '.join(header))

        if req.body is not None:
            logging.info("------request body-------")
            if 'Content-Type' in req.headers and 'application/json' == req.headers['Content-Type']:
                logging.info('body:'+req.body.decode('utf-8'))
            else:
                logging.info('body:'+req.body)

    if resp is not None:

        logging.info("------response header-------")
        logging.info("%s %s"%(resp.status_code,resp.reason))
        for header in resp.headers.items():
            logging.info(': '.join(header))

        logging.info("------response body-------")
        logging.info(resp.text)
        resp.raise_for_status()

    # cookie_list = resp.cookies # type: # cookies.RequestsCookieJar
