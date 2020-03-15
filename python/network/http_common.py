import random,logging


'''
headers使用

    1、urllib底层默认设置：
        headers["Connection"] = "close" 
        headers["User-Agent"] = "Python-urllib/%s" % __version__
    2、request header中Accept-Encoding中若包含gzip，response header通常会返回Content-Encoding: gzip
    3、response header中包含Content-Encoding: gzip，需要先解压再转码
 
'''


'设置请求头'


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


'''
cookie使用

    1、http.cookiejar：为存储和管理cookie提供客户端支持
        CookieJar：Cookie对象存储在内存中，包含request、response中的cookie信息
        FileCookieJar：检索cookie信息并将信息存储到文件中
        MozillaCookieJar：创建与Mozilla cookies.txt文件兼容的FileCookieJar实例
        LWPCookieJar：创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例
        # save()函数带有两个参数，ignore_discard和ignore_expires
            ignore_discard：即使cookies将被丢弃也将它保存下来
            ignore_expires：cookies已经过期也将它保存并且文件已存在时将覆盖
            
    2、http.cookies：创建以HTTP报头形式表示的cookie数据输出
        SimpleCookie：设置response中的Set-Cookie
            cookie = cookies.SimpleCookie()
            cookie["token"] = "test"
            cookie["token"]["domain"] = ".xxx.com"
            # Set-Cookie: token=test; Domain=.xxx.com
'''


'设置request中的cookie'


cookie_list = []

def set_cookies(name:str,value:str,domain=''):

    if not name or name is None:return
    if not value or value is None:return

    cookie_list.append({'name':name,'value':value,'domain':domain})


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
