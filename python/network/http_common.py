import random,logging

'''
headers使用

    1、urllib底层默认设置：
        headers["Connection"] = "close" 
        headers["User-Agent"] = "Python-urllib/%s" % __version__
    2、request header中Accept-Encoding中若包含gzip，response header通常会返回Content-Encoding: gzip
    3、response header中包含Content-Encoding: gzip，需要先解压再转码
'''

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


'''配置日志'''
LOG_FORMAT = "%(asctime)s-->%(levelname)s-->HTTP-->%(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
logging.basicConfig(level=logging.DEBUG,
                    format= LOG_FORMAT,
                    datefmt= DATE_FORMAT)