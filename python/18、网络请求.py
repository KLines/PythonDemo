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
    dict_data = {'userName':'zhbjfan01', 'password': '123456','deviceId': '111', 'deviceType': '1'}
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


# 设置cookie
def request_cookie():

    network.set_cookies('channel','official','getman.cn')

    url = 'https://getman.cn/mock/test'
    network.urllib_utils(url,'get')

    network.headers.update({'test':'temp'})
    url = 'https://getman.cn/mock/demo'
    network.urllib_utils(url,'get')


if __name__ == '__main__':

    # request_demo()

    request_get()

    # request_post()

    # request_cookie()

    # 保持数据
    # params = {}
    # params.update(name='测试',age=20,flag=True,company=None)
    # url = '?'.join(['https://www.httpbin.org/get', parse.urlencode(params)])
    # resp = request.urlretrieve(url, filename='test.txt')
