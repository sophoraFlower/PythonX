# coding=utf-8

import os


# 获取当前目录名称
cwd = os.getcwd()
print(cwd)  # C:\Users\caofei\Desktop\Github\PythonPractice\基础\EverQuest\work

# 获得一个文件的绝对路径
abspath = os.path.abspath('base_test_06.py')
print(abspath)  # C:\Users\caofei\Desktop\Github\PythonPractice\基础\EverQuest\work\base_test_06.py

# 检查一个文件或者目录是否存在
print(os.path.exists('base_test_06.py'))  # True
# 检查否是一个目录
print(os.path.isdir('base_test_06.py'))  # False
print(os.path.isdir('C:\\Users\\caofei\\Desktop\\Github'))  # True

# 返回给定目录下的文件列表（以及其它目录）
print(os.listdir('./'))


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk('C:\\Users\\caofei\\Desktop\\Github\\PythonPractice')

# 管道
cmd = 'dir'
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print(stat)  # None 表示正常结束

# 内建函数 repr：接受任意一个对象作为参数，然后返回一个该对象的字符串表示。对于空白符号，它将用反斜杠序列表示
s = '1 2\t 3\n 4'
print(s)  # 1 2	 3 4
print(repr(s))  # '1 2\t 3\n 4'

