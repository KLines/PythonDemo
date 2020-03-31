'''
变量作用域
UnboundLocalError和NameError错误根源解析
https://blog.csdn.net/weixin_34061555/article/details/93452652
'''


if __name__ == "__main__":

    print("===== 变量作用域类型 =====")


    b =int(3.3) # 内建作用域
    g = 4  # 全局变量
    def outer():
        e = 2  # 闭包函数外的函数中
        def inner():
            l = 1  # 局部变量
            print("局部作用域：",l)
            print("闭包函数外的函数中："+str(e))
            print("全局作用域：",g)
            print("内建作用域：", b)
        return inner  # 返回一个函数
    outer()()


    '''
    只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
    其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域，这些语句内定义的变量，外部也可以访问
    '''


    if True:
        msg = "test"
    print("if 中的变量：", msg)


    print("===== 修改作用域变量 =====")


    global_num = 10
    def func():
        global  global_num
        enclosing_num = 100  # 闭包函数外的函数中
        def inner():
            '修改作用域变量'
            global  global_num  # 需要使用 global 关键字声明
            nonlocal enclosing_num  # 需要使用 nonlocal 关键字声明
            global_num = 30
            enclosing_num = 200
        print(inner.__doc__)
        print("global_num 修改前：", global_num)
        print("enclosing_num 修改前：", enclosing_num)
        inner()
        print("enclosing_num 修改后：", enclosing_num)
    func()
    print("global_num 修改后：", global_num)


    '''
    在执行程序时的预编译能够在scope()中找到局部变量variable(对variable进行了赋值)。在局部作用域找到了变量名，所以不会升级到嵌套作用域去寻找。
    但是在使用print语句将变量variable打印时，局部变量variable并有没绑定到一个内存对象(没有定义和初始化，即没有赋值)。本质上还是Python调用变量
    时遵循的LEGB法则和Python解析器的编译原理，决定了这个错误的发生。所以，在调用一个变量之前，需要为该变量赋值(绑定一个内存对象)。
    
    注意：为什么在这个例子中触发的错误是UnboundLocalError而不是NameError：name ‘variable’ is not defined。因为变量variable不在全局作用域。
    Python中的模块代码在执行之前，并不会经过预编译，但是模块内的函数体代码在运行前会经过预编译，因此不管变量名的绑定发生在作用域的那个位置，都能被编译器知道
    '''


    variable = 300
    def scope():
        # print(variable) # variable是test_scopt()的局部变量，但是在打印时并没有绑定内存对象
        variable = 200 # 因为这里，所以variable就变为了局部变量
    scope()
    print(variable)