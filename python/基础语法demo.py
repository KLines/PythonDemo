print("======= 1、str list tuple dict 数据类型 的用法 ========")
# a =100000000
# b =100000000
# print(id(100000000))
# print(id(a))
# print(id(b))
String, str = "hello world", "test"
List = ['runoob', 786, "john", 'john', 70.2, ['test1', 'test2']]  # 元素可以是可变对象
# 元组不能二次赋值，相当于只读列表
Tuple = ('tuple', 123, 'test', ['test1', 'test2'])  # 元素可以是可变对象
tuple = ('test1', 'test2')
Set = {'Tom', 'Mary', 'Tom', 'Jack', 'Rose', tuple}  # 元素必须是不可变对象
Dictionary = {'name':'test','name': 'john', tuple: 6734, 'dept': 'sales'}  # key值必须是不可变对象
print('str : ' + String)
print('str : ' + str)
print('修改前 list : ', end="")
print(List)
List[2] = 123
print('修改后 list : ', end="")
print(List[::2])  # step 为 2
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
print(Dictionary.items())
print("数据类型：", type(1.0), type(String), type(List), type(Tuple), type(Set), type(Dictionary))

# 产生随机数
L = ['b', 'a', 'c']
L = list(set(L))
print(L)


# 可变参数
def test(*args):
    print(args)
    return args


print(type(test(1, 2, 3, 4)))  # 可以看见其函数的返回值是一个元组

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
print(b is a)  # true
print(id(b) == id(a))  # true
print(b == a)  # true
b = a[:]  # 给b重新赋值，重新开辟一块内存空间
print(b is a)  # false
print(id(b) == id(a))  # false
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

a = [1, 2, 3]
b = a if len(a) != 0 else ""
print(b)

print("使用 switcher 字典映射：")


def zero():  # 方法
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
        3: lambda: "three()"
    }
    # func=switcher.get(arg,lambda:"nothing")
    # return func()
    return switcher.get(arg, lambda: "nothing")()  # 返回对应函数


def num(arg):
    switcher = {
        0: 1,
        1: "1",
        2: "2"
    }
    return switcher.get(arg, "nothing")


if __name__ == '__main__':  #
    print("普通字典映射：", end="")
    print((num(3)))
    print("函数与lambda字典映射：", end="")
    print(num2Str(2))

print("======= 7、while 循环语句 ========")


def trim(args):
    while args[:1] == " ":
        args = args[1:]
    while args[-1:] == " ":
        args = args[:-1]
    return args


str = "  trim  "
print(trim(str))

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
    print("当前水果：无")

print(range(1, 3))  # 返回的是一个对象，并没有将数据完全实例化，所以内存中只有一个对象的空间
print(list(range(1, 3)))
print(type(list()))
