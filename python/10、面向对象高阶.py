# 面向对象高阶
# __slots__ 详解 https://blog.csdn.net/sxingming/article/details/52892640

from types import MethodType

class Classname(object):  # 类对象

    age = 0

    def __init__(self, name):
        self.name = name

m = Classname('man')
w = Classname('womam')

print(dir(Classname)) # 获取一个对象的所有属性和方法

print("====== 绑定类属性和类方法 ======")

# 给class绑定类方法和类属性
def set_score(self, score):
    print(self)
    self.score = score  # 方法中的属性值实际是类属性

Classname.set_score = MethodType(set_score,Classname)
m.set_score(50)
print(Classname.score)
print(m.score)
print(w.score)
Classname.set_score(100)
print(Classname.score)
print(m.score)
print(w.score)


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


print("====== Classname 属性和方法 ======")

print(dir(Classname))
print(Classname.__dict__)  # 类的dict显示类的属性和方法

print("====== man 属性和方法 ======")

for k, v in m.__dict__.items():
        print(k, ':', v)

print(dir(m))
print(m.__dict__)  # 实例的dict只显示实例的属性，对于类的属性和方法是不保存的

print("====== woman 属性和方法 ======")

for k, v in vars(w).items():
        print(k, ':', v)

print(dir(w))
print(w.__dict__)



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



print("====== __slots__使用 ======")


class test_slots(object):
    __slots__= 'x','y'
    def printHello(self):
        print('hello!')

class test(object):
    def printHello(self):
        print('hello')

print(dir(test_slots))  # 可以看到test_slots类结构里面包含__slots__,x,y
print(dir(test))  # test类结构里包含__dict__
print(test_slots.__dict__)
print(test.__dict__)

print('**************************************')

ts=test_slots()
t=test()

print(dir(ts))  # 可以看到ts实例结构里面包含__slots__,x,y，不能任意绑定属性
print(dir(t))  # t实例结构里包含__dict__,可以任意绑定属性
# print(ts.__dict__) # error 定义了__slots__后，就不再有__dict__
print(t.__dict__)

print('**************************************')

class Person:

    __slots__ = ('name','phone','set_phone') # 限制类的实例能添加的属性或者方法

    def __init__(self,name):
        self.name = name

p = Person("person")

Person.temp = 'temp' # 类属性不受slots限制
print(p.temp)

# Person.name ='test' # 类变量与slots中的变量同名，则该变量被设置为readonly
# p.grade = 1 # error 类的实例只能拥有slots中定义的变量，不能再增加新的变量

# 给类的实例绑定方法时，不能添加__slots__限制之外的属性
def set_phone(self, phone):
    self.phone = phone

Person.set_phone = set_phone
p.set_phone(123)

print(p.name,":",p.phone)


# 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class Teacher(Person):
    pass

t = Teacher("teacher")
t.age = 20
t.set_phone(321)
print(t.name,":",t.age,":",t.phone)


# 父类和子类中都定义__slots__，子类允许定义的属性：子类__slots__+父类__slots__

class Student(Person):

    __slots__ = ('sex',)

    def __init__(self,name,sex):
        super().__init__(name)
        self.sex = sex

s = Student("student","男")
# s.age  = 10 error
s.set_phone(456)
print(s.name,":",s.sex,":",s.phone)


# 父类存在__dict__属性,则其子类将继承__dict__；此时，即使该子类包含了__slots__属性，该子类的实例依然可以任意添加

class A(object):
    pass

class B(A):
    __slots__=('x')

b = B()
b.x = 9
print('b.x=',b.x)
b.y = 8
print('b.y=',b.y)

