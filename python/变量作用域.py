# 变量作用域

Global = 1  # 全局变量


def outer():
    outer_num = 1  # 闭包函数外的函数中

    def inner():
        inner_num = 1  # 局部变量


'''
只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域，这些语句内定义的变量，外部也可以访问
'''
if True:
    msg = "变量"

print(msg)

num = 1


def fun():
    global num  # 需要使用 global 关键字声明
    num = 2  # 修改全局变量

fun()
print(num)


def outer():
    outer_num = 100  # 闭包函数外的函数中

    def inner():
        nonlocal outer_num  # 局部变量
        outer_num = 200

    inner()
    print(outer_num)
outer()
