import types
from collections.abc import Iterable
from collections.abc import Iterator
from inspect import isgeneratorfunction


print("===== 1、iterator迭代器 =====")


list_iter = [1, 2, 3, 4]
print("list_iter 是否是iterator对象：", isinstance(list_iter, Iterator))  # false
print("list_iter 是否是iterable对象：", isinstance(list_iter, Iterable))  # true
it = iter(list_iter)  # 创建迭代器对象
print("it 是否是iterator对象：", isinstance(it, Iterator))  # true
print("it 是否是iterator对象：", isinstance(it, Iterable))  # true
for x in iter(it):
    print(x, end=" ")


print()


print("===== 2、generator生成器 =====")


# 生成器函数，使用了 yield 的函数被称为生成器（generator）
def createGenerator():
    for i in range(4):
        yield i * i

mygenerator = createGenerator()  # 调用函数时内部的代码并不立马执行，只是返回迭代器对象
print("生成器函数：", mygenerator)
print("mygenerator 是否是iterator对象：", isinstance(mygenerator, Iterator))  # true
for x in mygenerator:  # 在迭代时，createGenerator方法中的代码才会执行，节省内存
    print(x, end=" ")

print()
print("createGenerator() 是否是generator对象：", isinstance(mygenerator, types.GeneratorType))  # true
print("createGenerator 是否是generator函数：", isgeneratorfunction(createGenerator))  # true
print("createGenerator() 是否是iterator对象：", isinstance(mygenerator, Iterator))  # true
print("createGenerator() 是否是iterable对象：", isinstance(mygenerator, Iterable))  # true
print("range() 是否是iterator对象：", isinstance((x for x in range(10)), Iterator))  # true
