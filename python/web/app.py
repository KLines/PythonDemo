


'''

application()：符合WSGI标准的一个HTTP处理函数，它接收两个参数

    environ：一个包含所有HTTP请求信息的dict对象

    start_response：一个发送HTTP响应的函数

    函数的返回值将作为HTTP响应的Body发送给浏览器，必须是byte类型

start_response()：发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次函数，它接收两个参数

    一个是HTTP响应码

    一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示

'''

def application(environ,start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'<h3>Hello, web!</h3>']
