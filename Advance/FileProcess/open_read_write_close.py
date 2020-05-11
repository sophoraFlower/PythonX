file1 = open('example.txt', 'w+')
# 写入文件缓存
file1.write("hello a\nhello b")
# 直接读取为空
print(file1.read())
# 写缓存同步到磁盘
file1.close()

file2 = open('example.txt', 'r+')
print(file2.read())


