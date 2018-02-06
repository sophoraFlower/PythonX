# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

reportPath = os.path.join(os.getcwd(), 'testReports')  # 测试报告的路径

print("打印路径：")

print(reportPath)


class SendMail(object):

    # 该函数的作用是为了在测试报告的路径下找到最新的测试报告
    def get_report(self):
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname  # 返回的是测试报告的名字

    # 该函数的目的是为了准备发送邮件的的消息内容
    def take_messages(self):
        newreport = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '战旗TV接口自动化测试报告'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:

            # 读取测试报告的内容
            mailbody = f.read()

        # 将测试报告的内容放在 邮件的正文当中
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')

        # 将html附加在msg里
        self.msg.attach(html)

        # html附件 > 下面是将测试报告放在附件中发送
        att1 = MIMEText(mailbody, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'

        # 这里的filename可以任意写，写什么名字，附件的名字就是什么
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):

        # recipients = ['xxxx@xxxx.com', 'xxxx@qq.com', 'xxx@xxxxx.com']  # 发送给多个人
        recipients = ['caofei@bianfeng.com']
        self.take_messages()

        # 发送邮件的人，这种是公司邮箱转发
        self.msg['from'] = 'caofei@bianfeng.com'

        # 收件人和发送人必须这里定义一下，执行才不会报错。
        self.msg['to'] = recipients
        toaddrs = recipients

        smtp = smtplib.SMTP()
        smtp.connect('smtp.xxxx.com')
        smtp.ehlo()
        smtp.login('caofei@xxxx.com', 'xxxxx')
        # 发送邮件
        smtp.sendmail(self.msg['from'], toaddrs, self.msg.as_string())
        smtp.close()
        print('send mail success!')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()