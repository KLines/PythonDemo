
import pandas

'''

    xlrd：只能读不能写
    xlwt、xlsxwriter：只能写不能读，xlwt支持2003，xlsxwriter支持2007
    xlutils：将excel中的某个值修改并重新保存
    
'''

class Excel:

    def __init__(self,filename):
        self.filename = filename
        # 防止空值变成nan
        self.pd = pandas.read_excel(self.filename,encoding='utf-8',keep_default_na=False)
        self.data_list = []

    def read(self):
        for index in self.pd.index.values:
            row_data = self.pd.loc[index].to_dict()
            self.data_list.append(row_data)

    def write(self,id:int,result:str):
        self.pd.loc[id-1,'测试结果']=result
        self.pd.to_excel(self.filename,index=False,encoding='utf-8')



