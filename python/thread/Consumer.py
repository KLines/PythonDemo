from threading import Thread
import threading

class Consumer(Thread):

    def __init__(self,stu):
        super().__init__()
        self.stu = stu

    def run(self):
        while True:
            self.stu.get(threading.current_thread().name)
