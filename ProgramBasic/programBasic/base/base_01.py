li = [3, 5, 1, 6, 12]
tup = (3, 5, 1, 6, 12)

print(li[-1])
print(tup[-1])

print(li[2:3])
print(tup[2:3])

print(li.count(3))
print(tup.count(3))

print(li.index(5))
print(tup.index(5))

li.reverse()
print(li)
li.sort()
print(li)

# reversed()返回一个倒转后的迭代器
print(list(reversed(li)))
print(list(reversed(tup)))

# 注意整体倒转和倒序的区别
print(sorted(li))
print(sorted(tup))

li_1 = []
tup_1 = ()
print(li_1.__sizeof__())  # 40
print(tup_1.__sizeof__())  # 24

li_1.append(1)
tup_1 = tup_1 + (1,)
print(li_1.__sizeof__())  # 40+32=72
print(tup_1.__sizeof__())  # 24+8=32

li_1.append(2)
tup_1 = tup_1 + (2,)
print(li_1.__sizeof__())  # 40+32=72
print(tup_1.__sizeof__())  # 32+8=40

li_1.append(3)
li_1.append(4)
li_1.append(5)
print(li_1.__sizeof__())  # 40+32+32=104

