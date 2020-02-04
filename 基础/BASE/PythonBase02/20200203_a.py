"""
tuple1 = (1, 2, 3)
a1 = (4,)
tuple2 = tuple1 + a1
print(tuple2)
tuple3 = reversed(tuple2)
print(tuple3)
list3 = list(tuple3)
print(list3)
list3.sort()
print(list3)

l1 = [1, 2, 3]
t1 = (1, 2, 3)
print(l1.__sizeof__())
print(t1.__sizeof__())
"""

"""
d1 = {'name': 'cao', 'age': 28, 'gender': 'male'}
d2 = dict({'name': 'cao', 'age': 28, 'gender': 'male'})
d3 = dict([('name', 'cao'), ('age', 28), ('gender', 'male')])
d4 = dict(name='cao', age=28, gender='male')
if d1 == d2 == d3 == d4:
    print('ture')

s1 = {1, 2, 3}
s2 = set([1, 2, 3, 4])
print(s1)
print(s2)
"""

# 创建，查找，增加，删除，更新，排序
"""
d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])
print(d_sorted_by_key)
print(d_sorted_by_value)
"""


