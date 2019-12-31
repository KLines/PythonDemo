print("======= 1、固定参数 ========")


def printinfo(name, age=20):
    "打印任何传入的字符串"
    print("名字：", name)
    print("年龄：", age)
    return

printinfo("test", 10) # 必须参数，根据参数顺序入参
printinfo(age=50, name="runoob")  # 关键字参数，可根据参数名匹配
printinfo("func")  # 使用默认参数，默认参数必须放在最后面


print("======= 2、可变参数 ========")


def printinfo(number, *args):  # 以元组(tuple)的形式导入
    print(number, args)

printinfo(1, "test", 3, 4)


def printinfo(number, **kwargs):  # 以字典(dict)的形式导入
    print(number, kwargs)

printinfo(1, name="test", age=20)  # key必须是字符串


def printinfo(*args, **kwargs):  # 以元祖、字典的形式导入
    print("入参为元祖&字典")
    print(args, kwargs)

printinfo("test", 3, 4, name="test", age=20)


def printinfo(a, b, *, c):  # 如果单独出现星号 * 后的参数必须用参数名传入
    return a + b + c

print(printinfo(1, 2, c=3))


print("======= 3、 lambda 表达匿名函数 ========")


count = lambda arg1, arg2: arg1 + arg2  # lambda 表达匿名函数
print("lambad", count(1, 2))


print("======= 4、函数参数可以是一个函数 ========")


def func1():
    print("func1()")

def excute(f):
    '函数也可以以一个函数为其参数'
    f()
    print("excute()")

excute(func1)
print(excute.__doc__)  # 通过 函数名.__doc__ 的方式来显示函数的说明文档


print("======= 5、在函数中定义函数 ========")


# 在函数中定义函数
def func2():
    print("func2()")

    def temp():
        print("temp2()")

    temp()

func2()


print("======= 6、从函数中返回函数 ========")


def func3():
    print("func3()")

    def temp():
        print("temp3()")

    return temp

f = func3()
f()


print("======= 7、函数引用传递 ========")


temp = excute
print("temp = excute")
temp(func1)  # 将函数赋值给一个变量，并调用
del excute  # 删除函数，其实就是删除引用，函数内容仍然存在
# excute(func) # 不能执行
print("del excute")
temp(func1)


print("======= 8、循环创建函数 ========")


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        # fs.append(f())
        fs.append(f)  # 创建函数，并添加到list中
    return fs

f = count()
print(f)
f1, f2, f3 = f
print(f1, f2, f3)
print(f1(), f2(), f3())  # 9,9,9 此时执行创建的函数，对应的循环变量已经变为最后一个值 i=3


print("======= 9、拷贝和引用的用法 ========")


# 直接赋值：其实就是对象的引用（别名）
# b = a: 赋值引用，a 和 b 都指向同一个对象
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象
# b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）
# 深拷贝(deepcopy)：copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象
# b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的

import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

