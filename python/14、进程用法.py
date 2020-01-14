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
    1、使用全局变量，需要加锁　　
    2、使用queue模块，可在进程间进行通信，并保证了进程安全
    3、管道（Pipes）

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

def func_porcess():

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

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(3)


def func_multi():

    print('Parent process (%s) start...' % os.getpid())
    p = multiprocessing.Process(target=run_proc,args=('test',))
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

def func1(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    return "finished"

def func2(m):
    print("回调函数",os.getpid())
    print("回调函数",m)

def func_pool()-> None:

    print('Parent process (%s) start...' % os.getpid())
    p = multiprocessing.Pool(4)
    for i in range(5):
        # p.apply(run_proc,args=(i,))  # 同步的执行
        p.apply_async(func1,args=(i,),callback=func2)  # 异步的执行

    p.close()  # 结束进程池提交任务
    p.join()

    print('Parent process (%s) end.'% os.getpid())

# 提交批量任务

def func_add(max):
    num = 0
    for i in range(max):
        num +=i
    return num

def func_map():

    p = multiprocessing.Pool(5)
    results = p.map_async(func_add,(5,10,15))
    p.close()
    p.join()
    for r in results.get():
        print('result-->',r)


if __name__ == '__main__':

    # func_porcess()
    # func_multi()
    # func_pool()
    func_map()