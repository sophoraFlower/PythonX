@echo off 

color 0a
title HTTP�ӿ��Զ�������

set path=%cd%
@echo ���������־
del %path%\logs\*
@echo ������ɲ��Ա���
del %path%\testReports\*

cd %path%
run_tests.py 

@echo Test End!
pause>nul



