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
        1、是一个线程执行，不需要创建多线程，协程的执行是无序的
        2、执行效率高，因为子程序（函数）切换不是线程切换，而是由程序自身控制，因此没有线程切换的开销
        3、不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态
    
    使用方法：
        多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
        
        
asyncio模块：

    主要功能：
        1、异步网络操作
        2、并发
        3、协程

    运行协程函数的方式：
        1、loop.run_until_complete()
        2、asyncio.gather()---asyncio.run()
        3、asyncio.create_task()---asyncio.run()
        
    关键字：
        event_loop 事件循环：程序开启一个无限循环，把协程函数注册到事件循环上，事件循环会循环执行这些函数，当某个函数被挂起时，会执行其他的协程函数
        coroutine 协程：协程对象，使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用
        task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
        future：代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
        async：定义一个协程函数，在函数执行过程中可以挂起，去执行其他异步函数，等到挂起条件消失后再回来执行
        await：只能用在协程函数中，用于挂起阻塞的异步调用接口，等待调用，后面只能跟异步程序或有__await__属性的对象
        sleep：暂停执行此任务，为事件循环分配要竞争的任务，并且它（事件循环）监视其所有任务的状态并从一个任务切换到另一个，这里是模拟io任务花费的时间。
        add_done_callback：通过add_done_callback方法给task任务添加回调函数
        
    await作用：
        1、假设有两个异步函数async a，async b，a中的某一步有await，当程序碰到关键字await b()后，异步程序挂起后去执行另一个异步b程序，
        就是从函数内部跳出去执行其他函数，当挂起条件消失后，不管b是否执行完，要马上从b程序中跳出来，回到原程序执行原来的操作
        2、如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，无法在b执行的过程中返回。如果要在b执行完才返回，也就不需要用await关键字了，直接调用b函数就行。
        所以这就需要await后面跟的是异步函数了
        3、执行协程时遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行
        4、await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权
    
    过程：
        开启事件循环 --> 监测task任务 --> 

    https://www.cnblogs.com/a2534786642/p/11013053.html
    https://www.cnblogs.com/zhaof/p/8490045.html
    https://testerhome.com/articles/19703
    https://www.cnblogs.com/rockwall/p/5750900.html

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
# loop.run_until_complete(func()) # 底层将协程函数包装成一个task对象，task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果
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
    print(loop.is_running())
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
    return 'say_after'

async def task():

    # 创建任务事件，异步函数加入参数，底层自动创建了事件循环loop
    task1 = asyncio.create_task(say_after(3,'hello'))
    task2 = asyncio.create_task(say_after(2,'world'))
    task1.add_done_callback(call_back)
    task2.add_done_callback(call_back)

    print('%s --> start'%datetime.datetime.now())
    print(task1)
    print(task2)
    await task1  # 将任务事件加入异步事件循环，等待调用
    await task2
    print(task1)
    print(task2)
    print('%s --> end'%datetime.datetime.now())

def call_back(future):
    print('%s --> %s'%(datetime.datetime.now(),future.result()))





async def func1():
    print('func1 start')
    await func3()
    print('func1 end')

async def func2():
    print('func2 start')
    await asyncio.sleep(2)
    print('func2 end')

async def func3():
    print('func3 start')
    await asyncio.sleep(3)
    print('func3 end')


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    tasks = [func1(),func2()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    # asyncio.run(main())

    # asyncio.run(task())
