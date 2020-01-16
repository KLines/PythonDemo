import time,datetime
from functools import wraps
import collections,re,base64,hashlib

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'liuk'



'函数装饰器'


def logUtils(dir="log.txt"):
    def logging(func):
        @wraps(func)
        def wrapper():
            with open(dir, "a+",encoding='utf-8') as file:
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(time+"\n")
                file.write(wrapper.__name__+" was called\n")
                file.write(wrapper.__doc__ + "\n")
            func()
        return wrapper
    return logging


@logUtils()
def myFunc1():
    'myFunc1 文档说明'
    print("test1")

@logUtils("temp.txt")
def myFunc2():
    'myFunc2 文档说明'
    print("test2")

def wrapper_utils():
    myFunc1()
    myFunc2()


'冒泡排序 & 选择排序'


def sort_utils():
    # 选择排序
    A = [64, 25, 12, 22, 11]
    for i in range(len(A)):
        min = i
        for j in range(i+1,len(A)):
            if(A[min] > A[j]):
                min = j
        A[i],A[min] = A[min],A[i]
    print(A)

    # 冒泡排序
    B = [64, 25, 12, 22, 11]
    for i in range(len(B)):
        for j in range(0,len(B)-i-1):
            if (B[j] > B[j+1]):
                B[j+1], B[j] =B[j], B[j+1]
    print(B)


'''
正则表达式
    \d、\w
    *：表示任意个字符（包括0个）
    +：表示至少一个字符
    ?：表示0个或1个字符
    {n}：表示n个字符
    {n,m}：表示n-m个字符
    []：表示范围，[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}（前面1个字符+后面最多19个字符）
    ()：表示的就是要提取的分组（Group）
    ^：表示行的开头，^\d表示必须以数字开头
    $：表示行的结束，\d$表示必须以数字结束
编译
    使用正则表达式时，re模块内部会干两件事情：
    1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错
    2、用编译后的正则表达式去匹配字符串
    因此可以先预编译正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''


def regular_utils():
    test = '029-88882222'
    regular = r'^\d{3}-\d{5,8}$'
    group = r'^(\d{3})-(\d{5,8})$'
    # 匹配成功，返回一个Match对象，否则返回None
    m = re.match(regular,test)
    print(m)
    # group(0)永远是原始字符串，group(1)是子集
    g = re.match(group,test)
    print(g.group(0))
    print(g[1])
    print(g[2])
    # 预编译
    re_tele = re.compile(r'^(\d{3})-(\d{5,8})$')
    print(re_tele.match('029-88882222').groups())
    print(re_tele.match('029-123456').groups())


'内建模块：datetime'


def time_utils():

    # 字符串的时间转换为时间戳
    str = "2020/5/10 23:40:00"
    timeArray = time.strptime(str, "%Y/%m/%d %H:%M:%S")  # 先转换为时间数组
    timeStamp = time.mktime(timeArray)  # 转换为时间戳
    print("%s-->%s"%(str,timeStamp))

    # 时间戳转换为指定格式的字符串时间
    timeStamp = 1589125200
    timeArray = time.localtime(timeStamp) # 先转换为时间数组
    str = time.strftime("%Y-%m-%d %H:%M:%S",timeArray) # 转换为时间
    print("%s-->%s"%(timeStamp,str))

    # 获取当前时间
    nowTime = datetime.datetime.now()
    # 获取当前时间戳
    nowStramp = time.time()
    print('当前时间：',nowTime)
    print('当前时间戳：',nowStramp)
    # print(nowTime.strftime("%Y-%m-%d %H:%M:%S"))
    # print(int(nowStramp))


'''
内建模块：collections
    1、deque：双向列表
    2、defaultdict：创建一个可以key不存在的dict
    3、OrderedDict：Key会按照插入的顺序排列
    4、ChainMap
    5、Counter：计数器
'''

def collections_utils():

    p = collections.deque([3,2,4])
    p.append(1)
    p.appendleft(5)
    print(p)

    dd = collections.defaultdict(lambda:'N/A')
    dd['key1'] = 'value1'
    print(dd['key1'])
    print(dd['key2'])
    print(dd['key3'])

    od = collections.OrderedDict([('b', 2), ('a', 1), ('c', 3)])
    print(od)

    c = collections.Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
    c.update('hello')
    print(c)


'''
内建模块：base64

base64编解码：一种用64个字符来表示任意二进制数据的方法
    1、base64编码后的数据是一个字符串，其包括a-z、A-Z、0-9、/、+共64个字符，对应数值为0-63，2^6=64
    2、每个6个bit为一组，4*6=24bit，4个为一个单元--->对应3个Byte，3*8=24bit，所以每3个字节一组
    3、数据字节数不是3的倍数时需，Base64用 \x00　在原数据后添加1个或2个零值字节，使其字节数为3的倍数，然后在编码后的字符串后添加1个或2个‘=’，表示零值字节
    4、Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，URL中就是把字符+和/分别变成-和_
'''


def base64_utils():

    # 字符串进行编解码
    st = 'base64编码'
    byte = st.encode('utf-8') # str类型变成byte类型
    base = base64.b64encode(byte) # 转换为base64编码
    print(st,'-->',byte,'-->',base)

    res = base64.b64decode(base)
    st = str(res,'utf-8')
    print(base,'-->',res,'-->',st)


    # 对url的字符串进行编解码
    url = "http://www.baidu.com"
    print(base64.urlsafe_b64encode(url.encode('utf-8')))
    print(str(base64.urlsafe_b64decode(b'aHR0cDovL3d3dy5iYWlkdS5jb20='),'utf-8'))


    print(base64.b64encode('test==='.encode('utf-8')))
    print(str(base64.b64decode(b'dGVzdD09PQ=='),'utf-8'))

    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))


'''
内建模块：hashlib

摘要算法：又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
    1、MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit，通常用一个32位的16进制字符串表示
    2、SHA1的结果是160bit，通常用一个40位的16进制字符串表示
    3、原始数据加一个复杂字符串用md5加密，俗称“md5加盐”，
'''
def hashlib_utils():

    m = hashlib.md5()
    m.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(m.hexdigest())
    m5 = hashlib.md5()
    m5.update("how to use md5 ".encode('utf-8'))
    m5.update("in python hashlib?".encode('utf-8'))
    print(m5.hexdigest())

    s1 = hashlib.sha1()
    s1.update('test'.encode('utf-8'))
    print(s1.hexdigest())


if __name__ == '__main__':

    # wrapper_utils()Counter
    # regular_utils()
    # sort_utils()
    # time_utils()
    # collections_utils()
    # base64_utils()
    hashlib_utils()