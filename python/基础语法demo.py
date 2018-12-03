print("=======str list tuple dict 数据类型 的用法========")
# a =1
# print(id(1))
# print(id(a))
String = "hello world"
List = ['runoob', 786, 2.23, 'john', 70.2]
# 元组不能二次赋值，相当于只读列表
Tuple = ('tuple', 123, 'test')
Dictionary = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print('string :' + String)
print('修改前 list : ', end="");print(List)
List[2] = 123
print('修改后 list : ', end="");print(List[:])
print('tuple : ', end="");print(Tuple)
print('dict : ', end="");print(Dictionary)
# print(Dictionary.get('name')) # 获取对应键的值
# print(Dictionary['code'])
print(Dictionary.keys())  # 输出所有键
print(Dictionary.values())  # 输出所有值

print("=======type isinstance 用法========")
class A:
    pass

class B(A):
    pass

# print(isinstance(Str,(str,int,list)) ) # 是元组中的一个返回 True
print("isinstance(A(), A) :", isinstance(A(), A))  # returns True
print("type(A()) == A :", type(A()) == A)  # returns True
print("isinstance(B(), A) :", isinstance(B(), A))  # returns True
print("type(B()) == A :", type(B()) == A)  # returns False

print("=======and or not 的用法========")
a = 10;b = 20
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
print("===== is 与 == 的区别========")
a = [1, 2, 3]
b = a  # 引用同一个对象
print(b is a)  # true
print(id(b) == id(a))  # true
print(b == a)  # true
b = a[:]  # 给b重新赋值，重新开辟一块内存空间
print(b is a)  # false
print(id(b) == id(a))  # false
print(b == a)  # true

print("======= if elif 条件语句 ========")
x = 0;y = 10
if x and y:
    print("test1")
elif x or y:
    print("test2")
else:
    print("test3")

print("======= 拷贝和引用的用法 ========")
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
print("源字典：",end="");print(dict1)
print("浅拷贝字典：",end="");print(dict2)
print("浅拷贝字典：",end="");print(dict3)
print("深拷贝字典：",end="");print(dict4)
# 修改动态数据类型，浅拷贝对应的数据发生改变，深拷贝的数据不发生改变
print('修改动态数据类型')
for i in range(5):
    dict3['a'][i] = 0
print("源字典：",end="");print(dict1)
print("浅拷贝字典：",end="");print(dict2)
print("浅拷贝字典：",end="");print(dict3)
print("深拷贝字典：",end="");print(dict4)
