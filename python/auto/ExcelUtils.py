
# import sys,os
# sys.path.append(os.path.dirname(sys.path[0]))  # 保证系统环境下可以调用其他module中的文件

import pandas
from concurrent.futures import ThreadPoolExecutor
import network,json
import datetime,time

'''
    xlrd：只能读不能写
    xlwt、xlsxwriter：只能写不能读，xlwt支持2003，xlsxwriter支持2007
    xlutils：将excel中的某个值修改并重新保存
    https://segmentfault.com/a/1190000018177573
'''

class Excel:

    def __init__(self,filename):
        self.filename = filename
        # 防止空值变成nan
        self.pd = pandas.read_excel(self.filename,encoding='utf-8',keep_default_na=False)

    def read(self):
        self.data_list = []
        for index in self.pd.index.values:
            row_data = self.pd.loc[index].to_dict()
            self.data_list.append(row_data)

    def write(self,id:int,result:str):
        self.pd.loc[id-1,'测试结果']=result
        e.pd.to_excel(self.filename,index=False,encoding='utf-8')

index = 0

def func(item):

    values = list(item.values())

    if 'Y' == values[3].upper():
        url = values[2]
        method = values[4]
        params = values[6]
        if params!='':
            params = json.loads(params)
        try:

            if 'GET' == method.upper():
                network.requests_utils(url,method,params=params)
            else:
                network.requests_utils(url,method,json=params)
            e.write(values[0],'Pass')
        except:
            e.write(item['id'],'Failure')
            pass

        global index
        index+=1


'''

在系统环境中sys.path默认只有文件的当前路径，没有父路径，因此需手动添加代码文件路径。而在IDE环境下会显示所有路径

    Ubuntu运行sys.path：
    ['/home/pc190559/demo/PythonDemo/python/auto', '/usr/lib/python37.zip', '/usr/lib/python3.7', 
    '/usr/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages']
    
    IDE运行sys.path：
    ['/home/pc190559/demo/PythonDemo/python/auto', '/home/pc190559/demo/PythonDemo/python', 
    '/home/pc190559/develop/pycharm/plugins/python/helpers/pycharm_display', '/usr/lib/python37.zip', '/usr/lib/python3.7', 
    '/usr/lib/python3.7/lib-dynload', '/home/pc190559/demo/PythonDemo/python/venv/lib/python3.7/site-packages',
     '/home/pc190559/develop/pycharm/plugins/python/helpers/pycharm_matplotlib_backend']
     
    # print(os.path.abspath(__file__)) # 返回绝对路径
    # print(os.path.basename(__file__)) # 返回文件名
    # print(os.path.dirname(__file__)) # 返回文件路径


获取第三方lib包路径信息：

    Ubuntu下Python3.7：
    1、系统Python3.7自带的lib包目录：/usr/lib/python3.7
    2、系统Python3.7对应的第三方lib包目录：/usr/lib/python3/dist-packages   
    
    IDE环境下
    1、系统Python3.7自带的lib包目录：/usr/lib/python3.7
    2、独立项目中第三方lib包目录：/xx/xx/venv/lib/python3.7/site-packages
    
    from distutils.sysconfig import get_python_lib
    print(get_python_lib())
    在IDE中运行获取的是项目中/venv/xx/site-packages目录，在系统环境通过python命令运行获取的是/usr/lib/python3/dist-packages目录
   
    注意
    1、升级系统自带的第三方lib包
    2、设置IDE中的Project Interpreter环境
    
解决办法：
    1、在文件头部导入当前文件父路径，必须在其他import之前导入
        # import sys,os
        # sys.path.append(os.path.dirname(sys.path[0]))  # 保证系统环境下可以调用其他module中的文件
    2、创建xxx.pth文件，将此文件添加到系统目录下/usr/lib/python3/dist-packages中
        添加当前项目路径-->解决通过python命令执行代码时无法调用其他module中的文件
        添加当前项目下的/xx/xx/venv/lib/python3.7/site-packages路径-->解决通过python命令执行代码时无法使用venv中的第三方lib包
    3、通过python命令pip3 list可以查询出系统在＋venv中下载的所有第三方lib包
        pip3 list 查询所有lib包
        pip3 install --upgrade xx 升级lib包
    　
'''

if __name__ == '__main__':

    # 读取excel数据
    import os
    e = Excel(os.path.dirname(__file__)+'/test.xlsx')
    e.read()

    # 开启线程池论询
    start = time.time()
    network.log_info('开始时间：'+str(datetime.datetime.now()))

    with ThreadPoolExecutor(max_workers=10,thread_name_prefix="network") as executor:
        for item in e.data_list:
            executor.submit(func,item)

    end = time.time()
    network.log_info('结束时间：'+str(datetime.datetime.now()))
    network.log_info('共计%s个接口，总耗时%s秒'%(index,end-start))
