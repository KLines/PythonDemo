from urllib import request,parse,error
from http.client import HTTPResponse
import json,random
from io import BytesIO
import gzip


'''
内建模块：urllib
    1、Get、Post请求
    2、参数拼接：Get请求参数，Post请求参数（json格式）
    3、添加请求头：cookie
    4、异步请求，取消任务
    https://www.cnblogs.com/fiona-zhong/p/10179421.html
    https://www.kancloud.cn/turing/www-tuling123-com/718227
    https://blog.csdn.net/zhangzeguang88/article/details/51554097
    
'''

USER_AGENTS =[
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
]

'''
request模块header默认值
    1、headers["Connection"] = "close"
    2、headers["User-Agent"] = "Python-urllib/%s" % __version__
    Content-Encoding: gzip
'''
def request_headers():
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip,deflate,br',
        'Accept-language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'User-Agent':random.choice(USER_AGENTS)
        # 'User-Agent':"Python-urllib/3.7"
    }
    return headers


def decode_data(resp:HTTPResponse):
    type = resp.getheader('Content-Encoding')
    if 'gzip'==type:
        buff = BytesIO(resp.read())
        f = gzip.GzipFile(fileobj=buff)
        return f.read().decode('utf-8')
    else:
        return resp.read().decode('utf-8')


def request_opener():
    opener = request.build_opener()
    opener.addheaders = request_headers().items() # 默认是 [('User-agent', 'Python-urllib/3.7')]
    request.install_opener(opener)


def get_response(req:request.Request,resp:HTTPResponse):

    if req:
        print("<------request header------->")
        for item in req.header_items():
            print(': '.join(item))

    print("<------response header------->")
    print(resp.code,resp.msg)
    print(resp.headers)

    print("<------response body------->")
    print(decode_data(resp))


def request_get():

    print("request_get")

    url = 'http://httpbin.org/ip'
    # 无参数
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


def request_post():

    print("request_post")

    url = "http://openapi.tuling123.com/openapi/api/v2"

    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": "附近的酒店"
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": "",
            "userId": ""
        }
    }

    req = request.Request(url)
    post_params = json.dumps(data).encode('utf-8') # 变成byte类型
    with request.urlopen(req,data=post_params) as resp: # type: HTTPResponse
        get_response(req,resp)


def request_proxy_handler():

    # 设置代码，通过fiddler抓包
    proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:8888/'})
    opener = request.build_opener()

    # Get请求
    url = 'http://jfx.qdfaw.com:8081/api/qingqi/product/login'
    params = {'userName':'linqi', 'password': 'Qweasd','deviceId': '111'}
    new_url = '?'.join([url, parse.urlencode(params)])
    req = request.Request(new_url,headers=request_headers())
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

        # request_opener()

        # request_get()

        # request_post()

        request_proxy_handler()

    except error.HTTPError as e:
        print(e)

    except:
        raise