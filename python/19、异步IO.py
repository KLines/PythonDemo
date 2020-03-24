import datetime,threading
import asyncio

'''

同步IO：
        
    CPU的速度远远快于磁盘、网络等IO。在一个线程中，CPU执行代码的速度极快，如果遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作，
    这种情况称为同步IO。在IO操作的过程中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了。

    解决办法：
        1、多线程、多进程模型，缺点：1、不能无上限增加进程、线程数量  2、系统需要不停地切换线程，导致性能下降
        2、异步IO
    
    
异步IO：
    
    当代码需要执行一个耗时的IO操作时，只需要发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理，这种情况称为异步IO。
    
    异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：
        loop = get_event_loop()
        while True:
            event = loop.get_event()
            process_event(event)
    在消息模型中，处理一个消息必须非常迅速，否则，主线程将无法及时处理消息队列中的其他消息，导致程序看上去停止响应


协程（Coroutine）：

    又称微线程，是单线程下的并发，协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。协程不是进程也不是线程，而是一个特殊的函数，
    这个函数可以在某个地方挂起，并且可以重新在挂起处外继续运行。
    
    特点：
        1、是一个线程执行，不需要创建多线程
        2、执行效率高，因为子程序（函数）切换不是线程切换，而是由程序自身控制，因此没有线程切换的开销
        3、不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态
    
    使用方法：
        多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
        
        
asyncio模块：

    运行协程函数的方式：
        1、loop.run_until_complete()
        2、asyncio.gather()---asyncio.run()
        3、asyncio.create_task()---asyncio.run()
        
    关键字：
        event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数
        coroutine 协程：协程对象，使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
        task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
        future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
        async/await：async定义一个协程，await用于挂起阻塞的异步调用接口，等待调用。
        sleep:暂停执行此任务，为事件循环分配要竞争的任务，并且它（事件循环）监视其所有任务的状态并从一个任务切换到另一个，这里是模拟io任务花费的时间。

'''


'协程函数'

def consumer():
    r = ''
    while True:
        n = yield r # 每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行
        if not n:
            return
        print('consumer --> %s'%n)
        r = 'OK'

def producer(c):
    c.send(None) # 启动生成器
    n = 0
    while n<5:
        n+=1
        print('producer --> %s'%n)
        r = c.send(n)  # yield不但可以返回一个值，它还可以接收调用者发出的参数
        print('producer --> %s'%r)

    c.close()


c = consumer()

producer(c)


'异步IO'

# 1、使用async关键字定义一个协程函数

async def func():
    print('%s %s --> write'%(datetime.datetime.now(),threading.current_thread().getName()))
    await asyncio.sleep(1)
    print('%s %s --> read'%(datetime.datetime.now(),threading.current_thread().getName()))

# 2、返回一个事件循环对象，是asyncio.Baseeventloop的实例
# loop = asyncio.get_event_loop()

# 3、将协程函数加入到事件循环loop，并启动事件循环
# loop.run_until_complete(func())
# loop.close()


'asyncio--运行协程函数的第一种方式'

async def test1():
    print('%s %s --> write1'%(datetime.datetime.now(),threading.current_thread().getName()))
    await asyncio.sleep(3)
    print('%s %s --> read1'%(datetime.datetime.now(),threading.current_thread().getName()))
    return 'test1'

async def test2():
    print('%s %s --> write2'%(datetime.datetime.now(),threading.current_thread().getName()))
    await asyncio.sleep(2)
    print('%s %s --> read2'%(datetime.datetime.now(),threading.current_thread().getName()))
    return 'test2'


'asyncio--运行协程函数的第二种方式'

async def main():
    # 同时将两个异步函数对象加入事件循环，但并不运行等待调用，底层会自动创建异步事件循环
    res = await asyncio.gather(test1(),test2())
    print(res)


'asyncio--运行协程函数的第三种方式'

async def say_after(delay,msg):
    await asyncio.sleep(delay)
    print('%s --> %s'%(datetime.datetime.now(),msg))

async def task():

    # 创建任务事件，异步函数加入参数，底层自动创建了事件循环loop
    task1 = asyncio.create_task(say_after(3,'hello'))
    task2 = asyncio.create_task(say_after(2,'world'))

    print('%s --> start'%datetime.datetime.now())
    await task1  # 将任务事件加入异步事件循环，等待调用
    await task2
    print('%s --> end'%datetime.datetime.now())


if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    # tasks = [test1(),test2()]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()

    asyncio.run(main())

    asyncio.run(task())