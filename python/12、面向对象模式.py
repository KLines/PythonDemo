

# 面向对象设计模式


print("===== 鸭子类型 =====")


class Payment(object):
    def pay(self):
        pass


class WeChat():
    def pay(self):
        print("微信支付")


class AliPay:
    def pay(self):
        print("支付宝支付")


class ApplePay:
    def pay(self):
        print("苹果支付")


def pay(obj):
    obj.pay()


pay(WeChat())
pay(AliPay())
pay(ApplePay())


print("===== 抽象类 =====")


from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        pass


class WeChat(Payment):
    def pay(self):
        print("微信支付")
        pass


wc = WeChat()
wc.pay()


print("===== Mixin模式 =====")


class Animal:

    def trait(self):
        print(self.name + "是一种动物")
        pass


class Manmal(Animal):

    def trait(self):
        print(self.name + "是一种哺乳动物")


class RunnableMixin:

    def run(self):
        print(self)
        print(self.name, "is running")  # 父类使用子类的属性


class Dog(Manmal, RunnableMixin):
    def __init__(self,name):
        self.name = name

# a = Animal()
# a.trait() # error

d = Dog("旺财")
d.trait()
d.run()
print(Dog.__bases__)
print(Dog.__mro__)