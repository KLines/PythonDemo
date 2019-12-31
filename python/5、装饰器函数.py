
from functools import wraps


def func(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("装饰器")
        func(*args,**kwargs)
    return wrapper

print("======= 1、未使用@装饰 ========")
def origin():
    print("函数装饰器--被装饰的函数")
    pass
origin = func(origin) # 等价于 func(origin)()
origin()

print("======= 1、使用@装饰 ========")
@func # 等价于 demo = func(demo)
def demo():
    print("函数装饰器--被装饰的函数")
    pass
print(demo.__name__)
demo()



print("======= 2、带参数的装饰器 ========")

def logit(args):
    print(args)
    def logging(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(func.__name__+" was called")
            func(*args, **kwargs)
        return wrapper
    return logging

@logit("使用logit")
def test():
    print("函数装饰器--带参数的装饰器")
    pass
test()



print("======= 3、类装饰器 ========")

class Func(object):
    def __init__(self, args):
        self.args = args

    def __call__(self, func):
        print(self.args)
        def wrapper(*args, **kwargs):
            print("class start")
            print(args)
            func(*args, **kwargs)
            print("class end")
        return wrapper

@Func("class args")
def test(*args, **kwargs):
    print("函数装饰器--类装饰器")
    print(kwargs)
    pass

test("demo", 1, name="test", age=20)








print("======= 4、两个装饰器装饰一个函数 ========")

def func1(func): #将被装饰函数传入
    print("func1")
    def wrapper1(*args, **kwargs):
        print("wrapper1")
        func(*args, **kwargs)  #执行被装饰的函数
    return wrapper1  #将装饰完之后的函数返回（返回的是函数名）

def func2(func):
    print("func2")
    def wrapper2():
        print("wrapper2")
        func()
    return wrapper2

@func2
@func1
def test(): # 自下而上的顺序调用装饰器函数 f = func2(func1(f))
    print("函数装饰器--两个装饰器装饰一个函数")
    pass

print("name：", test.__name__)
test()







#  函数装饰器
if __name__ == "__main__":

    '函数装饰器 Demo'

    print("====入参 @funcA @funcB ：====")
    def funcA(A):  # 入参是函数
        print("funcA")

    def funcB(B):  # 入参是函数
        print(B(3))
        print("funcB")

    @funcA  # 等价于 funcA(funcB(func))
    @funcB
    def func(c):  # 作为入参传递，无法单独调用
        print("装饰器传参：func")
        return c ** 2

    print("====入参 @funcC ：====")
    def funcC(C):  # 入参是函数
        @wraps(C)  # 表示不改变入参函数，可以访问入参函数的属性
        def temp(x, *args):
            print("function is temp")
            print(temp.__name__)
            print(C(x, *args))
        return temp  # 返回内部函数，用于func在外部可以独立调用

    @funcC   # 使用@修饰函数后 func 变成 funcC 内部返回的函数对象 func = temp
    def func(x, *args):  # 等价于 funcC(func)(4, test", 2323)
        """ 使用函数修饰符"""
        print("function is func", args)
        return x**2

    print("name :", func.__name__)
    print("doc :", func.__doc__)
    func(4, "test", 2323)  # 修饰器下的函数可以独立调用

    print("====入参 @funcD() ：====")
    def funcD(): #
        print("function is funcD")
        def inner(func):
            print("function is inner")
            @wraps(func)
            def temp():
                func()  # 执行修饰器下的函数
            return temp
        return inner

    @funcD()  # 等价于  funcD()(func)()
    def func():
        print("function is func")

    func()

