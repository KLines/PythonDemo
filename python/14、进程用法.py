import os,time
import multiprocessing

'''
多进程

守护进程和守护线程的区别   
    无论是进程还是线程，都遵循：守护xxx 会等待主xxx 运行完毕后被销毁
    守护进程：只会守护到主进程的代码结束
    守护线程：会守护所有其他非守护线程的结束    
    
创建方式：
    1、通过fork方法创建子进程
    1、通过Process方法创建子进程
    2、通过继承Process类创建子进程

进程同步：
    1、Lock锁--->处理资源共享问题
    2、Condition锁，wait()，notify()--->生产者消费者问题
    3、Semaphore信号量--->控制进程的并发数
    4、Event对象
    5、同步队列
    6、管道（Pipes）

多进程间通信：
    1、使用queue模块，可在进程间进行通信，并保证了进程安全
    2、管道（Pipes）
    3、数据共享manager

进程中断问题：
    1、退出标记
    2、terminate()
    
多进程使用问题：
    1、死锁问题
    2、生产者消费者问题
    3、获取进程任务执行结果
    4、进程池：multiprocessing.Pool，ThreadPoolExecutor

'''


'创建进程'


# Only works on Unix/Linux/Mac:

def process_create():

    if os.name is not 'posix':
        return

    num = 10  # 进程中数据独立
    print(id(num))
    print('Parent process (%s) start...' % os.getpid())
    try:
        pid = os.fork() # 在子进程永远返回0，而在父进程返回子进程的ID
        if pid == 0:
            print("id：",pid)
            print("当前进程id：",os.getpid())
            print('父进程id：',os.getppid())
            num = num - 1
            print('num：',num)
            time.sleep(5)
        else:
            print("id：",pid)
            print("子进程id：",pid)
            print("当前进程id：",os.getpid())
            print('父进程id：',os.getppid())
            print('num：',num)
            time.sleep(2)
    except OSError as e:
        print(e)

# multiprocessing模块就是跨平台版本的多进程模块

def multi_run(name):

    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(3)

