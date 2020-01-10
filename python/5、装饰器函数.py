from functools import wraps


'''
函数装饰器
https://blog.csdn.net/legend818/article/details/95165703
'''


# 程序只是简单的将定义代码块读入内存中
def func(func): # 闭包
    # 封装内部函数，防止被装饰的函数未进行调用的情况下，程序已经执行完毕
    def wrapper(*args,**kwargs):
        print("装饰器")
        func(*args,**kwargs)
    return wrapper


print("===== 1、装饰器函数-未使用@装饰 =====")


def origin():
    print("被装饰的函数")
    pass
origin = func(origin) # 等价于 func(origin)()
origin()


print("===== 1、装饰器函数-使用@装饰 =====")


# @func这句代码在程序执行到这里时会自动执行func函数内部的代码
@func # 等价于 demo = func(demo)
def demo(name, age):
    print("被装饰的函数")
    print(name, age)
    pass
print(demo.__name__)
demo("test", 21) #  只有调用了，才会执行


print("===== 2、装饰器函数-两个装饰器装饰一个函数 =====")


def func1(func):
    print("func1")
    def wrapper1(*args, **kwargs):
        print("认证成功")
        func(*args, **kwargs)
        print("打印日志")
    return wrapper1

def func2(func):
    print("func2")
    def wrapper2():
        print("一条欢迎信息")
        func()
        print("一条离开信息")
    return wrapper2

@func2 # test = func2(test)
@func1 # test = func1(test)
def test(): # 自下而上的顺序调用装饰器函数 f = func2(func1(f))
    print("两个装饰器装饰一个函数")
    pass

print("name：", test.__name__)
test()


print("===== 3、装饰器函数-一般参数 =====")


def logit(args):
    def logging(func):
        @wraps(func)
        def wrapper():
            print(args)
            print(func.__name__+" was called")
            func()
        return wrapper
    return logging

@logit("使用logit")
def test():
    print("函数装饰器--带参数的装饰器")
    pass
test()


print("===== 4、装饰器函数-函数名参数 =====")


def outh():
    print("认证成功")

def log():
    print("添加日志")

# 装饰器函数。接收两个参数，这两个参数是某个函数的名字
def filter(func_outh,func_log):
    # 第一层封装，test函数实际上被传递给了func这个参数
    def logging(func):
        # 第二层封装，auth和log函数的参数值被传递到了这里
        def wrapper(*args,**kwargs):
            func_outh()
            func(*args,**kwargs)
            func_log()
        return wrapper
    return logging

# 其实这里 filter(auth,log) = logging , @filter(auth,log) = @logging
@filter(outh,log)
def test():
    print("装饰器函数--参数是函数的装饰器")
    pass
test()


print("===== 5、类装饰器-不带参数 =====")


class Func1():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("class start")
        self.func(*args, **kwargs)
        print("class end")

@Func1
def test(*args, **kwargs):
    print(args)
    print("函数装饰器--类作为装饰器使用")
    print(kwargs)
    pass

test("demo", 1, name="test", age=20)



print("===== 6、类装饰器-带参数 =====")

class Func2(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        print(self.kwargs)

    def __call__(self,func):
        print(self.kwargs)
        def wrapper(*args, **kwargs):
            print("class start")
            print(args)
            func(*args, **kwargs)
            print("class end")
        return wrapper

# 装饰器的参数从 __init__ 函数中传
@Func2(args="class args")
def test(*args, **kwargs):
    print("函数装饰器--类作为装饰器使用")
    print(kwargs)
    pass

# 函数的参数从 __call__ 函数中传
test("demo", 1, name="test", age=20)


if __name__ == '__main__':

    # 单例模式1
    def singleton(obj):
        instance = {}
        def wrapper(*args, **kwargs):
            if obj not in instance:
                instance[obj] = obj(*args,**kwargs)
            return instance[obj]
        return wrapper

    @singleton
    class Person(object): # Person = singleton(Person)
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def printInfo(self):
            print(self.args)


    test1 = Person("test1",12)
    test2 = Person("test2",13)
    test1.printInfo()
    test2.printInfo()
    print(id(test1),id(test1))


    # 单例模式2
    def cls(obj):
        def wrapper(*args, **kwargs):
            if not obj.instance:
                obj.instance = obj(*args, **kwargs)
            return obj.instance
        return wrapper

    @cls
    class Demo(object):

        instance = None

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def printInfo(self):
            print(self.args)


    zs = Demo("zs",12)
    ls = Demo("ls",32)
    zs.printInfo()
    ls.printInfo()
    print(id(zs),id(ls))