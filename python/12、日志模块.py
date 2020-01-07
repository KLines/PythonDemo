

'''
logging模块

https://www.cnblogs.com/Nicholas0707/p/9021672.html
https://www.cnblogs.com/yyds/p/6885182.html
https://www.cnblogs.com/zhbzz2007/p/5943685.html

默认的日志级别设置为WARNING，DEBUG < INFO < WARNING < ERROR < CRITICAL，日志的信息量是依次减少的
'''

import logging
import logging.handlers
import logging.config
import yaml


FILE_NAME = "logging.log"

def print_log(info,type=0):

    with open(FILE_NAME,"a") as file:
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
    log.error(name+"error")
    log.critical(name+"critical")


"====== 通过basicConfig配置日志 ======"

def log_config():

    LOG_FORMAT = "%(asctime)s,%(name)s,level-->%(levelname)s,funcName-->%(funcName)s\nmsg-->%(message)s\n%(pathname)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"

    # filename=os.getcwd()+"\logging.log"

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
            mailhost=("smtp.126.com","25"),
            fromaddr="liukai19900820@126.com",
            toaddrs="471636288@qq.com",
            subject="python发送邮件",
            credentials=("liukai19900820@126.com","10110068172008lk")
        )

        # 4、设置格式器
        formatter = logging.Formatter("%(asctime)s  %(name)s-->%(levelname)s  %(filename)s[:%(lineno)d]-->%(funcName)s\nmsg-->%(message)s")

        # 5、设置处理器输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        st.setLevel(logging.ERROR)
        st.setFormatter(formatter)

        # 6、添加处理器、格式器
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.addHandler(st)

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

    with open("logging.yml", "r") as file:
        dict_conf = yaml.safe_load(file)

    logging.config.dictConfig(dict_conf)

    logger = logging.getLogger("log_dict")

    return logger



# print_log("====== 通过basicConfig配置日志 ======\n")
print_log("====== 通过组件配置日志 ======\n",1)
# print_log("====== 通过fileConfig()配置日志 ======\n",2)
# print_log("====== 通过dictConfig()配置日志 ======\n",3)