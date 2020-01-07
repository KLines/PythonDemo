
# 捕获异常

print("====== 捕获异常 ======")

try:
    print("程序执行")
    i = 1 / 0
except (OSError,ValueError):
    print("环境异常")
except ZeroDivisionError as err:
    print(err)
    # logging.exception(err)
except:
    print("抛出异常")
    # raise Exception("xxxx") # 抛出指定的异常
    raise
else:
    print("程序没有异常")
finally:
    print("程序结束")

# 自定义异常
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError('test')
except MyError as e:
    print('My exception occurred, value:', e.value)

# 断言使用
assert  1==2,'1 不等于 2'

