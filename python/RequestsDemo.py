import requests,HttpUtils,json,logging
from requests import cookies


'''
requests默认使用application/x-www-form-urlencoded对POST数据编码
'''

LOG_FORMAT = "%(asctime)s-->%(levelname)s-->HTTP-->%(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"

logging.basicConfig(level=logging.DEBUG,
                    format= LOG_FORMAT,
                    datefmt= DATE_FORMAT)


# 打印http日志信息
def log_info(req:requests.PreparedRequest = None,resp:requests.Response = None):

    if req is not None:

        logging.info("------request header-------")
        logging.info('url:'+req.url)
        logging.info('method:'+req.method)
        for header in req.headers.items():
            logging.info(': '.join(header))

        logging.info("------request body-------")
        if 'Content-Type' in req.headers and 'application/json' == req.headers['Content-Type']:
            logging.info('body:'+req.body.decode('utf-8'))
        else:
            logging.info('body:'+req.body)

    if resp:

        logging.info("------response header-------")
        logging.info("%s %s"%(resp.status_code,resp.reason))
        for header in resp.headers.items():
            logging.info(': '.join(header))

        logging.info("------response body-------")
        logging.info(resp.text)

        cookie_list = resp.cookies # type: cookies.RequestsCookieJar



def request_utils(url:str,method:str,**kwargs):

    request_method = method.upper()
    request_headers = HttpUtils.set_request_headers()
    if 'GET' == request_method:
        resp = requests.get(url,headers=request_headers,**kwargs)
    elif 'POST' == request_method:
        resp = requests.post(url,headers=request_headers,**kwargs)
    else:
        return

    log_info(resp.request,resp)


# Get请求
def request_get():

    print("===== request_get ======")

    # 无参数
    url = 'https://www.baidu.com'
    request_utils(url,'get')

    # 带参数
    params = {}
    url = 'https://www.httpbin.org/get'
    params.update(name='测试',age=20)
    request_utils(url,'get',params=params)


# Post请求
def request_post():

    print("===== request_post ======")

    url = "https://www.httpbin.org/post"

    data = {
        "userName":"test",
        "password":"123456"
    }

    request_utils(url,'post',json=data)


if __name__ == '__main__':

    # request_get()

    request_post()