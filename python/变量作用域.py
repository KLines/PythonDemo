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
            print("内建作用域：",b)
        # inner()
        return inner #返回一个函数
    # outer()
    outer()() # 先执行外部函数，再执行内部函数


    '''
    只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
    其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域，这些语句内定义的变量，外部也可以访问
    '''
    if True:
        msg = "if"
    print("if 中的变量：",msg)

    num = 1
    print("修改全局变量：",num)
    def fun():
        global num  # 需要使用 global 关键字声明
        num = 2  # 修改 global 作用域变量
        print("inner :",num)
    fun()
    print("global :",num)

    outer_num = 10
    print("修改 enclosing 作用域变量：",outer_num)
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

    def changeme(mylist):
        mylist.append([1, 2, 3, 4])
        print("函数内取值: ", mylist)
    # 调用changeme函数
    mylist = [10, 20, 30]
    changeme(mylist)
    print("函数外取值: ", mylist)

    def changeme(mylist):
        mylist = [1, 2, 3, 4] # 重新开辟一块内存空间
        print("函数内取值: ", mylist)
    # 调用changeme函数
    mylist = [10, 20, 30]
    changeme(mylist)
    print("函数外取值: ", mylist)


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        # fs.append(f())
        fs.append(f) # 创建函数，并添加到list中
    return fs

f1, f2, f3 = count()
# print(f1,f2,f3)`
if __name__ == "__main__":
    print(f1(),f2(),f3()) # 9,9,9 此时执行创建的函数，对应的循环变量已经变为最后一个值 i=3

# 函数装饰器

def funcA(f):
    f(3)
    print("function A")

def funcB(f):
    def temp(c):
        print(f(c))
        print("function B")
    return temp



# @funcA
@funcB
def func(c): # 等价于 funcA(funcB(func))
    print("function C")
    return c**2
func(4)
# funcB(func)(4)

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration(): # 等价于 a_new_decorator(a_function_requiring_decoration)
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

