

# 基础语法


print("===== 1、str list tuple dict 数据类型 的用法 =====")


String = "hello world"
print('str：' + String)
print(id(String))
String = 'test'
print(id(String))
# 有序，元素可以是可变对象
List = ['runoob', 786, "john", 'john', 70.2, ['test1', 'test2']]
print('修改前 list：', List)
print(id(List))
List[2] = 123
List.append(123456)
print(id(List))
print('修改后 list：', List[::])  # 返回所有值
print('反向取值 list：', List[::-1])  # 反向取值
# append() extend() insert() remove() pop() clear() copy()

# 元组不能二次赋值，有序，元素可以是可变对象
Tuple = ('tuple', 123, 'test', ['test1', 'test2'])
print('tuple：', Tuple)

# 无序，元素必须是不可变对象
Set = {'Tom', 'Mary', 'Tom', 'Jack', 'Rose'}
print('set：', Set)
# add() update() remove() discard() pop() clear() copy()

# 无序，key 值必须是不可变对象，赋值时可以重复，运行时去重
Dictionary = {'name': 'test', 'name': 'john', ('test2', 'test1'): 6734, 'dept': 'sales'}
# update() pop() clear() copy()s

print('dict：', Dictionary)
# print(Dictionary.get(tuple))  # 获取对应键的值
# print(Dictionary['name'])
# print(Dictionary.keys())  # 输出所有键
# print(Dictionary.values())  # 输出所有值
# print(Dictionary.items())  # 输出所有项
print("数据类型：", type(1.0), type(String), type(List), type(Tuple), type(Set), type(Dictionary))


print("===== 2、type isinstance 用法 =====")


class A:  # 空类
    pass  # pass是空语句，是为了保持程序结构的完整性，不做任何事情，一般用做占位语句。

class B(A):
    pass

# type() 不会认为子类是一种父类类型
# isinstance() 会认为子类是一种父类类型
# print(isinstance(String, (str, list)))  # 是元组中的一个返回 True
print("isinstance(A(), A)：", isinstance(A(), A))  # returns True
print("isinstance(B(), A)：", isinstance(B(), A))  # returns True
print("type(A()) == A：", type(A()) == A)  # returns True
print("type(B()) == A：", type(B()) == A)  # returns False


print("===== 3、and or not 的用法 =====")


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


print("===== 4、is 与 == 的区别 =====")


"== 与 is 的区别：is 与 == 区别，is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。"

a = [1, 2, 3]
b = a  # 引用同一个对象
print("前提条件：b = a ")
print("b is a：", b is a)  # true
print("b == a：", b == a)  # true
b = a[:]  # 给b重新赋值，重新开辟一块内存空间
print("前提条件：b = a[:]")
print(b is a)  # false
print(b == a)  # true

# （1）只要是变量的值相同，标识都相同，没有-5~256的限制
a = 100000000000000000000000000000000000000000000000
b = 100000000000000000000000000000000000000000000000
if a is b:
    print('a 和 b 标识相同，标识为：', id(a))
else:
    print('a 和 b 标识不相同，a 标识为：', id(a), 'b 标识为：', id(b))

# （2）同样的如果是负数，仍然没有上述限制：
a = -100000
b = -100000
if a is b:
    print('a 和 b 标识相同，标识为：', id(a))
else:
    print('a 和 b 标识不相同,a 标识为：', id(a), 'b 标识为：', id(b))

# （3）列表也是一样的，只要是列表项数值一样，那么标识也是一样的。例子如下：
list1 = [10000, 20000, 30000]
list2 = [10000, 12000, 15000]
if list1[0] is list2[0]:
    print('list1[0] 和 list2[0] 标识相同，标识为：', id(list1[0]))
else:
    print('list1[0] 和 list2[0] 标识不相同，list1[0]标识为：', id(list1[0]), 'list2[0]标识为：', id(list2[0]))

# （4）元组的标识是跟着变量名的，变量名不一样，标识也不一样，上例子：
tuple1 = (10000, 20000, 30000) # 两者id不同
tuple2 = (10000, 12000, 15000)
# tuple1 = ("test", 20000, 30000)  # 两者id相同
# tuple2 = ("test", 12000, 15000)
if tuple1[0] is tuple2[0]:
    print('tuple1[0] 和 tuple2[0] 标识相同，标识为：', id(tuple1[0]))
else:
    print('tuple1[0] 和 tuple2[0] 标识不相同，tuple1[0] 标识为：', id(tuple1[0]), '，tuple2[0]标识为：', id(tuple2[0]))

# （5）字典和列表是一样的，只要是列表项数值一样，那么标识也是一样的。例子如下：
dict1 = {1: 10000, 2: 20000, 3: 30000}
dict2 = {1: 10001, 2: 12000, 3: 15000}
if dict1[1] is dict2[1]:
    print('dict1[1] 和 tuple2[1] 标识相同，标识为：', id(dict1[1]))
else:
    print('dict1[1] 和 tuple2[1] 标识不相同，dict1[1] 标识为：', id(dict1[1]), '，tuple2[1] 标识为：', id(dict2[1]))

a =100000000
b =100000000
print(id(100000000))
print(id(a))
print(id(b))