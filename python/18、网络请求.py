from http.client import HTTPResponse
from urllib import request, parse

import json
import network

'''

https://www.cnblogs.com/fiona-zhong/p/10179421.html


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
        
        
HTTP请求：

    1、模拟Get、Post请求
    2、异步请求，取消任务
'''


def request_demo():

    # Get请求
    url = 'http://jfx.qdfaw.com:8081/api/qingqi/product/login'
    params = {'userName':'linqi', 'password': 'Qweasd','deviceId': '111'}
    new_url = '?'.join([url, parse.urlencode(params)])
    print(new_url)
    # 底层调用OpenerDirector
    with request.urlopen(new_url) as resp:  # type: HTTPResponse
        print(resp.read().decode('utf-8'))


    # Post请求
    url = 'http://itg.sih.cq.cn:18080/api/hongyan/serverstation/login'
    req = request.Request(url,headers=network.headers)
    req.add_header('Content-Type', 'application/json')
    dict_data = {'userName':'zhfan01', 'password': '123456','deviceId': '111', 'deviceType': '1'}
    post_params = json.dumps(dict_data).encode('utf-8')
    with request.urlopen(req,data=post_params,timeout=10) as resp:  # type: HTTPResponse
        print(resp.read().decode('utf-8'))




cookie_list = [{'name':'token','value':'test1','domain':'.httpbin.org'},
               {'name':'BAIDUID','value':'tesdsff=','domain':'.httpbin.org'}]


# Get请求
def request_get():

    # 无参数
    url = 'https://www.httpbin.org/get'
    network.urllib_utils(url,'get')

    # 带参数
    url = 'https://www.baidu.com'
    url = 'https://www.httpbin.org/get'
    params = {}
    params.update(name='测试',age=20,flag=True,company=None)
    network.urllib_utils(url,'get',params=params)

    # 重置request中的cookie
    # for item in my_cookiejar: # type: cookiejar.Cookie
    #     if 'BAIDUID'==item.name:
    #         value = item.value
    #         break
    # cookie_list[0]['value'] = 'test2'
    # cookie_list[1]['value'] = "tesdsfffsdfsdfds="
    # HttpUtils.set_request_cookies(cookie_list)

# Post请求
def request_post():


    url = "https://www.httpbin.org/post"

    data = {
            "userName":"test",
            "password":"123456",
            "flag":True,
            "company":None
           }

    network.urllib_utils(url,'post',params=data)

    network.urllib_utils(url,'post',json_data=data)


if __name__ == '__main__':

    # HttpUtils.set_request_cookies(cookie_list)  # 设置cookie
    # my_cookiejar = HttpUtils.my_cookiejar  # type: cookiejar.LWPCookieJar

    request_get()

    request_post()

    # for item in my_cookiejar: # type: cookiejar.Cookie
    #     print(':'.join([item.name,item.value]))
