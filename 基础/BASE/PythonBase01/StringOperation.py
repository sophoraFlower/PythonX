# coding:utf8

TestStr = "abC123^%JJ%%fgh"
print(TestStr[3])
print(TestStr[5:-1])
print(TestStr[:-2])
print(TestStr[1:-1:2])
print(TestStr[::-1])

print("abc\ndef")

print("abc"+" def")
print("abc"*3)
if "a" in "abc":
    print("'a' is in 'abc'")

'''
WeekInput = input()  # WeekInput = eval(input())
WeekOptions = "星期一星期二星期三星期四星期五星期六星期日"
print(WeekOptions[(int(WeekInput)-1)*3:(int(WeekInput))*3])
'''

print(len(TestStr))
print(str(1.23))
print(hex(8))  # 十六进制
print(oct(8))  # 八进制
print(ord("A"))  # 单字符 > Unicode
print(chr(65))  # Unicode > 单字符

# 星座展示
for i in range(12):
    print(chr(9800+i), end=" ")

print("\n")
print(TestStr.lower())
print(TestStr.upper())
print(TestStr.split(","))
print(TestStr.count("C"))

print(TestStr.replace("b", "B"))
print(TestStr.center(30, "-"))

print(TestStr.strip("agh="))
print("-".join("123456789"))

print("{}:计算机{}的CPU占用率为{}%".format("2018-10-10", "C", 10))
print("{2}:计算机{1}的CPU占用率为{0}%".format("2018-10-10", "C", 10))
print("{0:=^20}".format("PYTHON"))  # 居中对齐
print("{0:=>20}".format("PYTHON"))  # 右对齐
print("{0:=<20}".format("PYTHON"))  # 左对齐
print("{:10}".format("BIT"))
print("{:=<20.8}".format("0.00006"))
