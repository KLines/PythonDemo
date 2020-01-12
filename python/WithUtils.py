
'''
with 实现原理
with后面的语句被求值后，返回对象的 __enter__() 方法被调用，这个方法的返回值将被赋值给as后面的变量。
当with后面的代码块全部被执行完之后，将调用前面返回对象的 __exit__()方法。
'''

class Sample:

    def __init__(self, error):
        self.error = error
        print("init")

    def __enter__(self):
        print("enter")

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

    with get_sample(ValueError):
        print("ZeroDivisionError")
        value = 3 / 0


test_func()
test_with()
