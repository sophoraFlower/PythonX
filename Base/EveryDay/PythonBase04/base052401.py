from collections import *


# name_list = ("houle01", "houle02")
# print(dir(name_list))
#
# # namedtuple
# User = namedtuple("User", ["name", "age"])
# user = User(name="houle", age=28)
# print(user.name, user.age)

# defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(d)  # defaultdict(<class 'list'>, {'default_factory': []})
for k, v in s:
    d[k].append(v)
print(d)  # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
