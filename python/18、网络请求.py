from urllib import request,parse,error
from http.client import HTTPResponse
import json


'''
内建模块：urllib
    https://www.cnblogs.com/fiona-zhong/p/10179421.html
    https://www.kancloud.cn/turing/www-tuling123-com/718227
'''


def urllib_utils():
    try:
        # Get请求
        url = 'http://jfx.qdfaw.com:8081/api/qingqi/product/login'
        params = {}
        params.update(userName='linqi', password='Qweasd', deviceId='111')
        get_params = parse.urlencode(params)
        new_url = '?'.join([url, get_params])
        print(new_url)
        with request.urlopen(new_url) as resp:  # type: HTTPResponse
            print(resp.status,resp.reason)
            print(resp.info())
            print(resp.read().decode('utf-8'))

        # Post请求
        url = 'http://itg.sih.cq.cn:18080/api/hongyan/serverstation/login'
        req = request.Request(url)
        # req.add_header('Content-Type', 'application/json')
        python_data = {'userName':'zhfan01', 'password': '123456','deviceId': '111', 'deviceType': '1'}
        post_params = json.dumps(python_data).encode('utf-8') # 变成byte类型
        with request.urlopen(req,data=post_params,timeout=10) as resp:  # type: HTTPResponse
            print(resp.status,resp.reason)
            print(resp.info())
            print(resp.read().decode('utf-8'))

    except error.HTTPError as e:
        print(e)
    except BaseException as e:
        print(e)

if __name__ == '__main__':
    urllib_utils()