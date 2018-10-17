import os
import sys


# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0,parentdir)
#
# print(parentdir)

print(os.getcwd())
print(os.path.abspath(''))
print(os.path.abspath('.'))

# print(os.path.split(os.getcwd()))
# print(os.path.split(os.path.abspath('')))
print(os.path.split(os.path.abspath('.')))

print(os.path.dirname(os.getcwd()))
print(os.path.dirname(os.path.abspath('')))
print(os.path.dirname(os.path.abspath('.')))

print(os.path.getctime(os.path.abspath('')))
print(os.path.getmtime(os.path.abspath('')))

