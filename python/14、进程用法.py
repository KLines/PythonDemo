import os,time
import multiprocessing
import datetime

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

# Only works on Unix/Linux/Mac:

def process_create():

    if os.name is not 'posix':
        return

    num = 10
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

#　提交单个任务

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

'进程间通信--管道（Pipes）'

def pipe_run(out_pipe,in_pipe):
    in_pipe.close() # 关闭子进程管道输入端
    while True:
        try:
            print("test")
            print('Run child process(%s)...' % os.getpid(),out_pipe.recv()) # 无数据时阻塞
        except EOFError as e: # 当pipe的输入端被关闭，且无法接收到输入的值，那么就会抛出EOFError
            print("test1")
            print(e)
            out_pipe.close()
        except OSError as e:
            print("test2")
            print(e)
            break

def process_pipe():
    # 创建管道
    out_pipe,in_pipe = multiprocessing.Pipe()
    p = multiprocessing.Process(target=pipe_run,args=(out_pipe,in_pipe))
    p.start()
    # 关闭主进程的输出管道端口
    out_pipe.close()
    for i in range(10):
        in_pipe.send("test"+str(i))
    in_pipe.close()


'生产者消费者问题'

count = 0
conn = multiprocessing.Condition()

def producer(produce,consume,name):
    global count
    consume.close()
    while True:
        count+=1
        # time.sleep(0.1)
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("%s %s 生产了--袜子%s"%(date,name,count))
        produce.send("袜子%s"%count)

def consumer(produce,consume,name):
    produce.close()
    while True:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("%s %s 卖掉了--%s"%(date,name,consume.recv()))

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


# 数据共享 Manager
# https://www.cnblogs.com/liuhailong-py-way/p/5680588.html

lock = multiprocessing.Lock()

def manager_run(dic):
    lock.acquire()
    dic['count'] -= 1
    print('%s-->%s'%(os.getpid(),dic))
    lock.release()

def process_man(dic):
    p_lst = []
    for i in range(5):
        p = multiprocessing.Process(target=manager_run,args=(dic,))
        p.start()
        p_lst.append(p)
    for i in p_lst: i.join()

if __name__ == '__main__':

    # process_create()
    # process_multi()
    # pool_single()
    # pool_map()
    # process_pipe()
    # conn_pipe()
    m = multiprocessing.Manager()
    dic=m.dict({'count':100})
    process_man(dic)
    print('%s-->%s'%(os.getpid(),dic))
