import datetime,threading,time
import asyncio
import functools

'''

asyncio模块：

    主要功能：
        1、异步网络操作
        2、并发
        3、协程
            协程函数（coroutine function）：由async def定义的函数
            协程对象（coroutine object）：调用协程函数返回的对象

    启动事件轮询
        1、asyncio.run()：底层创建loop，调用run_until_complete()，运行完后自动关闭loop，总是创建一个新的事件循环
        2、loop.run_until_complete()：是一个阻塞方法，只有协程函数全部运行结束后这个方法才结束，才会运行之后的代码
        3、loop.run_forever()：是一个阻塞方法，即使协程函数全部运行结束，该方法还会一直运行，需手动停止loop，再关闭loop
        注意：事件轮询在哪个线程启动，协程函数就在哪个线程执行，哪个线程就会阻塞
        
    event_loop：
        1、get_running_loop()：返回在当前线程中正在运行的事件循环
        2、get_event_loop()：获得一个事件循环，如果当前线程还没有事件循环，则创建一个新的事件循环loop
            1、在主线程中调用时，可以直接运行，创建event_loop，但是子线程中运行异常
        3、set_event_loop(loop)：设置一个事件循环为当前线程的事件循环
        4、new_event_loop()：创建一个新的事件循环
        注意：同一个线程中是不允许有多个事件循环loop
    
    创建Task：
        1、asyncio.create_task()：必须在协程函数中创建，才能在run_until_complete()调用，底层先调用get_running_loop()，再调用loop.create_task() 
        2、asyncio.encure_future()：创建Task后，直接在run_until_complete()调用
        3、loop.create_task()：创建任务后直接运行，不用手动开启事件轮询
        注意：coroutine可以自动封装成task，而Task是Future的子类

    并发运行多个任务：
        1、asyncio.wait([task1,task2,task3])
        2、asyncio.gather(*[task1,task2,task3]) 或 asyncio.gather(task1,task2,task3)
       
    关键字：
        event_loop：程序开启一个无限循环，把协程函数注册到事件循环上，事件循环会循环执行这些函数，当某个函数被挂起时，会执行其他的协程函数
        coroutine：使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象
        task：任务是对协程函数进一步封装，其中包含了任务的各种状态
        future：代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
        async：定义一个协程函数，在函数执行过程中可以被挂起，去执行其他函数，等到挂起条件消失后再回来执行
        await：只能用在协程函数中，用于挂起耗时操作，后面只能跟异步程序或有__await__属性的对象
        sleep：暂停执行此任务，为事件循环分配要竞争的任务，并且它（事件循环）监视其所有任务的状态并从一个任务切换到另一个 
        
    gather和wait的区别：
        1、gather是需要所有任务都执行结束，如果某一个协程函数崩溃了，则会抛异常，都不会有结果
        2、wait可以定义函数返回的时机，可以是FIRST_COMPLETED、FIRST_EXCEPTION、ALL_COMPLETED(默认的)
        3、gather按输入协程的顺序返回对应协程的执行结果，wait返回任务集合
        
    await作用：
        1、await针对耗时操作进行挂起，就像生成器里的yield一样，使函数让出控制权。耗时的操作一般是一些IO操作，例如网络请求，文件读取等
        2、执行协程时遇到await，事件循环将会挂起该协程，执行其他协程。当挂起条件消失后，不管其它协程是否执行完，要马上从程序中跳出来，回到原协程执行原来的操作

    不同线程的事件循环：
        场景：
            1、子线程执行同步函数
            2、子线程执行协程函数
        实现方法：
            1、在主线程中创建event_loop，传递至在子线程中，调用set_event_loop设置，开启事件循环
            2、在子线程中创建event_loop，开始事件循环

    https://www.cnblogs.com/zhaof/p/8490045.html
    https://testerhome.com/articles/19703
    https://blog.csdn.net/qq_27825451/article/details/86218230
    https://www.cnblogs.com/a2534786642/p/11013053.html
    
    
'''


'自定义协程函数'

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

async def func(name,delay):
    print('%s %s --> %s start'%(datetime.datetime.now(),threading.current_thread().getName(),name))
    await asyncio.sleep(delay)
    print('%s %s --> %s end'%(datetime.datetime.now(),threading.current_thread().getName(),name))
    return name


'asyncio--并发运行'

def run_concurrency():
    tasks = (
        [
            func('gather1',3),
            func('gather2',2)
        ],
        [
            func('wait1',3),
            func('wait2',2)
        ]
    )
    loop = asyncio.get_event_loop()
    # 运行并发函数-->使用gather
    loop.run_until_complete(asyncio.gather(*tasks[0]))
    # 运行并发函数-->使用wait
    loop.run_until_complete(asyncio.wait(tasks[1]))
    loop.close()


'asyncio--Task任务'

