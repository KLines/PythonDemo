from concurrent.futures import ThreadPoolExecutor
import datetime
import threading
from time import sleep

'''
线程池
    １、concurrent.futures模块
    
        当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数
        

        Executor
            |--ThreadPoolExecutor 用于创建线程池
            |--ProcessPoolExecutor 用于创建进程池

        Exectuor    
            |---submit(fn, *args, **kwargs)：将 fn 函数提交给线程池，*args、*kwargs 代表 fn 函数传入参数
            |---map(func, *iterables, timeout=None, chunksize=1)：该函数将会启动多个线程，以异步方式立即对 iterables 执行 map 处理
            |---shutdown(wait=True)：关闭线程池

        Future
            |--cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
            |--cancelled()：返回 Future 代表的线程任务是否被成功取消。
            |--running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
            |--done()：如果该 Funture 代表的线程任务被成功取消或执行完成，则该方法返回 True。
            |--result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程，其中 timeout 参数指定最多阻塞多少秒。
            |--exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
            |--add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。

    ２、threadpool第三方模块
'''

def func(max):
    my_sum = 0
    for i in range(max):
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("%s---%s 线程运行"%(time,threading.current_thread().name) + '  ' + str(i))
        my_sum += i
    sleep(1)
    return my_sum


def func_pool():

    thread_pool = ThreadPoolExecutor(max_workers=4,thread_name_prefix="thread_pool")
    for i in range(10):
        thread_pool.submit(func,10)

    thread_pool.shutdown()


def func_future():

    with ThreadPoolExecutor(4) as executor:
        for i in range(10):
            result = executor.submit(func,5)
            # print('====',result.result())
            result.add_done_callback(func_result)


def func_result(result):
    print('====',result.result())


def func_map():

    with ThreadPoolExecutor(4) as executor:
        results = executor.map(func,(5,10,15))
        for r in results:
            print('====',r)

if __name__ == '__main__':

    # func_pool()
    # func_future()
    func_map()