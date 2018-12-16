# 变量作用域

if __name__ == "__main__":
    b =int(3.3) # 内建作用域
    g = 1  # 全局变量
    def outer():
        outer_num = 1  # 闭包函数外的函数中
        print("外部函数")
        def inner():
            inner_num = 1  # 局部变量
            print("内部函数")
            print("内建作用域：", b)
        # inner()
        return inner #返回一个函数
    outer()()

    '''
    只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
    其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域，这些语句内定义的变量，外部也可以访问
    '''
    if True:
        msg = "if"
    print("if 中的变量：", msg)

    num = 1
    print("修改全局变量：", num)
    def fun():
        global num  # 需要使用 global 关键字声明
        num = 2  # 修改 global 作用域变量
        print("inner :", num)
    fun()
    print("global :", num)

    outer_num = 10
    print("修改 enclosing 作用域变量：", outer_num)
    def outer():
        # global  outer_num
        outer_num = 100  # 闭包函数外的函数中
        def inner():
            'nonlocal 只能修改外层函数的变量而不能修改外层函数所引用的全局变量'
            nonlocal outer_num  # 需要使用 nonlocal 关键字声明
            outer_num = 200 # 修改 enclosing 作用域变量
            print("inner : ", outer_num)
            print(inner.__doc__)
        inner()
        print("outer : ", outer_num)
    outer()
    print("global : ", outer_num)



#  函数装饰器
from functools import wraps
if __name__ == "__main__":

    print("@funcA @funcB ：")

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
    print("@funcC ：")


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

    print("@funcD ：")

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

    def set_fun1(func):
        print("set_fun1")
        def call_fun1(*args,**kwargs):
            return func(*args,**kwargs)
        return call_fun1

    def set_fun2(func):
        print("set_fun2")
        def call_fun2(*args,**kwargs):
            return func(*args,**kwargs)
        return call_fun2

    @set_fun1
    @set_fun2
    def test():
        print("两个装饰器装饰一个函数")
        pass
    print(test.__name__)
    test()

    def set_args(args):
        print(args)
        def set_fun(func):
            def call_fun(*args,**kwargs):
                return func(*args,**kwargs)
            return call_fun
        return set_fun

    @set_args("test")
    def test():
        print("装饰器传参")
        pass
    test()


    class Funcc(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            self.func()


    @Funcc  # test = Funcc(test)
    def test():
        print("类装饰器")
        pass

    test()
