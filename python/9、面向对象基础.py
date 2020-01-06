# 面向对象基础

print("====== 类属性和实例属性 ======")

class Classname(object):  # 类对象

    age = 0  # 公有类属性
    __like = None  # 私有类属性，解释器对外把__like改成了_Classname__like

    def __init__(self, name, sex):
        super(Classname,self).__init__()
        self.name = name   # 公有实例属性
        self.__sex = sex  # 私有实例属性

    # 静态方法，对象和类调用，可以没有参数
    @staticmethod
    def func_static():
        print("类的静态方法")

    # 类方法，对象和类调用，cls 指向类对象
    @classmethod
    def func_cls(cls):
        print('类的类方法')
        print(cls.age)

    # 普通方法，对象调用
    def func_normal(self):
        print("类的普通方法")

    # 私有方法
    def __func_normal(self):
        pass

m = Classname('man','男')
w = Classname('woman','女')


# 添加类属性
Classname.temp = "temp"
print("类属性-temp：",Classname.temp) # class-temp
m.temp = "m-temp"
print("类属性-temp：",m.temp) # m-temp
print("类属性-temp：",w.temp) # class-temp


# 添加实例属性
m.grade = 'grade'
# print("实例属性-grade：",Classname.grade) # error
print("实例属性-grade：",m.grade) # grade
# print("实例属性-temp：",w.grade) # error


# 访问实例属性
# print("实例属性-name：",Classname.name) # error
print("实例属性-name：",m.name) # man
print("实例属性-name：",w.name) # woman


# 通过实例更改类属性的值，不影响类访问类属性的值
m.age = 20
print("类属性-age：",Classname.age)  # 0
print("类属性-age：",m.age) # 20
print("类属性-age：",w.age) # 0


# 通过类更改类属性的值，不影响实例访问类属性的值
Classname.age = 50
print("类属性-age：",Classname.age)  # 50
print("类属性-age：",m.age) # 20
print("类属性-age：",w.age) # 50


# 通过另一个实例更改类属性的值，不影响类访问类属性的值和之前实例的值
w.age = 30
print("类属性-age：",Classname.age)  # 50
print("类属性-age：",m.age) # 20
print("类属性-age：",w.age) # 30

# 调用方法
Classname.func_static()
Classname.func_cls()
w.func_normal()

print(__name__)

# ===========================================

class Person(object):

    # 类属性
    count=0
    sex = '男'

    def __init__(self,name,age):
        Person.count += 1
        self.__name = name
        self.__age = age
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
        print("name:", self.__name)
        print("age:", self.__age)
        pass


# p = Person('person','10')
# p.__private() # Error
# p._Person__private()


print("====== 单继承 ======")

# 单继承
class Student(Person):

    grade = 1 # 类属性

    def __init__(self, name, age, sex):
        super().__init__(name,age) # 显示调用父类构造函数
        self.sex = sex
        print("Student")
        pass

    def speak(self):
        super().speak()  # 调用父类方法
        # 当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
        print("sex:", self.sex)
        print("grade:", self.grade)
        pass


# 实例化类
s = Student("student", 7, '男')
s.grade = 2
s.speak()
s.print_info()

temp = Student("temp", 6, '女')
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

    def lecture(self):
        print("lecture")

# 多重继承
class Sample(Student, Speaker):

    name = "test"
    aget = 0

    def __init__(self, name, age,sex):
        # 调用父类构造函数
        # super(Sample,self).__init__(name,age)
        # super().__init__(name, age, sex)
        Student.__init__(self,name, age, sex)
        Speaker.__init__(self, name, age)
        print("Sample")


s = Sample("Tim", 25,'女')
s.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
s.lecture()
print(Sample.__bases__) # 查询继承的基类
print(Sample.__mro__) # 查询类的调用顺序


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

    def __getattr__(self, attr): # 自定义属性
        if attr == "score":
            return 99
        elif attr == "age":
            return lambda : 20
        else:
            return None

    def __call__(self, *args, **kwargs):
        print("call-->",self.prompt)


t = Test()

print(t)
t() # 对实例进行调用
print(t.score)
print(t.age())

print(callable(t))
print(callable(Test()))
print(callable(Test)) # True
