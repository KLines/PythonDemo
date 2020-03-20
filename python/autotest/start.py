
import sys,os
sys.path.append(os.path.dirname(sys.path[0]))
import autotest.utils as utils
import autotest.test_control as control


if __name__ == '__main__':

    # 读取excel数据
    dir = os.path.dirname(os.path.abspath(__file__))
    e = utils.Excel(dir+'/case/test.xlsx')

    # 开始测试接口
    control.test_api(e)

