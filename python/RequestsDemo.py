import network


# Get请求
def request_get():

    # 无参数
    url = 'https://www.httpbin.org/get'
    network.requests_utils(url,'get')

    # 带参数
    params = {}
    url = 'https://www.httpbin.org/get'
    params.update(name='测试',age=20,flag=True,company=None)
    network.requests_utils(url,'get',params=params)


# Post请求
def request_post():

    url = "https://www.httpbin.org/post"
    data = {
            "userName":"test",
            "password":"1234",
            "flag":True,
            "company":None
           }

    # 表单入参
    network.requests_utils(url,'post',data=data)

    # json入参，实际就是字典类型数据
    network.requests_utils(url,'post',json=data)


# 设置cookie
def request_cookie():

    network.set_cookies('channel','official','.httpbin.org')
    url = 'https://www.httpbin.org/get'
    network.requests_utils(url,'get')

    network.set_cookies('version','1','.httpbin.org')
    network.headers.update({'test':'temp'})
    url = 'https://www.httpbin.org/get'
    network.requests_utils(url,'get')

    network.set_cookies('version','2','.httpbin.org')
    network.set_cookies('token','sdfqazxv=','.httpbin.org')
    url = 'https://www.httpbin.org/get'
    network.requests_utils(url,'get')


# 使用session
def request_session():

    network.set_cookies('channel','official','getman.cn')

    url = 'https://getman.cn/mock/test'
    network.requests_session(url,'get')

    network.headers.update({'test':'temp'})
    url = 'https://getman.cn/mock/demo'
    network.requests_session(url,'get')

    url = "https://www.httpbin.org/post"
    data = {
        "userName":"test",
        "password":"1234",
        "flag":True,
        "company":None
    }

    # 表单入参
    network.requests_session(url,'post',data=data)


if __name__ == '__main__':

    # request_get()

    # request_post()

    # request_cookie()

    request_session()
