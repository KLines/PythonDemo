

'''
with as 语句

操作对象

    1、语句仅能工作于支持上下文管理协议（context management protocol）的对象
    2、同时包含 __enter__() 和 __exit__() 方法的对象就是上下文管理器
    3、目前支持该协议的对象有：
            file
            decimal.Context
            thread.LockType
            threading.Lock
            threading.RLock
            threading.Condition
            threading.Semaphore
            threading.BoundedSemaphore
    4、构建上下文管理器，常见的有 2 种方式：基于类实现和基于生成器实现

相关方法：

    1、__enter__(self)：进入上下文管理器自动调用的方法，该方法会在 with as 代码块执行之前执行。如果 with 语句
    有 as子句，那么该方法的返回值会被赋值给 as 子句后的变量
    2、__exit__（self, exc_type, exc_value, exc_traceback）：退出上下文管理器自动调用的方法。该方法会在
    with as 代码块执行之后执行。如果 with as 代码块成功执行结束，程序自动调用该方法，调用该方法的三个参数都为 None，
    如果 with as 代码块因为异常而中止，程序也自动调用该方法，使用 sys.exc_info 得到的异常信息将作为调用该方法的参数。
    3、当 with as 操作上下文管理器时，就会在执行语句体之前，先执行 __enter__()，然后再执行语句体，最后执行 __exit__()

'''


# 基于类的上下文管理器

class Sample:

    def __init__(self, error):
        self.error = error
        print("init")

    def __enter__(self):
        print("enter")
        return self

    def dosomething(self):
        print("dosomething")

    def __exit__(self, exc_type, exc_val, exc_tb):

        print("exit")
        print("exc_type:", exc_type)
        print("exc_val:", exc_val)
        print("exc_tb:", exc_tb)

        # 跳过一个异常，只需要返回该函数True即可
        if self.error == exc_type:
            print("test passed")
            return True
        else:
            print("test failed")
            return False


def get_sample(error, *args, **kwargs):
    if args:
        try:
            func = args[0]
            if len(args) != 1:
                func(*args[1:])
            elif kwargs:
                func(*kwargs.values())
            else:
                func()
        except BaseException as exc:

            if not error == type(exc):
                print("test failed")
                raise
            else:
                print("test passed")
    else:
        return Sample(error)


def test(a, b):
    return a / b


# 使用func测试
def test_func():
    get_sample(ZeroDivisionError, test, 3, 0)

    get_sample(ZeroDivisionError, test, a=3, b=0)

    get_sample(ZeroDivisionError, lambda: 3 / 0)


# 使用with测试

def test_with():
    with get_sample(ValueError):
        print("ValueError")
        raise ValueError

    try:
        with get_sample(ValueError) as sample:
            sample.dosomething()
            print("ZeroDivisionError")
            value = 3 / 0
    except:
        print("error")


test_func()
test_with()


# 基于生成器的上下文管理器

from contextlib import contextmanager

@contextmanager
def file_manager(name, mode):
    f = None
    try:
        f = open(name, mode)
        yield f  # yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始
    finally:
        if f is not None:
            f.close()

with file_manager('a.txt', 'w') as f:
    f.write('hello world')