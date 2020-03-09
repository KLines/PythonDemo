from http.client import HTTPResponse
from urllib import request, parse

import json
import network

'''

https://www.cnblogs.com/fiona-zhong/p/10179421.html
   
HTTP请求：

    1、模拟Get、Post请求
    2、异步请求，取消任务
'''

# 原始urllib请求
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
    print(url)
    print(post_params)
    with request.urlopen(req,data=post_params,timeout=10) as resp:  # type: HTTPResponse
        print(resp.read().decode('utf-8'))


# Get请求
def request_get():

    # 无参数
    url = 'https://www.httpbin.org/get'
    network.urllib_utils(url,'get')

    # 带参数
    url = 'https://www.httpbin.org/get'
    params = {}
    params.update(name='测试',age=20,flag=True,company=None)
    network.urllib_utils(url,'get',params=params)


# Post请求
def request_post():

    url = "https://www.httpbin.org/post"

    data = {
            "userName":"test",
            "password":"123456",
            "flag":True,
            "company":None
           }

    # 表单入参
    network.urllib_utils(url,'post',params=data)

    # json入参
    network.urllib_utils(url,'post',json_data=data)



cookie_list = [{'name':'token','value':'test1','domain':'.httpbin.org'},
               {'name':'BAIDUID','value':'tesdsff=','domain':'.httpbin.org'}]


def request_cookie():
    # 重置request中的cookie
    # url = 'https://www.baidu.com'
    # for item in my_cookiejar: # type: cookiejar.Cookie
    #     if 'BAIDUID'==item.name:
    #         value = item.value
    #         break
    # cookie_list[0]['value'] = 'test2'
    # cookie_list[1]['value'] = "tesdsfffsdfsdfds="
    # HttpUtils.set_request_cookies(cookie_list)
    pass


if __name__ == '__main__':

    # request_demo()

    request_get()

    request_post()

    # request_cookie()

    # HttpUtils.set_request_cookies(cookie_list)  # 设置cookie
    # my_cookiejar = HttpUtils.my_cookiejar  # type: cookiejar.LWPCookieJar

    # for item in my_cookiejar: # type: cookiejar.Cookie
    #     print(':'.join([item.name,item.value]))
