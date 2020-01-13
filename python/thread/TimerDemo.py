

'''
常用的定时任务实现方式：

    1.循环+sleep
    
    2.线程模块中Timer类
    
    3.schedule第三方模块
    
    4.APScheduler任务框架
'''


def func():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time,"运行任务")


# 循环+sleep

def func_while():

    while True:
        func()
        sleep(3)


# 线程模块中Timer类

def func_timer():

    task = Timer(3,func) # 定时器只能执行一次
    task.start()


# schedule第三方模块

def func_schedule():

    schedule.every(3).seconds.do(func)
    while True:
        schedule.run_pending()


# APScheduler任务框架

def func_aps():
    scheduler = BlockingScheduler()
    scheduler.add_job(func,'interval',seconds=3, id="job1")
    scheduler.start()


if __name__ == '__main__':

    import datetime
    import schedule
    from time import sleep
    from threading import Timer
    from apscheduler.schedulers.blocking import BlockingScheduler

    # func_while()
    # func_timer()
    # func_schedule()
    func_schedule()