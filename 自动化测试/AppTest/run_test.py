# coding: utf-8

import time
import sys
import unittest
from base.HTMLTestRunner import HTMLTestRunner

sys.path.append('./testCases')

test_case_dir = './testCases'
suite = unittest.defaultTestLoader.discover(test_case_dir, pattern='*_test.py')

if __name__ == '__main__':
    now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    HtmlFile = './testReports/' + now_time + '_result.html'
    fp = open(HtmlFile, 'wb')
    runner = HTMLTestRunner(
                            stream=fp,
                            title=u'移动端-Android-版本自动化测试报告',
                            description=u'测试数据统计',
                            verbosity=2
                            )
    runner.run(suite)
    fp.close()

