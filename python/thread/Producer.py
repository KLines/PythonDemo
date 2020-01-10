from threading import Thread
import threading

class Producer(Thread):

    def __init__(self,stu):
        super().__init__()
        self.stu = stu

    def run(self):
        while True:
            self.stu.set(threading.current_thread().name)
