# 面向对象高阶

from types import MethodType

class Classname(object):  # 类对象

    def __init__(self, name):
        self.name = name

m = Classname('man')
w = Classname('womam')

print(dir(Classname))

print("====== 绑定类属性和类方法 ======")

# 给class绑定类方法和类属性
def set_score(self, score):
    print(self)
    self.score = score  # 方法中的属性值实际是类属性

Classname.set_score = MethodType(set_score,Classname)

Classname.set_score(50)
print(Classname.score)
print(m.score)
print(w.score)
m.set_score(100)
print(Classname.score)
print(m.score)
print(w.score)

print(dir(Classname))


print("====== 绑定实例属性和普通方法 ======")

# 给class绑定普通方法和实例属性
def set_sex(self, sex):
    print(self)
    self.sex = sex

Classname.set_sex = set_sex
# Classname.set_sex('男') # error
m.set_sex("男")
w.set_sex('女')
print(m.sex)
print(w.sex)


print("====== 单个实例绑定实例属性和普通方法 ======")

# 给单个实例绑定一个方法
def set_grade(self, grade):
    print(self)
    self.grade = grade

m.set_grade= MethodType(set_grade,m)

m.set_grade("grade") # 只属于 m 实例对象的特定方法，其他实例中不存在
print("实例方法-set_name：",m.grade) # grade
# w.set_name("test") # error

print(dir(Classname))
print(dir(m))
print(dir(w))

print("====== Classname 属性和方法 ======")

for k, v in vars(Classname).items():
        print(k, ':', v)

print("====== man 属性和方法 ======")

for k, v in vars(m).items():
        print(k, ':', v)

print("====== woman 属性和方法 ======")

for k, v in vars(w).items():
        print(k, ':', v)


print("====== @dataclass使用 ======")

from dataclasses import dataclass

@dataclass
class Data:
    name:str = "test"
    age:int = 21
    isFlag:bool = False
    value : float = 2.0

d = Data()
print(d)
