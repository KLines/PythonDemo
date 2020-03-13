import pandas

'''
    xlrd：只能读不能写
    xlwt、xlsxwriter：只能写不能读，xlwt支持2003，xlsxwriter支持2007
    xlutils：将excel中的某个值修改并重新保存
    https://segmentfault.com/a/1190000018177573
'''

class Excel:

    def __init__(self,filename):
        pass

    def read(self):
        pass

    def write(self):
        pass


# if __name__ == '__main__':

p = pandas.read_excel('test.xlsx',encoding='utf-8')
print(p)


    # e = Excel('w','test.xlsx')
    #
    # e.write()
    #
    # e.read()
    #
    # for data in e.list_data:
    #     print(data)
