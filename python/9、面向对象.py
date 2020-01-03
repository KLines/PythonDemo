# 面向对象

# 1、self与变量关系
# 2、_和__的使用场景
# 3、对象访问权限
# 4、类属性和实例属性

# "单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量
# "双下划线" ：私有成员，不能在类外通过类对象访问私有的类属性，只有在类内部才能访问
# https://blog.csdn.net/pfm685757/article/details/45918575

print("====== 类属性和实例属性 ======")

class Classname(object):  # 类对象

    age = 0  # 公有类属性
    __like = None  # 私有类属性

    def __init__(self,name,sex):
        self.name = name   # 公有实例属性
        self.__sex = sex  # 私有实例属性

    @staticmethod
    def func_static():      # 静态方法，可以没有参数
        print("类的静态方法")

    @classmethod
    def func_cls(cls):   # 类方法  cls 指向类对象
        print('类的类方法')

    def func_normal(self):  # 公有方法  self指向实例对象
        print("类的普通方法")

    def __func_normal(self):  # 私有方法
        pass


c = Classname('class','男')

# 通过实例更改类属性的值，不影响类访问类属性的值
c.age  = 20
print("实例属性-name：",c.name) # class
print("实例属性-age：",c.age) # 20
# print("实例属性-sex：",c.__sex) # error
# print("实例属性-name：",Classname.name) # error
print("类属性-age：",Classname.age) # 0

# 通过类更改类属性的值，不影响实例访问类属性的值
Classname.nage = 'temp'
Classname.age = 50
print("实例属性-name：",c.name) # class
print("实例属性-age：",c.age) # 20
print("类属性-age：",Classname.age) # 50

# 另外实例化一个对象,其值不是默认值,而是上次由类更改类属性后的值
c1 = Classname('temp','女')
print("实例属性-name：",c1.name) # temp
print("实例属性-age：",c1.age) # 50
print("类属性-age：",Classname.age) # 50

Classname.func_static()
Classname.func_cls()
c.func_normal()

print(__name__)

# ===========================================

class Person(object):

    # 类属性
    count=0
    name = 'Person'
    age = 0
    sex = '男'

    def __init__(self):
        Person.count+=1
        print("Person")
        pass

    def print_info(self):
        print(self)
        print(self.__class__)
        pass

    def __private(self):  # 私有方法
        print("__private")
        pass

    def speak(self):
        print("name:", self.name)
        print("age:", self.age)
        pass


# p = Person("Person",20)
# p.__private() # Error
# p._Person__private()

print("====== 单继承 ======")


# 单继承
class Student(Person):

    grade = 1

    def __init__(self, name, age, sex):
        # 显示调用父类构造函数
        super().__init__()
        Person.name = name
        Person.age = age
        self.sex = sex
        print("Student")
        pass

    def speak(self):
        super().speak()  # 调用父类方法
        print("sex:", self.sex)
        # 当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
        print("grade:", self.grade)
        pass


# 实例化类
s = Student("Student", 7, '男')
s.grade = 2
s.speak()
s.print_info()

temp = Student("temp", 77, '女')
temp.speak()

# super(Student, s).speak()  # 用子类对象调用父类已被覆盖的方法
# s.__private() # Error
# s._Student__private() # Error

print("====== 多继承 ======")


class Speaker():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Speaker")

    def speak(self):
        print("姓名 %s，年龄 %s" % (self.name, self.age))

# 多重继承
class Sample(Student, Speaker):
    name = "test"
    aget = 0

    def __init__(self, name, age,sex):
        # 调用父类构造函数
        # super(Sample,self).__init__(name,age)
        # Student.__init__(self,name,age)
        super().__init__(name, age, sex)
        Speaker.__init__(self, name, age)


s = Sample("Tim", 25,'女')
s.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

print("====== suepr()使用 ======")


class A:
    def __init__(self):
        print('enter A')
        super().__init__()
        print('leave A')

class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')

class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')

class D(C, B):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

D()


print("====== str和repr的区别 ======")

class Test():

    def __init__(self):
        self.prompt ="hello,zss041962"

    def __str__(self):
        return "str-->%s"%(self.prompt)

    def __repr__(self):
        return "repr-->%s"%(self.prompt)


t = Test()
print(t)


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
