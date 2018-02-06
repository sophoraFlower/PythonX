@echo off  
C:  
cd C:\Users\caofei\Desktop\TestFrameDebug
del C:\Users\caofei\Desktop\TestFrameDebug\logs\*
del C:\Users\caofei\Desktop\TestFrameDebug\testReports\*

start python run_tests.py 
# start python run_tests.py 10
exit 