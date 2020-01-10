from dataclasses import dataclass


# 面向对象特性


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


print("===== 单继承 =====")


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


print("===== 多继承 =====")


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


print("===== @dataclass使用 =====")


@dataclass
class Data:
    name:str = "test"
    age:int = 21
    isFlag:bool = False
    value : float = 2.0

d = Data()
print(d)