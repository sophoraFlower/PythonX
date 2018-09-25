# !/usr/bin/env python
# coding: utf-8

import unittest
from ygn_test import MainTest
from HTMLTestRunner import HTMLTestRunner
from base.mail import Email


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MainTest))
    # tests = [MainTest("test_adoff"), MainTest("test_center"), MainTest("test_search"), MainTest("test_login")]
    # suite.addTests(tests)
    # with open('HTMLReport.html', 'w', encoding='utf-8') as f:  # 用例同目录下生成执行报告
    filename = "D:/Java/uiautotest/case/HTMLReport.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
                            stream=fp,
                            title='自动化测试报告',
                            description='用例执行情况：',
                            verbosity=2
                            )
    runner.run(suite)

    # e = Email(
    #           title='ZQ-Android自动化测试报告',
    #           message='各位好，这是今天的测试报告,请同浏览器打开附件查看！有问题请及时联系，谢谢！',
    #           receiver='2835230597@qq.com',
    #           cc='yangguoning@bianfeng.com',
    #           server='smtp.qq.com',
    #           sender='1373742590@qq.com',
    #           password='osfnmpxljucvgdba',
    #           path="D:/Java/uiautotest/case/HTMLReport.html"
    #           )
    # e.send()
