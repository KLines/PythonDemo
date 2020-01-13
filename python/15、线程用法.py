from time import time,sleep
from thread.Student import *
from thread.Consumer import *
from thread.Producer import *
from queue import Queue, Empty

'''
多线程

创建方式：
    1、通过thread方法创建线程
    2、通过继承Thread类创建线程

线程同步：
    1、Lock锁--->处理资源共享问题
    2、Condition锁，wait()，notify()--->生产者消费者问题
    3、Semaphore信号量--->控制线程的并发数
    4、Event对象
    5、同步队列

多线程间通信：
    1、使用全局变量，需要加锁　　
    2、使用queue模块，可在线程间进行通信，并保证了线程安全

线程中断问题：
    1、退出标记
    2、使用ctypes强行杀掉线程
    
多线程使用问题：
    1、死锁问题
    2、生产者消费者问题
    3、获取线程任务执行结果
    4、多线程定时任务
    5、threadlocal
    6、线程池

Python的线程：
１、Python解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
２、GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
３、在Python中可以使用多线程，但不要指望能有效利用多核，不过可以通过多进程实现多核任务，多个Python进程有各自独立的GIL锁，互不影响。
'''


'创建线程任务'


def func():
    n = 0
    while n < 5:
        n = n + 1
        print("%s 线程运行---"%threading.current_thread().name)
        sleep(1)


class MyThread(Thread):

    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        n = 0
        while n < 5:
            n = n + 1
            print("%s 线程运行---"%threading.current_thread().name)
            sleep(1)
        self.num = n

    def result(self):
        return self.num


def create_thread():

    start = time()
    print("%s 线程运行---"%threading.current_thread().name)


    '===== 通过thread方法创建线程====='

    t1 = threading.Thread(target=func,name="thread-1")
    t1.start()
    t1.join()


    '===== 通过继承Thread类创建线程 ====='

    t2 = MyThread('mythread')
    t2.start()
    t2.join()
    print(t2.result())

    print("%s 线程结束---"%threading.current_thread().name)
    end = time()

    print("总共耗时%s秒"%(end-start))


'处理线程任务资源共享问题'


'===== 线程同步：Lock ====='


num = 0
lock = threading.Lock()

def func_lock():
    while True:
        try:
            lock.acquire()
            global num
            num = num + 1
            sleep(0.001)
            print("%s 线程运行---num = "%threading.current_thread().name,num)
        finally:
            lock.release()

def thread_lock():

    t1 = threading.Thread(target=func_lock,name="thread-1")
    t2 = threading.Thread(target=func_lock,name="thread-2")
    t1.start()
    t2.start()


'===== 线程同步：Condition ====='

thread_local = threading.local()

def thread_con():

    stu = Student(False)
    pro = Producer(stu)
    con = Consumer(stu)

    pro.start()
    con.start()


'===== 线程同步：Semaphore ====='


sem = threading.Semaphore(1)

def func_sem():
    while True:
        try:
          sem.acquire()
          global num
          num = num + 1
          print("%s 线程运行---num = "%threading.current_thread().name,num)
        finally:
            sem.release()

def thread_sem():

    t1 = threading.Thread(target=func_sem,name="thread-1")
    t2 = threading.Thread(target=func_sem,name="thread-2")
    t1.start()
    t2.start()


'===== 线程同步：Event ====='

'''
wait(timeout=None) 挂起线程timeout秒(None时间无限)，直到超时或收到event()信号开关为True时才唤醒程序。
set() Even状态值设为True
clear() Even状态值设为 False
is_set() 返回Even对象的状态值。
'''

event = threading.Event() # 默认False

def func_wait():
    print("%s 线程运行---num = " % threading.current_thread().name, "等待服务")
    event.wait()
    print("%s 线程运行---num = "%threading.current_thread().name,"连接服务")

def func_conn():
    print("%s 线程运行---num = " % threading.current_thread().name, "启动服务")
    event.set()

def thread_event():
    t1 = threading.Thread(target=func_wait,name="thread-1")
    t2 = threading.Thread(target=func_conn,name="thread-2")
    t1.start()
    t2.start()


'===== 线程同步：queue ====='

q = Queue(maxsize=10)
count = 0
conn = threading.Condition()

def producer(name):
    global count
    while True:
        try:
            conn.acquire()
            if not q.empty():
                conn.wait()
            count+=1
            q.put(count)
            sleep(0.1)
            print("%s 生产了--袜子%s"%(name,count))
            conn.notify()
        except:
            raise
        finally:
            conn.release()

def consumer(name):
    while True:
        try:
            conn.acquire()
            if q.empty():
                conn.wait()
            count = q.get(block=False)
            sleep(0.1)
            print("%s 卖掉了--袜子%s"%(name,count))
            conn.notify()
        except Empty:
            conn.notify()
        except:
            raise
        finally:
            conn.release()

def thread_queue():
    t1 = threading.Thread(target=producer,args = ("thread-1",))
    t2 = threading.Thread(target=consumer,args = ("thread-2",))
    t3 = threading.Thread(target=consumer,args = ("thread-3",))
    t1.start()
    t2.start()
    t3.start()
    print('---success---')





if __name__ == '__main__':

    # create_thread()
    # thread_lock()
    # thread_con()
    # thread_sem()
    # thread_event()
    thread_queue()





