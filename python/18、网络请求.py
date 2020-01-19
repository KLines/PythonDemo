from urllib import request,parse,error
from http.client import HTTPResponse
from http import cookiejar,cookies
import json,random,ssl

'''

https://www.cnblogs.com/fiona-zhong/p/10179421.html
https://www.kancloud.cn/turing/www-tuling123-com/718227
https://www.cnblogs.com/my8100/p/7271564.html

    
HTTP内容编码：在http协议中，可以对内容（也就是body部分）进行编码
    1、可以采用压缩编码，比如gzip这样的从而达到压缩的目的，因此http压缩就是HTTP内容编码的一种
    2、可以使用其他的编码把内容搅乱或加密，以此来防止未授权的第三方看到文档的内容
   
        
HTTP压缩：采用通用的压缩算法，比如gzip来压缩HTML,Javascript, CSS文件，能大大减少网络传输的数据量，提高了用户显示网页的速度
    1、压缩过程：
        1、发送request包含Accept-Encoding: gzip, deflate。(告诉服务器， 浏览器支持gzip压缩)
        2、Web服务器接到request后，生成原始的response, 其中有原始的Content-Type和Content-Length
        3、Web服务器通过Gzip来对Response进行编码，编码后header中有Content-Type和Content-Length(压缩后的大小)，并且增加了Content-Encoding:gzip
        4、将response发送给浏览器，然后根据Content-Encoding:gzip来对response进行解码，获取到原始response后显示出网页 
    2、Content-Encoding值
        gzip：表明实体采用GNU zip编码，PEG这类文件用gzip压缩的不够好
            　简单来说， Gzip压缩是在一个文本文件中找出类似的字符串，并临时替换他们，使整个文件变小。这种形式的压缩对Web来说非常适合， 
            　因为HTML和CSS文件通常包含大量的重复的字符串，例如空格，标签
        compress：表明实体采用Unix的文件压缩程序
        deflate：表明实体是用zlib的格式压缩的
        identity：表明没有对实体进行编码。当没有Content-Encoding header时， 就默认为这种情况
        gzip, compress, 以及deflate编码都是无损压缩算法，用于减少传输报文的大小，不会导致信息损失，其中gzip通常效率最高， 使用最为广泛。
'''


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
def set_headers():
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip,deflate,br',  # 支持的压缩编码
        'Accept-language':'zh-CN,zh;q=0.9',
        'Accept-Charset':'utf-8',
        'Connection':'keep-alive',
        'User-Agent':random.choice(USER_AGENTS)
        # 'Cookie':'token=demo'
        # 'User-Agent':'Python-urllib/3.7'
    }
    return headers


# 解码response
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


# 打印header
def get_response(req:request.Request,resp:HTTPResponse):

    if req:
        print("<------request header------->")
        for item in req.header_items():
            print(': '.join(item))

    print("<------response header------->")
    print(resp.code,resp.msg)
    print(resp.headers)

    print("<------response body------->")
    for item in cookie_list: # type: cookiejar.Cookie
        print(': '.join([item.name,item.value]))
        print(item.domain)
    print(decode_data(resp))


'''
    1、全局自定义opener：
        设置代理服务器、添加headers、设置debug模式、cookie
    2、模拟Get、Post请求
        异步请求，取消任务
    3、异常信息：
        http.client.RemoteDisconnected: Remote end closed connection without response：校验SSL证书
        ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]：服务器根据 UA 来判断拒绝了 python 爬虫
'''
# 设置request中的cookie
cookie_list = cookiejar.CookieJar()
cookie1 = cookiejar.Cookie(0,'token', 'test', None, None, '.baidu.org',
                          None, None, '/', None, None, None, None, None, None, None, True)
cookie2 = cookiejar.Cookie(0,'channel', 'official', None, None, '.httpbin.org',
                           None, None, '/', None, None, None, None, None, None, None, True)

# 设置response中的cookie
C = cookies.SimpleCookie()
C["fig"] = "newton"
C["fig"]["domain"] = ".baidu.com"
print(C)
print(C.output(header="Cookie:"))


# 自定义全局opener
def request_opener():
    # 忽略ssl证书验证
    ssl._create_default_https_context = ssl._create_unverified_context
    # 设置http请求debug模式
    http_handler = request.HTTPHandler(debuglevel=1)
    # 设置代理服务器
    http_proxy = request.ProxyHandler({'http': 'http://127.0.0.1:8888/'})
    https_proxy = request.ProxyHandler({'https': 'https://127.0.0.1:8888/'})

    cookie_list.set_cookie(cookie1)
    cookie_list.set_cookie(cookie2)

    cookie_handler = request.HTTPCookieProcessor(cookie_list) # 创建cookie处理器
    # 创建opener
    opener = request.build_opener(cookie_handler)
    # 设置headers
    opener.addheaders = set_headers().items() # 默认是 [('User-agent', 'Python-urllib/3.7')]
    # 设置全局opener
    request.install_opener(opener)


# Get请求
def request_get():

    print("request_get")


    # url = 'https://www.baidu.com'
    url = 'http://httpbin.org/ip'
    # url = 'https://www.httpbin.org/get'
    # 无参数，底层调用OpenerDirector
    with request.urlopen(url) as resp:  # type: HTTPResponse
        get_response(None,resp)


    # 带参数
    params = {}
    params.update(name='test',age=20)
    get_params = parse.urlencode(params)
    new_url = '?'.join([url,get_params]) # join参数为 list、tuple
    print(new_url)
    with request.urlopen(new_url) as resp:  # type: HTTPResponse
        get_response(None,resp)


# Post请求
def request_post():

    print("request_post")

    url = "https://www.httpbin.org/post"

    data = {
            "userName":"test",
            "password":"123456"
    }

    req = request.Request(url)
    req.add_header('Content-Type', 'application/json')
    post_params = json.dumps(data).encode('utf-8') # 变成byte类型
    with request.urlopen(req,data=post_params,timeout=10) as resp: # type: HTTPResponse
        get_response(req,resp)


def request_demo():

    # 设置代理，通过fiddler抓包
    proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:8888/'})
    opener = request.build_opener()

    # Get请求
    url = 'http://jfx.qdfaw.com:8081/api/qingqi/product/login'
    params = {'userName':'linqi', 'password': 'Qweasd','deviceId': '111'}
    new_url = '?'.join([url, parse.urlencode(params)])
    req = request.Request(new_url,headers=set_headers())
    print(new_url)
    with opener.open(req) as resp:  # type: HTTPResponse
        get_response(req,resp)


    # Post请求
    url = 'http://itg.sih.cq.cn:18080/api/hongyan/serverstation/login'
    req = request.Request(url)
    req.add_header('Content-Type', 'application/json')
    dict_data = {'userName':'zhfan01', 'password': '123456','deviceId': '111', 'deviceType': '1'}
    post_params = json.dumps(dict_data).encode('utf-8')
    with opener.open(req,data=post_params,timeout=10) as resp:  # type: HTTPResponse
        get_response(req,resp)


if __name__ == '__main__':

    try:




        request_opener()

        # request_get()

        request_post()


        # request_proxy_handler()

    except error.HTTPError as e:
        print(e)

    except:
        raise