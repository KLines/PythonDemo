
print("======= 两个装饰器装饰一个函数 ========")


def set_fun1(func):
    print("set_fun1")

    def call_fun1(*args, **kwargs):
        return func(*args, **kwargs)

    return call_fun1


def set_fun2(func):
    print("set_fun2")

    def call_fun2(*args, **kwargs):
        return func(*args, **kwargs)

    return call_fun2


@set_fun1
@set_fun2
def test():
    print("函数装饰器--两个装饰器装饰一个函数")
    pass


print(test.__name__)
test()

print("======= 装饰器传参 ========")


def set_args(args):
    print(args)

    def set_fun(func):
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        return call_fun

    return set_fun


@set_args("函数装饰器--test")
def test():
    print("函数装饰器--装饰器传参")
    pass


print(test.__name__)
test()

print("======= 类装饰器 ========")


class Func(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func()


@Func  # test = Func(test)
def test():
    print("函数装饰器--类装饰器")
    pass


test()
