print("======= 1、str list tuple dict 数据类型 的用法 ========")
String, str = "hello world", "test"
List = ['runoob', 786, "john", 'john', 70.2, ['test1', 'test2']]  # 有序，元素可以是可变对象
# 元组不能二次赋值，相当于只读列表
Tuple = ('tuple', 123, 'test', ['test1', 'test2'])  # 有序，元素可以是可变对象
tuple = ('test1', 'test2')
Set = {'Tom', 'Mary', 'Tom', 'Jack', 'Rose', tuple}  # 无序，元素必须是不可变对象
Dictionary = {'name': 'test', 'name': 'john', tuple: 6734, 'dept': 'sales'}  # 无序，key 值必须是不可变对象，赋值时可以重复，运行时去重
print('str : ' + String)
print('str : ' + str)
print('修改前 list : ', end="")
print(List)
List[2] = 123
print('修改后 list : ', end="")
print(List[::])  # 返回所有值
print('反向取值 list : ', end="")
print(List[::-1])  # 反向取值
print('tuple : ', end="")
print(Tuple)
print('set : ', end="")
print(Set)
print('dict : ', end="")
print(Dictionary)
# print(Dictionary.get(tuple))  # 获取对应键的值
# print(Dictionary['tuple'])
print(Dictionary.keys())  # 输出所有键
print(Dictionary.values())  # 输出所有值
print(Dictionary.items())  # 输出所有项
print("数据类型：", type(1.0), type(String), type(List), type(Tuple), type(Set), type(Dictionary))

print("======= 2、type isinstance 用法 ========")


class A:  # 空类
    pass  # pass是空语句，是为了保持程序结构的完整性，不做任何事情，一般用做占位语句。


class B(A):
    pass


# print(isinstance(Str,(str,int,list)) ) # 是元组中的一个返回 True
print("isinstance(A(), A) :", isinstance(A(), A))  # returns True
print("type(A()) == A :", type(A()) == A)  # returns True
print("isinstance(B(), A) :", isinstance(B(), A))  # returns True
print("type(B()) == A :", type(B()) == A)  # returns False

print("======= 3、and or not 的用法 ========")
a = 10
b = 20
print("a=10,b=20")
print("and ：如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值")
print("a and b :", a and b)
print("or ：如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值")
print("a or b :", a or b)
print("not(x) ：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True")
print("not (a and b) :", not (a and b))
# 修改变量 a 的值
print("====修改 a=0")
a = 0  # 数字类型是不可变数据类型，重新开辟一块内存，把新地址与变量名绑定，并非改变原空间内的值
print("a and b :", a and b)
print("a or b :", a or b)
print("not (a and b) :", not (a and b))
print("====修改 a=False")
a = False
print("a and b :", a and b)
print("a or b :", a or b)
print("not (a and b) :", not (a and b))

"== 与 is 的区别：is 与 == 区别，is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。"
print("===== 4、is 与 == 的区别 ========")
a = [1, 2, 3]
b = a  # 引用同一个对象
print("前提条件：b = a ")
print("b is a:", b is a)  # true
print("b == a:", b == a)  # true
b = a[:]  # 给b重新赋值，重新开辟一块内存空间
print("前提条件：b = a[:]")
print(b is a)  # false
print(b == a)  # true

print("======= 5、拷贝和引用的用法 ========")
import copy

dict1 = {'a': [8, 2, 3, 4, 5], 'b': 4}
dict2 = dict.copy(dict1)  # 浅拷贝
dict3 = copy.copy(dict1)  # 浅拷贝
dict4 = copy.deepcopy(dict1)  # 深拷贝
# 修改 静态数据类型，各自对应字典value值改变，不影响其他的字典变量
print('修改静态数据类型')
x = dict1['b']
x += 4
dict2['b'] = 5
dict3['b'] = 6
dict4['b'] = 7
print("源字典：", end="")
print(dict1)
print("浅拷贝字典：", end="")
print(dict2)
print("浅拷贝字典：", end="")
print(dict3)
print("深拷贝字典：", end="")
print(dict4)
# 修改动态数据类型，浅拷贝对应的数据发生改变，深拷贝的数据不发生改变
print('修改动态数据类型')
for i in range(5):
    dict2['a'][i] = 0
print("源字典：", end="")
print(dict1)
print("浅拷贝字典：", end="")
print(dict2)
print("浅拷贝字典：", end="")
print(dict3)
print("深拷贝字典：", end="")
print(dict4)

print("======= 6、if elif 条件语句 ========")
x = 0
y = 10
if (x > 0) and (y / x > 2):  # 采用短路规则
    print("test1")
elif x or y:
    print("test2")
else:
    print("test3")

x = [1, 2, 3]
print(x) if len(x) != 0 else ""


