

'''
logging模块

https://www.cnblogs.com/Nicholas0707/p/9021672.html
https://www.cnblogs.com/yyds/p/6885182.html

默认的日志级别设置为 WARNING，

DEBUG < INFO < WARNING < ERROR < CRITICAL，日志的信息量是依次减少的

handler名称：位置；作用

StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
FileHandler：logging.FileHandler；日志输出到文件

注意多线程时的使用
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
RotatingFileHandler：logging.handlers.RotatingFileHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
TimedRotatingFileHandler：logging.handlers.TimedRotatingFileHandler；日志回滚方式，在一定时间区域内回滚日志文件

SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址

SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器

'''

import logging
import logging.handlers
import logging.config
import yaml
import time


FILE_NAME = "logger.log"

def print_log(info,type=0):

    with open(FILE_NAME,"a",encoding="utf-8") as file:
        file.write(info)

    # 删除所有现有的处理程序，重新生成basicConfig
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    log = logging

    name = "basicConfig:"
    if type == 1:
        log = log_components()
        name = "components:"
    elif type == 2:
        log = log_fileConfig()
        name = "fileConfig:"
    elif type == 3:
        log = log_dictConfig()
        name = "dictConfig:"
    else:
        log_config()

    log.debug(name+"debug")
    log.info(name+"info")
    log.warning(name+"warning")
    try:
        open("temp.txt","r")
    except Exception:
        # 捕获traceback
        log.error(name+"error",exc_info = True)
        # log.exception(name+"error")
    log.critical(name+"critical")


"====== 通过basicConfig配置日志 ======"

def log_config():

    LOG_FORMAT = "%(asctime)s,%(name)s,level-->%(levelname)s,funcName-->%(funcName)s\nmsg-->%(message)s\n%(pathname)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"

    # filename=os.getcwd()+"\logger.log"

    logging.basicConfig(level=logging.DEBUG,
                        format= LOG_FORMAT,
                        datefmt= DATE_FORMAT,
                        handlers=[logging.FileHandler(FILE_NAME,encoding="utf-8"),logging.StreamHandler()])

"====== 通过组件配置日志 ======"

# Logger（日志器）, Handler（处理器）, Filter（过滤器）, Formatter（格式器）

def log_components():

    # 1、创建日志器
    logger = logging.getLogger("log_components")

    # 2、设置日志等级
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:

        # 3、创建处理器
        fh = logging.FileHandler(FILE_NAME,encoding="utf-8")
        ch = logging.StreamHandler() # 控制台输出
        st = logging.handlers.SMTPHandler(
            mailhost=("smtp.mxhichina.com","25"),
            fromaddr="xxx@xx.com",
            toaddrs="yyy@yy.com",
            subject="python发送邮件",
            credentials=("xxx@xx.com","xx")
        )

        "====== 配置日志回滚 ======"

        # 定义一个RotatingFileHandler，最多备份２个日志文件，每个日志文件最大128Bytes
        rh = logging.handlers.RotatingFileHandler(FILE_NAME, maxBytes=1*128, backupCount=2, encoding="utf-8")

        nowtime = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))

        # 定义一个TimedRotatingFileHandler，最多备份２个日志文件，每隔１分钟自动保存
        th = logging.handlers.TimedRotatingFileHandler(FILE_NAME, when="m", interval=1, backupCount=2, encoding="utf-8")

        # 4、设置格式器
        formatter = logging.Formatter("%(asctime)s  %(name)s-->%(levelname)s  %(filename)s[:%(lineno)d]-->%(funcName)s\nmsg-->%(message)s")

        # 5、设置处理器输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        st.setLevel(logging.ERROR)
        st.setFormatter(formatter)
        rh.setLevel(logging.ERROR)
        rh.setFormatter(formatter)
        th.setLevel(logging.ERROR)
        th.setFormatter(formatter)

        # 6、添加处理器、格式器
        logger.addHandler(fh)
        logger.addHandler(ch)
        # logger.addHandler(st)
        # logger.addHandler(rh)
        # logger.addHandler(th)

    # logger.removeHandler(fh)

    return logger


"====== 通过fileConfig()配置日志 ======"

def log_fileConfig():

    # 读取配置文件信息
    logging.config.fileConfig("logging.conf")

    logger = logging.getLogger("log_conf")

    return logger


"====== 通过dictConfig()配置日志 ======"

def log_dictConfig():

    with open("logging.yml", "r", encoding="utf-8") as file:
        dict_conf = yaml.safe_load(file)

    logging.config.dictConfig(dict_conf)

    logger = logging.getLogger("log_dict")

    return logger



if __name__ == '__main__':

    # while True:
    #     time.sleep(0.1)

        print_log("\n====== 通过basicConfig配置日志 ======\n\n")
        print_log("\n====== 通过组件配置日志 ======\n\n",1)
        print_log("\n====== 通过fileConfig()配置日志 ======\n\n",2)
        print_log("\n====== 通过dictConfig()配置日志 ======\n\n",3)