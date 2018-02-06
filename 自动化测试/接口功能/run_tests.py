import time
import sys
from HTMLTestRunner import HTMLTestRunner
# from commentClass.SendEmail import SendMail
import unittest
sys.path.append('./testCase')


# 指定测试用例为当前文件夹下的testCase目录
test_dir = './testCase'
suite = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = './testReports/' + now + '_result.html'
    fp = open(HtmlFile, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"PC端线上接口自动化测试报告",
                            description=u"测试数据统计")
    runner.run(suite)
    fp.close()

    # 测试结束之后，执行邮件发送报告
    # sendMail = SendMail()
    # sendMail.send()



