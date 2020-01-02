
import datetime
from functools import wraps

def logUtils(dir="log.txt"):
    def logging(func):
        @wraps(func)
        def wrapper():
            with open(dir, "a+") as file:
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
