from threading import Thread
import threading,time


#　死锁问题

class MyThreadA(Thread):

    def run(self):
        if lock1.acquire():
            print("a---up")
            if lock2.acquire():
                print("a---down")
                lock2.release()
            lock1.release()

class MyThreadB(Thread):

    def run(self):
        if lock2.acquire():
            print("b---up")
            if lock1.acquire():
                print("b---down")
                lock1.release()
            lock2.release()


if __name__ == '__main__':

    lock1 = threading.Lock()
    lock2 = threading.Lock()

    a = MyThreadA()
    b = MyThreadB()

    a.start()
    b.start()