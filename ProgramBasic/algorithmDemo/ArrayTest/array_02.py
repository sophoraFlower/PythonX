from array import *

x = array('f', [1.0, 2.0, 5.0, 6.5, 7.0])

for i in x:
    print(i)

print("---------")

y = array('i', [1, 11, 22, 33, 44, 55])

print("数组内容如下：")
for i in y:
    print(i)

m = eval(input("请输入欲插入的索引："))
n = eval(input("请输入欲插入的数值："))
if 5 < m < 0:
    print("输入错误")
else:
    y.insert(m, n)
for i in y:
    print(i)
