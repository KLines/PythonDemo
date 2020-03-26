import datetime,threading,time
import asyncio


'''

asyncio模块：

    主要功能：
        1、异步网络操作
        2、并发
        3、协程

    启动事件轮询
        1、asyncio.run()：底层创建loop，调用run_until_complete()，运行完后自动关闭loop
        2、loop.run_until_complete()：是一个阻塞方法，只有协程函数全部运行结束后这个方法才结束，才会运行之后的代码
        3、loop.run_forever()：是一个阻塞方法，即使协程函数全部运行结束，该方法还会一直运行，需手动停止loop
        
    event_loop：
        1、get_running_loop()：返回在当前线程中正在运行的事件循环
        2、get_event_loop()：获得一个事件循环，如果当前线程还没有事件循环，则创建一个新的事件循环loop
        3、set_event_loop(loop)：设置一个事件循环为当前线程的事件循环
        4、new_event_loop()：创建一个新的事件循环
        注意：同一个线程中是不允许有多个事件循环loop
    
    创建Task：
        1、asyncio.create_task()
        2、asyncio.encure_future()
        3、loop.create_task()：创建任务后直接运行，不用手动开启事件轮询
        注意：coroutine可以自动封装成task，而Task是Future的子类

    并发运行多个任务：
        1、asyncio.await([task1,task2,task3])
        2、asyncio.gather(*[task1,task2,task3]) 或 asyncio.gather(task1,task2,task3)
        
  
        
    
        
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
    https://blog.csdn.net/qq_27825451/article/details/86218230
    
    
    https://www.cnblogs.com/a2534786642/p/11013053.html
    https://www.cnblogs.com/rockwall/p/5750900.html

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

def call_back(task):
    print('%s %s --> result：%s'%(datetime.datetime.now(),threading.current_thread().getName(),task.result()))

def test_task():
    # 创建任务事件，底层自动创建了事件循环loop
    task1 = asyncio.create_task(func('test1',3))
    task2 = asyncio.create_task(func('test2',2))
    task1.add_done_callback(call_back)
    task2.add_done_callback(call_back)

    print(task1)
    print(task2)
    # 将任务事件加入异步事件循环，等待调用
    # await task1
    # await task2
    print(task1)
    print(task2)
    return [task1,task2]


def run_task():
    # asyncio.run(test_task())
    loop = asyncio.get_event_loop()
    task1 = asyncio.ensure_future(func('task1',3))
    loop.create_task(func('task2',2))
    loop.run_until_complete(task1)
    # loop.run_until_complete(task1)
    # loop.run_until_complete(task2)
    # loop.run_until_complete(asyncio.wait([task1,task2]))
    loop.close()



async def test_gather():
    # 同时将两个异步函数对象加入事件循环，但并不运行等待调用，底层会自动创建异步事件循环
    res = await asyncio.gather(func('test1',3),func('test2',2))
    print(res)










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


async def test_async(loop):
    tasks = [
        asyncio.create_task(ping('www.baidu.com',1)),
        asyncio.create_task(ping('www.sina.com',3)),
        asyncio.create_task(ping('www.sohu.com',2))
    ]
    await asyncio.gather(*tasks)
    loop.stop()

def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def run_thread():

    # 主线程创建一个事件循环，在子线程中启动事件循环，主线程不会被block
    loop = asyncio.get_event_loop()
    test = threading.Thread(target=start_thread_loop,args=(loop,),name='test')
    test.start()

    '执行同步函数'
    # test_sync(loop)

    '执行协程函数'
    asyncio.run_coroutine_threadsafe(test_async(loop),loop)



if __name__ == '__main__':

    print('%s MainThread start'%datetime.datetime.now())

    run_task()

    # run_func()

    # run_thread()

    print('%s MainThread end'%datetime.datetime.now())



