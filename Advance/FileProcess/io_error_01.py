"""
    OSError: [Errno 23] Too many open files in system: 'example.txt'
"""

list_files = []
for i in range(8000):
    list_files.append(open('example.txt', 'w'))
    print("{}, {}".format(i, list_files[i].fileno()))
