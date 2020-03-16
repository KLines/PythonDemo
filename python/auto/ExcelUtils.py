import pandas,datetime
from concurrent.futures import ThreadPoolExecutor
import network,json

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
        e.pd.to_excel('test.xlsx',index=False,encoding='utf-8',keep_default_na=False)

index = 0

def func(item):

    values = list(item.values())

    if 'Y' == values[3].upper():
        url = values[2]
        method = values[4]
        params = values[6]
        if params!='':
            params = json.loads(params)
        if 'GET' == method.upper():
            network.requests_utils(url,method,params=params)
        else:
            network.requests_utils(url,method,json=params)
        global index
        index+=1
        # e.write(item['id'],'Pass')

if __name__ == '__main__':

    # 读取excel数据
    e = Excel('test.xlsx')
    e.read()
    # 开启线程池论询
    start = datetime.datetime.now()
    print(start)
    with ThreadPoolExecutor(max_workers=10,thread_name_prefix="network") as executor:
        for item in e.data_list:
            executor.submit(func,item)
    end = datetime.datetime.now()
    print(end)
    print(index)