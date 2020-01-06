#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'liuk'

import datetime
from functools import wraps

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

myFunc1()
myFunc2()

import time
if __name__ == '__main__':

    # 字符串的时间转换为时间戳
    str = "2020/5/10 23:40:00"
    # 先转换为时间数组
    timeArray = time.strptime(str, "%Y/%m/%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)

    # 时间戳转换为指定格式的字符串时间
    timeStamp = 1589125200
    timeArray = time.localtime(timeStamp)
    str = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
    print(str)

    # 获取当前时间
    nowTime = datetime.datetime.now()
    # 获取当前时间戳
    nowStramp = time.time()
    print(nowTime)
    print(nowStramp)
    nowTime.strftime("%Y-%m-%d %H:%M:%S")
    int(nowStramp)

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