
from wsgiref.simple_server import make_server
from wsgi.app import application

# coding:utf-8

"""

Java：浏览器-->Nginx-->Tomcat-->Java Web应用程序

Python：浏览器-->Nginx-->uWSGI-->WSGI协议-->Python Web应用程序

web服务器：
    Apache/Nginx：是一个HTTP Server，侧重关心HTTP协议层面的传输和访问控制，比如代理、负载均衡等功能
    Tomcat：是一个web应用服务器，运行部署的Java Web代码
    uWSGI：是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议

Web Server Gateway Interface：
    WSGI是一种在 Web 服务器和 Python Web 应用程序框架之间的标准接口。通过标准化 Web 服务器和 Python web 应用程序框架之间的行为和通信，
    使得编写可移植的的 Python web 代码变为可能，使其能够部署在任何符合 WSGI 的 web 服务

"""

def server():
    # application()函数必须由WSGI服务器来调用
    httpd = make_server('',8000,application)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    server()