import requests
import random,logging


USER_AGENTS =[
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
]


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip,deflate,br',  # 支持的压缩编码
    'Accept-language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'User-Agent':random.choice(USER_AGENTS)
}


'配置日志'

LOG_FORMAT = "%(asctime)s-->%(levelname)s-->HTTP-->%(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
logging.basicConfig(level=logging.DEBUG,
                    format= LOG_FORMAT,
                    datefmt= DATE_FORMAT)


def log_info(msg):
    logging.info(msg)


def log_error(msg):
    logging.error(msg)


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
        # 每次请求都是独立的，需要设置请求头
        with func(url,headers=headers,timeout=10,**kwargs) as resp:
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
