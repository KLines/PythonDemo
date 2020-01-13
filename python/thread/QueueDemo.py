from collections import deque
from queue import Queue,LifoQueue,PriorityQueue


'''
同步队列（Queue）

FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，优先级队列 PriorityQueue

Queue
    |--maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉
    |--qsize()	返回队列的当前大小
    |--empty()	如果队列为空，返回True，否则返回False
    |--full()	如果队列已满，返回True，否则返回False
    |--put(item, block=True, timeout=None)	将项放入队列
        １、block=True, timeout=None 在必要时阻塞，直到有空位可用，timeout 为阻止的时间，超时抛出Full异常
        ２、block=False 立即将item放入队列，队列已满引发Full异常
    |--put_nowait(item)	相当于put(item, False)
    |--get(block=True, timeout=None)  从队列中删除并返回一个项
        １、block=True, timeout=None 在必要时阻塞，直到有可用数据为止，timeout 为阻止的时间，超时抛出Empty异常
        ２、block=False 立即获取队列中的可用数据，否则抛出Empty异常
    |--get_nowait()	等价于get(False)
    |--task_done() 向已完成的队列任务发送一个信号
    |--join() 阻塞线程，直到队列为空才放行


'''




# Queue 先进先出队列

q = Queue(maxsize=0)  # maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉

q.put(1)
q.put(2)
q.put(3)

print(q.queue)

print(q.get(block=False,timeout=2)) # 队列中没有值时，线程阻塞状态

print(q.queue)



# LifoQueue 后入先出队列

lq = LifoQueue(maxsize=5)

lq.put(1)
lq.put(2)
lq.put(3)

print(lq.queue)

print(lq.get())

print(lq.queue)

print('队列总size：',lq.maxsize)
print('队列当前size：',lq.qsize())


# PriorityQueue 优先队列

pq = PriorityQueue(maxsize=0)

pq.put((9,'a'))  # 优先级设置数越小等级越高，按优先级取数据
pq.put((7,'c'))
pq.put((1,'d'))

print(pq.queue)

print(pq.get())

print(pq.queue)


# 双边队列

dq = deque(['a','b'])

dq.append('c')

dq.appendleft('d')

print(dq)