
from concurrent.futures import ThreadPoolExecutor
import datetime,time,json
import autotest.utils as utils


def func_api(item):

    values = list(item.values())

    if 'Y' == values[3].upper():
        url = values[2]
        method = values[4]
        params = values[6]
        if params!='':
            params = json.loads(params)
        try:
            if 'GET' == method.upper():
                utils.requests_utils(url,method,params=params)
            else:
                utils.requests_utils(url,method,json=params)
            return (values[0],'Pass')
        except:
            return (values[0],'Failure')
    else:
        return (values[0],'未运行')


def test_api(e):

    success = fail = none = 0

    # 读取excel数据
    e.read()

    # 开启线程池论询
    start = time.time()
    utils.log_info('开始时间：'+str(datetime.datetime.now()))

    with ThreadPoolExecutor(max_workers=10,thread_name_prefix="network") as executor:
        results = executor.map(func_api,e.data_list)
        for result in results:
            case_result = result[1]
            if case_result == 'Pass':
                success+=1
            elif case_result == 'Failure':
                fail+=1
            else:
                none+=1
            e.write(result[0],case_result)

    end = time.time()
    utils.log_info('结束时间：'+str(datetime.datetime.now()))
    utils.log_info('共计%s个接口，总耗时%s秒'%(len(e.data_list),end-start))
    utils.log_info('Pass：%s个，Failure：%s个，未测试：%s个'%(success,fail,none))