def num(arg):  # switcher使用
    switcher = {
        0: 1,
        1: "1",
        2: "2"
    }
    return switcher.get(arg, "nothing")  # 无匹配时，返回置默认值


def zero():
    return "zero()"


def one():
    return "one()"


def two():
    return "two()"


def num2Str(arg):
    switcher = {
        0: zero,  # 对应函数名
        1: one,
        2: two,
        3: lambda: "three()"  # lambda 来创建匿名函数
    }
    # func=switcher.get(arg,lambda:"nothing") # 返回函数名
    # return func()
    return switcher.get(arg, lambda: "nothing")()  # 返回对应函数


if __name__ == '__main__':  #
    print("switcher普通字典映射：", end="")
    print((num(3)))
    print("switcher函数与lambda字典映射：", end="")
    print(num2Str(2))

print("======= 7、while 循环语句 ========")


def trim(args):
    while args[:1] == " ":
        args = args[1:]
    while args[-1:] == " ":
        args = args[:-1]
    return args


str = "  trim  "
print(trim(str))  # 去掉首尾重复空格

print("======= 8、for 循环语句 ========")
s = 'Python'
print("当前所有值：", end="")
for letter in 'Python':
    print(letter, end="")
print("")

print("偶数索引值：", end="")
for index in range(0, len(s), 2):  # 索引值+2
    print(s[index], end="")
print("")

print("当前水果：", end="")
fruits = ['banana', 'apple', 'mango']
for index, item in enumerate(fruits):  # 打印索引以及对应值
    # if ('apple' == fruits[index]):
    #     print(fruits[index], end="")
    # continue
    if index == len(fruits) - 1:
        print(fruits[index])
    else:
        print(fruits[index] + ",", end="")
else:
    print("当前水果：无")  # 在循环条件为 false 时执行 else 语句块

print("======= 9、iterator迭代器，generator生成器 ========")
import types
from inspect import isgeneratorfunction
from collections.abc import Iterable
from collections.abc import Iterator

list_iter = [1, 2, 3, 4]
print("list_iter 是否是iterator对象 : ", isinstance(list_iter, Iterator))  # false
print("list_iter 是否是iterable对象 : ", isinstance(list_iter, Iterable))  # true
print("迭代器：", next(iter(list_iter)))  # 创建迭代器对象
# for x in iter(list_iter):
#     print(x)

# 生成器表达式
generator = (x for x in ("abcde"))
print("生成器表达式：", generator)
print(next(generator))


# 生成器函数
def createGenerator():
    list_generator = range(3)
    for i in list_generator:
        yield i * i


mygenerator = createGenerator()  # 调用函数时内部的代码并不立马执行，只是返回迭代器对象
print("生成器函数：", mygenerator)
print(next(mygenerator))  # 在迭代时，createGenerator方法中的代码才会执行，节省内存
# for x in mygenerator:
#     print(x)

print("createGenerator 是否是generator函数 : ", isgeneratorfunction(createGenerator))  # true
print("createGenerator() 是否是generator函数 : ", isgeneratorfunction(createGenerator()))  # false
print("createGenerator 是否是generator对象 : ", isinstance(createGenerator, types.GeneratorType))  # false
print("createGenerator() 是否是generator对象 : ", isinstance(createGenerator(), types.GeneratorType))  # true
print("createGenerator 是否是iterator对象 : ", isinstance(createGenerator, Iterator))  # false
print("createGenerator() 是否是iterator对象 : ", isinstance(createGenerator(), Iterator))  # true
print("createGenerator 是否是iterable对象 : ", isinstance(createGenerator, Iterable))  # false
print("createGenerator() 是否是iterable对象 : ", isinstance(createGenerator(), Iterable))  # true
print("range() 是否是iterator对象 : ", isinstance((x for x in range(10)), Iterator))  # true

print("======= 10、函数的使用 ========")

print("======= 固定参数 ========")


def printinfo(name, age=20):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo("test", 10)
printinfo(age=50, name="runoob")  # 可根据参数名匹配
printinfo("func")  # 使用默认参数

print("======= 可变参数 ========")


def printinfo(number, *args):  # 以元组(tuple)的形式导入
    print(number)
    print(args)


printinfo(1, "test", 3, 4)


def printinfo(number, **kwargs):  # 以字典(dict)的形式导入
    print(number)
    print(kwargs)


printinfo(1, name="test", age=20)  # key必须是字符串


def printinfo(a, b, *, c):  # 如果单独出现星号 * 后的参数必须用参数名传入
    return a + b + c


print(printinfo(1, 2, c=3))

count = lambda arg1, arg2: arg1 + arg2  # lambda 表达匿名函数
print(count(1, 2))
