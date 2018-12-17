# 变量作用域

if __name__ == "__main__":
    print("==== 变量作用域范围 ====")
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
        return inner  # 返回一个函数
    outer()()

    '''
    只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
    其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域，这些语句内定义的变量，外部也可以访问
    '''
    if True:
        msg = "if"
    print("if 中的变量：", msg)

    print("==== 变量作用域修改 ====")
    num = 1
    print("全局变量 num：", num)
    def fun():
        global num  # 需要使用 global 关键字声明
        num = 2  # 修改 global 作用域变量
    fun()
    print("修改全局变量后 num：", num)

    outer_num = 10
    print("全局变量 outer_num：", outer_num)
    def outer():
        # global  outer_num
        outer_num = 100  # 闭包函数外的函数中
        print("enclosing 作用域变量，outer_num修改前：", outer_num)
        def inner():
            'nonlocal 只能修改外层函数的变量而不能修改外层函数所引用的全局变量'
            nonlocal outer_num  # 需要使用 nonlocal 关键字声明
            outer_num = 200 # 修改 enclosing 作用域变量
            print(inner.__doc__)
        inner()
        print("enclosing 作用域变量，outer_num修改后：", outer_num)
    outer()
    print("全局变量 outer_num：", outer_num)


#  函数装饰器
from functools import wraps
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


