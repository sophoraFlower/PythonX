# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# from email.mime.image import MIMEImage
from email.utils import formataddr

reportPath = os.path.join(os.getcwd(), 'testReports')
print(reportPath)


class SendMail(object):

    def __init__(self):
        self.dirs = os.listdir(reportPath)
        self.dirs.sort()
        self.new_report_name = self.dirs[-1]
        self.new_report = self.get_report()
        self.sender = 'zhanqitv2017@sina.com'
        self.receivers = 'caofei@bianfeng.com'
        self.msg = MIMEMultipart('alternative')

    def get_report(self):
        print('The new report name: {0}'.format(self.new_report_name))
        return self.new_report_name

    def take_msgs(self):

        # 邮件正文内容
        self.msg['From'] = formataddr(["Test Group", self.sender])
        self.msg['To'] = formataddr(["Project member", self.receivers])
        self.msg['Subject'] = Header("PC端线上接口测试报告").encode()
        mail_body = '<html><body><h2>接口自动化测试报告</h2><p>&nbsp&nbsp详情见附件</p></body></html>'
        html_content = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        self.msg.attach(html_content)

        # html附件
        with open(os.path.join(reportPath, self.new_report_name), 'r', encoding='utf-8') as f:
            mail_file = f.read()
            f.close()
        att_content = MIMEText(mail_file, 'base64', 'utf-8')
        att_content["Content-Type"] = 'application/octet-stream'
        att_content["Content-Disposition"] = 'attachment; filename="PC_online_api_test_report.html"'
        self.msg.attach(att_content)

    def send(self):
        try:
            self.take_msgs()
            server = smtplib.SMTP_SSL('smtp.sina.com', '465')
            server.starttls()
            server.connect('smtp.sina.com', '465')
            server.set_debuglevel(1)
            server.login('zhanqitv2017@sina.com', '2017@zhanqiTV')
            server.sendmail(self.sender, [self.receivers, ], self.msg.as_string())
            time.sleep(5)
            server.quit()
            print('send mail success!')
        except smtplib.SMTPException as e:
            print("Error: %s" % e)
