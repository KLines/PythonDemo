import datetime,threading,time
import asyncio,os
import functools

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

    运行并发方式：
        1、loop.run_until_complete(asyncio.await(tasks))
        2、asyncio.gather()---asyncio.run()
        3、asyncio.create_task()---asyncio.run()
        
    关键字：
        event_loop 事件循环：程序开启一个无限循环，把协程函数注册到事件循环上，事件循环会循环执行这些函数，当某个函数被挂起时，会执行其他的协程函数
        coroutine：协程对象，使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用
        task：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
        future：代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
        async：定义一个协程函数，在函数执行过程中可以被挂起，去执行其他函数，等到挂起条件消失后再回来执行
        await：只能用在协程函数中，用于挂起耗时操作，后面只能跟异步程序或有__await__属性的对象
        sleep：暂停执行此任务，为事件循环分配要竞争的任务，并且它（事件循环）监视其所有任务的状态并从一个任务切换到另一个
        
    await作用：
        1、await针对耗时操作进行挂起，就像生成器里的yield一样，使函数让出控制权。耗时的操作一般是一些IO操作，例如网络请求，文件读取等。
        2、执行协程时遇到await，事件循环将会挂起该协程，执行其他协程。当挂起条件消失后，不管其它协程是否执行完，要马上从程序中跳出来，回到原协程执行原来的操作
        
    gather和wait的区别：
        gather是需要所有任务都执行结束，如果某一个协程函数崩溃了，则会抛异常，都不会有结果
        wait可以定义函数返回的时机，可以是FIRST_COMPLETED(第一个结束的), FIRST_EXCEPTION(第一个出现异常的), ALL_COMPLETED(全部执行完，默认的)
        gather按输入协程的顺序返回对应协程的执行结果，wait返回任务集合
        asyncio.wait(tasks)、asyncio.gather(*tasks)，前者接受一个task列表，后者接收一堆task
        
    encure_future和create_task的区别：
        encure_future: 最高层的函数
        create_task: 在确定参数是 coroutine 的情况下可以使用，底层调用 loop.create_task()    
    
    
    
    过程：
        开启事件循环 --> 监测task任务 --> 

    停止run_forever

    https://www.cnblogs.com/zhaof/p/8490045.html
    https://testerhome.com/articles/19703
    
    
    https://www.cnblogs.com/a2534786642/p/11013053.html
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


# c = consumer()
# producer(c)


'异步IO'

# 1、使用async关键字定义一个协程函数
async def func():
    print('%s %s --> write'%(datetime.datetime.now(),threading.current_thread().getName()))
    await asyncio.sleep(1)
    print('%s %s --> read'%(datetime.datetime.now(),threading.current_thread().getName()))

# 2、返回一个事件循环对象，是asyncio.Baseeventloop的实例
# loop = asyncio.get_event_loop()

# 3、将协程函数加入到事件循环loop，并启动事件循环
# loop.run_until_complete(func()) # 是一个阻塞方法，只有协程运行结束后这个方法才结束，才会运行之后的代码
# loop.close()



'asyncio--运行并发函数'

async def test(name,delay):
    print('%s %s --> %s start'%(datetime.datetime.now(),threading.current_thread().getName(),name))
    await asyncio.sleep(delay)
    print('%s %s --> %s end'%(datetime.datetime.now(),threading.current_thread().getName(),name))
    return name

async def test_gather():
    # 同时将两个异步函数对象加入事件循环，但并不运行等待调用，底层会自动创建异步事件循环
    res = await asyncio.gather(test('test1',3),test('test2',2))
    print(res)

async def test_task():
    # 创建任务事件，底层自动创建了事件循环loop
    task1 = asyncio.create_task(test('test1',3))
    task2 = asyncio.create_task(test('test2',2))
    task1.add_done_callback(call_back)
    task2.add_done_callback(call_back)

    print(task1)
    print(task2)
    # 将任务事件加入异步事件循环，等待调用
    await task1
    await task2
    print(task1)
    print(task2)

def call_back(task):
    print('%s %s --> result：%s'%(datetime.datetime.now(),threading.current_thread().getName(),task.result()))

def run_test():

    # 运行并发函数-->使用wait
    loop = asyncio.get_event_loop()
    tasks = [test('test1',3),test('test2',2)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    # 运行并发函数-->使用gather
    asyncio.run(test_gather())

    # 运行并发函数-->创建task任务
    asyncio.run(test_task())



'asyncio--协程嵌套'

async def func1():
    print('%s func1 start'%datetime.datetime.now())
    await func3()
    print('%s func1 end'%datetime.datetime.now())
    return 'func1'

async def func2():
    print('%s func2 start'%datetime.datetime.now())
    await asyncio.sleep(3)
    # n = 1
    # while n <100000000:
    #     n+=1
    print('%s func2 end'%datetime.datetime.now())
    return 'func2'

async def func3():
    print('%s func3 start'%datetime.datetime.now())
    await asyncio.sleep(2)
    print('%s func3 end'%datetime.datetime.now())
    return 'func3'

def run_func():
    tasks = [
        asyncio.ensure_future(func1()),
        asyncio.ensure_future(func2())
    ]

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*tasks))  # 将list元素拆解成独立元素入参
    loop.close()

    for result in results:
        print(result)



'asyncio--多个协程任务的并行在子线程中'

def request(url,delay):
    print('%s %s --> 同步函数运行，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))
    time.sleep(delay)
    print('%s %s --> 同步函数结束，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))

def test_sync(loop):
    # 使用单线程串行执行，相当于变成线程去阻塞执行添加进去的函数
    loop.call_soon_threadsafe(request,'www.baidu.com')
    loop.call_soon_threadsafe(request,'www.sina.com')
    loop.call_soon_threadsafe(request,'www.sohu.com')

    # 使用线程池并行执行
    # loop.run_in_executor(None,request,'www.baidu.com')
    # loop.run_in_executor(None,request,'www.sina.com')
    # loop.run_in_executor(None,request,'www.sohu.com')

async def ping(url,delay):
    print('%s %s --> 协程函数运行，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))
    await asyncio.sleep(delay)
    print('%s %s --> 协程函数结束，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))

async def test_async():
    tasks = [
        asyncio.create_task(ping('www.baidu.com',1)),
        asyncio.create_task(ping('www.sina.com',3)),
        asyncio.create_task(ping('www.sohu.com',2))
    ]
    await asyncio.gather(*tasks)

def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def run_thread():

    loop = asyncio.get_event_loop()

    test = threading.Thread(target=start_thread_loop,args=(loop,),name='test')
    test.start()

    '执行同步函数'
    # test_sync(loop)

    '执行协程函数'
    asyncio.run_coroutine_threadsafe(test_async(),loop)


if __name__ == '__main__':

    print('%s MainThread start'%datetime.datetime.now())

    # run_test()

    # run_func()

    run_thread()

    print('%s MainThread end'%datetime.datetime.now())



