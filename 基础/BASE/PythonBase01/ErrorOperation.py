# coding:utf8
"""
try:
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:
    print("输入不是整数")
else:
    print("AAA")
finally:
    print("输入不确定")

p = pow(-0.5, 0.5)
print(p)

print(len(str(55555)))

input_value = input()
output_value = pow(int(input_value), 0.5)
print("{0:+>30.3f}".format(output_value))

input_value = input()
value_list = input_value.split("-")
print(value_list[0]+"+"+value_list[-1])

"""
# 十进制：一般表示
# 二进制：0b 或 0B 开头
# 八进制：0o 或 0O 开头
# 十六进制：0x 或 0X 开头
# 没有0E开头
"""

print(pow(2, 15))

k = 10000
while k > 1:
    print(k)
    k = k/2

start = 1000
end = 9999
for i in range(start, end+1):
    if pow(int(str(i)[0]), 4) + pow(int(str(i)[1]), 4) + pow(int(str(i)[2]), 4) + pow(int(str(i)[3]), 4) == i:
        print(i)
"""

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


