
from concurrent.futures import ThreadPoolExecutor
import datetime,time,json
import autotest.utils as utils
import autotest.config as config


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
    msg = '共计测试%s个接口，总耗时%s秒，Pass：%s个，Failure：%s个，未测试：%s个'%(len(e.data_list),end-start,success,fail,none)
    utils.log_info('结束时间：'+str(datetime.datetime.now()))
    utils.log_info(msg)
    send_mail(msg,e.filename)


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_mail(text,filename=None):

    from_user = config.mali_dict['from_user']  # 发件人
    password = config.mali_dict['password']
    to_user = config.mali_dict['to_user']   # 收件人
    subject = config.mali_dict['subject']   # 主题
    server_address = config.mali_dict['server_address']

    # 设置邮件信息
    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = subject
    msg.attach(MIMEText(text,'plain', 'utf-8')) # 添加正文

    # 添加附件
    if filename is not None:
        with open(filename,'rb') as f:
            part_attach = MIMEApplication(f.read())
            part_attach.add_header('Content-Disposition', 'attachment', filename='api-report.xlsx')  # 为附件命名
            msg.attach(part_attach)

    # 发送邮件 SMTP
    server = smtplib.SMTP(server_address,25)
    server.login(from_user,password)
    server.sendmail(from_user,to_user,msg.as_string())
    server.quit()


