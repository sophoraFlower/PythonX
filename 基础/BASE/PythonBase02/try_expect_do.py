"""
# Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常。

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    print(num1+num2)

except ValueError as err:
    print('Value Error: {}'.format(err))
except TypeError as err:
    print('Type Error: {}'.format(err))
except Exception as err:
    print('Other Error: {}'.format(err))


print('continue！')

"""

"""
# finally block 中的语句都会被执行，即使try和except block中使用了return语句
import sys
try:
    f = open('file.txt', 'r')
    # some data processing
except OSError as err:
    print('OS Error: {}'.format(err))
except:
    print('Unexcepted error: {}'.format(sys.exc_info()[0]))
finally:
    f.close()
"""


# 自定义异常类型
class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的 string 表达形式
        return "{} is invalid input".format(repr(self.value))


try:
    raise MyInputError(666)  # 抛出 MyInputError 这个异常
except MyInputError as err:
    print('error: {}'.format(err))





