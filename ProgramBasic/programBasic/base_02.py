import time

d1 = {'name': 'hole', 'age': 18, 'gender': 'male'}
d2 = dict({'name': 'hole', 'age': 18, 'gender': 'male'})
d3 = dict([('name', 'hole'), ('age', 20), ('gender', 'male')])
d4 = dict(name='myo', age=22, gender='female')
print(d1 == d2)  # True

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)  # True

print(d4.get('name'))
print(d4.get('lastname', 'default_name'))

print(2 in s2)  # True

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])  # 根据字典值的升序排序
print(d_sorted_by_key)  # [('a', 2), ('b', 1), ('c', 10)]
print(d_sorted_by_value)  # [('b', 1), ('a', 2), ('c', 10)]


def find_unique_price_using_list(products_):
    unique_price_list = []
    for _, price_ in products_:  # A
        if price not in unique_price_list:  # B
            unique_price_list.append(price_)
    return len(unique_price_list)


def find_unique_price_using_set(products_):
    unique_price_set = set()
    for _, price_ in products_:
        unique_price_set.add(price_)
    return len(unique_price_set)


id_ = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id_, price))
# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
# time elapse using list: 56.651887877
print("time elapse using list: {}".format(end_using_list - start_using_list))

# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
# time elapse using set: 0.009517312999996363
print("time elapse using set: {}".format(end_using_set - start_using_set))
