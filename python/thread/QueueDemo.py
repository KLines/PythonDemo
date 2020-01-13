from collections import deque
from queue import Queue,LifoQueue,PriorityQueue


# Queue 先进先出队列

q = Queue(maxsize=0)  # maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉

q.put(1)
q.put(2)
q.put(3)

print(q.queue)

print(q.get())

print(q.queue)



# LifoQueue 后入先出队列

lq = LifoQueue(maxsize=4)

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