

# 面向对象基础


print("===== 类属性和实例属性 =====")


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
    def method_cls(cls):
        print(cls)
        print('类的类方法')
        print(cls.age)

    # 普通方法，对象调用
    def method_normal(self):
        print("类的普通方法")

    # 私有方法
    def __method_normal(self):
        pass

m = Classname('man','男')
w = Classname('woman','女')


'''
1、静态方法，不论任何情况.都是函数--function
2、类⽅法，不论任何情况,都是⽅法--method
3、实例方法，如果是实例访问就是⽅法，如果是类名访问就是函数
'''
from types import FunctionType,MethodType
print(type(Classname.func_static)==FunctionType)
print(type(Classname('test',0).func_static))
print(type(Classname.method_cls)==MethodType)
print(type(Classname('test',0).method_cls))
print(type(Classname.method_normal))
print(type(Classname('test',0).method_normal))


# 添加类属性
Classname.temp = "class-temp"
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
Classname.method_cls()
w.method_normal()

print(__name__)


print("===== suepr()使用 =====")


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


print("===== str和repr的区别 =====")


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

    def __del__(self):
        print("析构函数")


t = Test()

print(t)
t() # 对实例进行调用
print(t.score)
print(t.age())


print("====== @property属性使用 ======")


class Animal:

    def __init__(self,name=None):
        self.__name = name
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

a = Animal("test")
print(a.name)
a.name = "animal"
print(a.name)