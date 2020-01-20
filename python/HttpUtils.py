from urllib import request
from http.client import HTTPResponse
from http import cookiejar,cookies
import random,ssl


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


my_cookiejar = None



def init_opener():

    # 创建opener
    opener = request.build_opener()

    # 忽略ssl证书验证
    ssl._create_default_https_context = ssl._create_unverified_context

    # 设置http请求debug模式
    http_handler = request.HTTPHandler(debuglevel=1)

    # 设置代理服务器
    proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:8888/','https': 'https://127.0.0.1:8888/'})

    # 设置cookie
    global my_cookiejar
    my_cookiejar = cookiejar.CookieJar()   # 创建cookie管理器
    cookiejar_handler = request.HTTPCookieProcessor(my_cookiejar)  # 创建cookie处理器
    opener.add_handler(cookiejar_handler)

    # 设置headers
    opener.addheaders = set_request_headers().items() # 默认是 [('User-agent', 'Python-urllib/3.7')]

    # 设置全局opener
    request.install_opener(opener)

    return opener


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


# 设置请求头
def set_request_headers():
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip,deflate,br',  # 支持的压缩编码
        'Accept-language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'User-Agent':random.choice(USER_AGENTS)
    }
    return headers


'''
cookie使用

    1、http.cookiejar：为存储和管理cookie提供客户端支持
        CookieJar：Cookie对象存储在内存中，包含request、response中的cookie信息，若两者中cookie名字一致，则重复显示
        FileCookieJar：检索cookie信息并将信息存储到文件中
        MozillaCookieJar：创建与Mozilla cookies.txt文件兼容的FileCookieJar实例
        LWPCookieJar：创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例
    2、http.cookies：创建以HTTP报头形式表示的cookie数据输出
'''


# 设置request中的cookie
def set_request_cookies(cookie_list:list):
    if not cookie_list or len(cookie_list) == 0:
        return
    for cookie in cookie_list:
        cookie = cookiejar.Cookie(0,cookie['name'], cookie['value'], None, None, cookie['domain'],
                                  None, None, '/', None, None, None, None, None, None, None, False)
        my_cookiejar.set_cookie(cookie)


# 设置response中的cookie
def set_response_cookies():
    cookie = cookies.SimpleCookie()
    cookie["token"] = "test"
    cookie["token"]["domain"] = ".baidu.com"
    print(cookie)
    print(cookie.output(header="Cookie:"))


'''日志信息＆解析数据'''


# 解码response中的数据
def decode_data(resp:HTTPResponse):
    type = resp.getheader('Content-Encoding')
    if 'gzip'==type:
        from io import BytesIO
        import gzip
        buff = BytesIO(resp.read())
        f = gzip.GzipFile(fileobj=buff)
        return f.read().decode('utf-8')
    else:
        return resp.read().decode('utf-8') # 返回的数据为byte类型，使用utf-8解码
