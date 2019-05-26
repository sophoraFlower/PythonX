# TempConvert.py
# eval()-评估函数：去掉参数最外侧引号并执行余下语句的函数

"""
TempStr = input("请输入带有符号的温度值: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    # {} 表示槽，后续变量填充在槽中
    # {:.2f}表示将变量C填充到这个位置时取小数点后2位
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
"""

"""
input_Value = input()
outPut_string = "Hello World"
if int(input_Value) == 0:
    print("Hello World")
elif int(input_Value) > 0:
    for i in range(len(outPut_string)//2+1):
        print(outPut_string[i*2:(i+1)*2])
elif int(input_Value) < 0:
    for i in outPut_string:
        print(i)
else:
    print("input error")
"""

input_Value = input()
OP_index = 0
for i in range(len(input_Value)):
    while input_Value == "+" or input_Value == "-" or input_Value == "*" or input_Value == "/":
        if i == 0:
            continue
        else:
            OP_index = i
M_value = input_Value[0:OP_index].strip()
OP_value = input_Value[OP_index]
N_value = input_Value[OP_index+1:].strip()
print("{:.2f}".format(eval((M_value+OP_value+N_value))))



