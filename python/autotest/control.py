
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
            return (values,'Pass')
        except:
            return (values,'Failure')
    else:
        return (values,'未运行')


def test_api(e):

    success = fail = none = 0

    test_msg = ''

    # 读取excel数据
    e.read()

    # 开启线程池论询
    start = time.time()
    utils.log_info('开始时间：'+str(datetime.datetime.now()))

    with ThreadPoolExecutor(max_workers=10,thread_name_prefix="network") as executor:
        results = executor.map(func_api,e.data_list)
        for result in results:
            values = result[0]
            case_result = result[1]
            if case_result == 'Pass':
                success+=1
            elif case_result == 'Failure':
                fail+=1
                test_msg = test_msg + set_font('16px','red',values[2]+' --> '+case_result)
            else:
                none+=1
                test_msg = test_msg + set_font('16px','orange',values[2]+' --> '+case_result)
            e.write(values[0],case_result)

    end = time.time()
    utils.log_info('结束时间：'+str(datetime.datetime.now()))

    test_time = '共计测试%s个接口，总耗时%s秒'%(len(e.data_list),end-start)
    test_count = 'Pass：%s个，Failure：%s个，未测试：%s个'%(success,fail,none)
    utils.log_info(test_time)
    utils.log_info(test_count)

    # 发送邮件
    test_time = set_font('20px','black',test_time)
    test_count = set_font('20px','black',test_count)
    send_mail(test_time+test_count+test_msg,e.filename)


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

'''

    MUA：Mail User Agent——邮件用户代理，就是电子邮件软件，比如Outlook
    MTA：Mail Transfer Agent——邮件传输代理，就是Email服务提供商，比如163邮箱
    MDA：Mail Delivery Agent——邮件投递代理

邮件发送流程：
    发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
    编写MUA把邮件发到MTA，编写MUA从MDA上收邮件
    发邮件时，MUA和MTA使用的协议：SMTP
    收邮件时，MUA和MDA使用的协议：POP3、IMAP4

多人收件
    1、收件人邮箱 ['abc@163.com','dhsjkbsh@qq.com','123463255@qq.com']，以列表的方式给出
    2、msg['To'] =','.join（msg_to）
    3、s.sendmail(msg_from, msg['To'].split(','), msg.as_string())
    
'''

def set_font(size,color,text):
   return '<p style="font-size:%s;color:%s">%s</p>'%(size,color,text)


def send_mail(text,filename=None):

    from_user = config.mali_dict['from_user']  # 发件人
    password = config.mali_dict['password']
    to_user = config.mali_dict['to_user']   # 收件人
    subject = config.mali_dict['subject']   # 主题
    server_address = config.mali_dict['server_address']

    # 设置邮件信息
    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = ','.join(to_user)
    msg['Subject'] = subject
    msg.attach(MIMEText(text,'html', 'utf-8')) # 添加正文

    # 添加附件
    if filename is not None:
        with open(filename,'rb') as f:
            part_attach = MIMEApplication(f.read())
            part_attach.add_header('Content-Disposition', 'attachment', filename='api-report.xlsx')  # 为附件命名
            msg.attach(part_attach)

    # 发送邮件 SMTP
    server = smtplib.SMTP(server_address,25)
    server.login(from_user,password)
    server.sendmail(from_user, msg['To'].split(','),msg.as_string())
    server.quit()


