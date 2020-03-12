
from wsgiref.simple_server import make_server
from web.client import application

# coding:utf-8

"""
desc: WSGI服务器实现

1、数据库：索引、事务、视图、SQL注入
2、网络通信

"""

def server():
    httpd = make_server('',8000,application)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    server()