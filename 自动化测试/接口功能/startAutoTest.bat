@echo off 

color 0a
title HTTP接口自动化测试

set path=%cd%
@echo 请清理旧日志
del %path%\logs\*
@echo 请清理旧测试报告
del %path%\testReports\*

cd %path%
run_tests.py 

@echo Test End!
pause>nul