async def test_task():
    task = asyncio.create_task(func('test2',2))
    task.add_done_callback(call_back)
    print(task)
    await task
    print(task)

def call_back(task):
    print('%s %s --> result：%s'%(datetime.datetime.now(),threading.current_thread().getName(),task.result()))

def run_task():

    # asyncio.run(test_task())

    loop = asyncio.get_event_loop()

    task = asyncio.ensure_future(func('task1',3))
    task.add_done_callback(call_back)
    loop.create_task(func('task3',1))

    loop.run_until_complete(asyncio.gather(task,test_task()))
    loop.close()


'asyncio--协程嵌套'

async def test1():
    print('%s test1 start'%datetime.datetime.now())
    await test3()
    print('%s test1 end'%datetime.datetime.now())
    return 'test1'

async def test2():
    print('%s test2 start'%datetime.datetime.now())
    await asyncio.sleep(3)
    # n = 1
    # while n <100000000:
    #     n+=1
    print('%s test2 end'%datetime.datetime.now())
    return 'test2'

async def test3():
    print('%s test3 start'%datetime.datetime.now())
    await asyncio.sleep(2)
    print('%s test3 end'%datetime.datetime.now())
    return 'test3'

async def run_nest():
    tasks = [
        asyncio.ensure_future(test1()),
        asyncio.ensure_future(test2())
    ]

    results = await asyncio.gather(*tasks) # 将list元素拆解成独立元素入参

    for result in results:
        print(result)


'asyncio--子线程中并发运行多个协程任务'

# 同步函数
def sync_ping(url,delay):
    print('%s %s --> 同步函数运行，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))
    time.sleep(delay)
    print('%s %s --> 同步函数结束，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))

def sync_task(loop):

    # 使用单线程串行执行，相当于变成线程去阻塞执行添加进去的函数
    # loop.call_soon_threadsafe(sync_ping,'www.baidu.com',1)
    # loop.call_soon_threadsafe(sync_ping,'www.sina.com',3)
    # loop.call_soon_threadsafe(sync_ping,'www.sohu.com',2)

    # 使用线程池并行执行
    task1 = loop.run_in_executor(None,sync_ping,'www.baidu.com',1) # 返回的是Future类型
    task2 = loop.run_in_executor(None,sync_ping,'www.sina.com',3)
    task3 = loop.run_in_executor(None,sync_ping,'www.sohu.com',2)
    tasks = asyncio.gather(task1,task2,task3)
    # # https://www.jianshu.com/p/7fd361cde22c
    tasks.add_done_callback(functools.partial(loop_stop, loop))

def loop_stop(loop, future):    # 函数的最后一个参数须为 future
    loop.stop()
    print(loop.is_closed())
    print(loop.is_running())

def thread_sync_loop(loop):
    print(id(loop))
    asyncio.set_event_loop(loop)
    sync_task(loop)
    loop.run_forever()
    loop.close()
    print(loop.is_closed())
    print(loop.is_running())


# 协程函数
async def aysnc_ping(url,delay):
    print('%s %s --> 协程函数运行，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))
    await asyncio.sleep(delay)
    print('%s %s --> 协程函数结束，当前url：%s'%(datetime.datetime.now(),threading.current_thread(),url))
    return url

async def aysnc_task(loop):
    tasks = [
        asyncio.create_task(aysnc_ping('www.baidu.com',1)),
        asyncio.create_task(aysnc_ping('www.sina.com',3)),
        asyncio.create_task(aysnc_ping('www.sohu.com',2))
    ]
    for task in tasks:
        task.add_done_callback(call_back)
    await asyncio.gather(*tasks)
    # print(threading.current_thread(),id(loop))
    # print(threading.current_thread(),id(asyncio.get_event_loop()))
    loop.stop() # 停止事件循环，stop 后仍可重新运行，close 后不可

def thread_async_loop(loop):

    # 可有可无，在当前线程启动事件轮询后自动设置
    # asyncio.set_event_loop(loop)

    try:
        loop.run_forever()
    finally:
        loop.close() # 关闭事件循环，只有 loop 处于停止状态才会执行



def run_thread():

    loop = asyncio.get_event_loop()

    '执行同步函数'
    sync_loop = threading.Thread(target=thread_sync_loop,args=(loop,),name='thread_sync')
    # sync_loop.start()

    '执行协程函数'
    async_loop = threading.Thread(target=thread_async_loop,args=(loop,),name='thread_async')
    async_loop.start()

    loop.create_task(func('task',1))
    # 从当前线程向运行事件循环的线程提交协程任务
    asyncio.run_coroutine_threadsafe(aysnc_task(loop),loop)


if __name__ == '__main__':

    print('%s MainThread start'%datetime.datetime.now())

    # run_concurrency()

    # run_task()

    # asyncio.run(run_nest())

    run_thread()

    print('%s MainThread end'%datetime.datetime.now())



