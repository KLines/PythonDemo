import threading


'''
１、线程同步问题
    name: test0 ,age: 1
    name: test1 ,age: 0
２、生产者消费者问题
    name: test0 ,age: 0
    name: test0 ,age: 0
    name: test0 ,age: 1
    name: test1 ,age: 1
'''


con = threading.Condition()
num = 0

class Student(object):

    def __init__(self,flag=False):
        super().__init__()
        self.flag = flag
        self.age = 0
        self.name = ""


    def set(self,name):
        global num
        con.acquire()
        try:
            if self.flag:
                con.wait()
            if num % 2 ==0:
                self.age = 0
                self.name = "test0"
            else:
                self.age = 1
                self.name = "test1"
            num = num +1
            print("%s 线程运行---设置学生信息"%name)
            self.flag =  True
            con.notify()
        finally:
            con.release()


    def get(self,name):
        con.acquire()
        try:
            if not self.flag:
                con.wait()
            print("%s 线程运行---name:%s,age:%s"%(name,self.name,self.age))
            self.flag =  False
            con.notify()
        finally:
            con.release()

