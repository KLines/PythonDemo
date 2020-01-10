

# 条件语句


print("===== 1、if elif 条件语句 =====")


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


print("===== 2、while 循环语句 =====")


def trim(args):
    while args[:1] == " ":
        args = args[1:]
    while args[-1:] == " ":
        args = args[:-1]
    return args


str = "  trim  "
print(trim(str))  # 去掉首尾重复空格


print("===== 3、for 循环语句 =====")


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):  # 顺序遍历
    print(i, end=" ")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

print()
for q, a in zip(questions, answers):  # 遍历多个序列
    print("what is your {0}? It is {1}".format(q, a))

for i in reversed(range(1, 10, 2)):  # 反向遍历
    print(i, end=" ")

print()
s = 'Python'
print("当前所有值：", end="")
for letter in 'Python':
    print(letter, end="")

print()
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


print("===== 4、switcher使用 =====")


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


if __name__ == '__main__':
    print("switcher普通字典映射：", end="")
    print((num(3)))
    print("switcher函数与lambda字典映射：", end="")
    print(num2Str(2))
    print(num2Str(3))
