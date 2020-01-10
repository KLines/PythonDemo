# 多线程、多进程和异步I/O

import threading,time

def func():
    n = 0
    while n < 5:
        n = n + 1
        print("%s 线程运行---"%threading.current_thread().name)
        time.sleep(1)


print("%s 线程运行---"%threading.current_thread().name)


t = threading.Thread(target=func,name="thread-1")

t.start()
t.join()

print("%s 线程结束---"%threading.current_thread().name)

