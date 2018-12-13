import datetime
from functools import wraps


def logUtils(dir="log.txt"):
    def logging_decorator(func):
        @wraps(func)
        def wrap_function():
            func_name = wrap_function.__name__
            with open(dir, "a+") as file:
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(time + ":\000")
                file.write(func_name)
                file.write(wrap_function.__doc__ + "\n")
            func()
        return wrap_function
    return logging_decorator


@logUtils()
def myFunc1():
    'myFunc1 文档说明'
    print("test1")
    pass

@logUtils("temp.txt")
def myFunc2():
    'myFunc2 文档说明'
    print("test2")
    pass

myFunc1()
myFunc2()