def process_multi():

    print('Parent process (%s) start...' % os.getpid())
    p = multiprocessing.Process(target=multi_run,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()  #　此方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')
    print('Parent process (%s) end.'% os.getpid())
    time.sleep(5)


'''
进程池-pool
    1、创建进程池
    2、同步执行、异步执行
    3、进程池的返回值
    4、进程池的回调函数
    5、批量提交进程任务
'''


# 提交单个任务

def single_run(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    return "finished"

def single_result(m):
    print("回调函数",os.getpid())
    print("回调函数",m)

def pool_single()-> None:

    print('Parent process (%s) start...' % os.getpid())
    p = multiprocessing.Pool(4)
    for i in range(5):
        # p.apply(run_proc,args=(i,))  # 同步的执行
        p.apply_async(single_run,args=(i,),callback=single_result)  # 异步的执行

    p.close()  # 结束进程池提交任务
    p.join()

    print('Parent process (%s) end.'% os.getpid())

# 提交批量任务

def map_run(max):
    num = 0
    for i in range(max):
        num +=i
    return num

def pool_map():

    p = multiprocessing.Pool(5)
    results = p.map_async(map_run,(5,10,15))
    p.close()
    p.join()
    for r in results.get(): # 获取执行结果
        print('result-->',r)


'''
进程间通信--管道（Pipes）
    1、Pipe([duplex]):在进程之间创建一条管道，并返回元组（conn1,conn2）,其中conn1，conn2表示管道两端的连接对象
    2、recv()-->如果没有消息可接收，recv()会一直阻塞。如果连接的另外一端已经关闭，那么recv()会抛出EOFError
    3、基于管道实现进程间通信（与队列的方式是类似的，队列就是管道加锁实现的）
'''


def pipe_run(out_pipe,in_pipe):
    in_pipe.close() # 关闭子进程管道输入端，recv()阻塞时会抛出EOFError
    while True:
        try:
            print('Run child process(%s)...' % os.getpid(),out_pipe.recv()) # 无数据时阻塞
        except EOFError as e:
            print(e)
            print("test")
            out_pipe.close()
        except OSError as e:
            print(e)
            break


def process_pipe():
    # 创建管道，必须在产生Process对象之前产生管道
    out_pipe,in_pipe = multiprocessing.Pipe()
    p = multiprocessing.Process(target=pipe_run,args=(out_pipe,in_pipe))
    p.start()
    # 关闭主进程的输出管道端口
    out_pipe.close()
    for i in range(10):
        in_pipe.send("test"+str(i))
    in_pipe.close()


'''
生产者消费者问题

未做同步操作时会出现异常：
    1、produce.send()-->BrokenPipeError: [Errno 32] Broken pipe
    2、consume.recv()-->_pickle.UnpicklingError: invalid load key, '\x00'.
    3、OSError: handle is closed：管道已关闭，但还在获取数据
'''


lock = multiprocessing.Lock()
socks = 0

def producer(produce,consume,name):
    consume.close()
    global socks
    while True:
        if socks < 100:
            socks+=1
            print("%s 生产了--袜子%s"%(name,socks))
            produce.send("袜子%s"%socks)
        else:
            produce.close()
            break

def consumer(produce,consume,name):
    produce.close()
    while True:
        lock.acquire()
        try:
            sock = consume.recv() #　未做同步操作时会出现异常
            print("%s 卖掉了--%s"%(name,sock))
            lock.release()
        except EOFError:
            consume.close()
            lock.release()
            break


def conn_pipe():

    produce,consume = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=producer,args=(produce,consume,"p1"))
    p2 = multiprocessing.Process(target=consumer,args=(produce,consume,"p2"))
    p3 = multiprocessing.Process(target=consumer,args=(produce,consume,"p3"))

    p1.start()
    p2.start()
    p3.start()

    produce.close()
    consume.close()


'''
数据共享 Manager

使用报错：
    conn = self._tls.connection
    AttributeError: 'ForkAwareLocal' object has no attribute 'connection'

原因：
    Manager是在主进程创建的，子进程修改主进程的数据，当主进程执行完毕后会把它里面的连接断开了，
    此时子进程就连接不上主进程，无法修改数据
    
处理list、dict等可变数据类型时，无法直接修改数据，Manager对象无法监测到它引用的可变对象值的修改，
需要通过触发__setitem__方法来让它获得通知，而触发__setitem__方法比较直接的办法就是增加一个中间变量
m_list = m.list()
m_list.append({'id':1})
print(id(m_list[0])) # 每次的id值都不一样，用于不同的进程使用

'''

def manager_dict(m_dic):
    with lock:
        m_dic['count'] -= 1
        print('%s-->%s-->%s'%(os.getppid(),os.getpid(),m_dic))

def manager_list(m_list):
    temp = m_list[0]
    temp['id'] = 2
    m_list[0] = temp
    m_list[1] = 1

    print('%s-->%s-->%s'%(os.getppid(),os.getpid(),m_list))

def func_manager():

    m = multiprocessing.Manager()
    m_dic = m.dict({'count':100})
    m_list = m.list([{'id':1}])
    m_list.append(0)

    print("原始数据：")
    print('%s-->%s-->%s'%(os.getppid(),os.getpid(),m_dic))
    print('%s-->%s-->%s'%(os.getppid(),os.getpid(),m_list))

    print("子进程中修改：")
    process_list = []
    for i in range(5):
        p = multiprocessing.Process(target=manager_dict,args=(m_dic,))
        p.start()
        process_list.append(p)
    p = multiprocessing.Process(target=manager_list,args=(m_list,))
    p.start()
    process_list.append(p)
    for i in process_list: i.join()

    print("修改后数据：")
    print('%s-->%s-->%s'%(os.getppid(),os.getpid(),m_dic))
    print('%s-->%s-->%s'%(os.getppid(),os.getpid(),m_list))


def process_manager():
    p = multiprocessing.Process(target=func_manager)
    p.start()



if __name__ == '__main__':

    # process_create()
    # process_multi()
    # pool_single()
    # pool_map()
    # process_pipe()
    # conn_pipe()
    process_manager()