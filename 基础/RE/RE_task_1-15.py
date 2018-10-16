# coding=utf-8
import re

"""1-1 识别后续的字符串：“bat”、“bit”、“but”、“hat”、“hit”或者“hut”。"""
patt1 = 'bat|bit|but|hat|hut|hit'  # '[b|h][u|a|i]t'、'[bh][uia]t'
re.search(patt1, 'bbtbithit').group()  # hit
print(re.findall(patt1, 'bat sad bit ad but d fa hat adfad hit ad da d hut aa hdt'))
print(re.findall('[b|h][u|a|i]t', 'bat sad bit ad but d fa hat adfad hit ad da d hut aa hdt'))
print(re.findall('[bh][uia]t', 'bat sad bit ad but d fa hat adfad hit ad da d hut aa hdt'))

"""1-2 匹配由单个空格分隔的任意单词对，也就是姓和名"""
patt2 = '[a-zA-Z0-9]+\s[a-zA-Z0-9]+'  # '\w+\s\w+'
print(re.match(patt2, 'Tom Dan').group())  # Tom Dan

"""1-3 匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母"""
patt3 = '\w+,\s\w+'
print(re.match(patt3, 'T, Dan').group())  # T, Dan

"""1-4 匹配所有有效 Python 标识符的集合"""
patt4 = '[_A-Za-z]+[_\w]+'  # 有效Python标识符：以下划线和字母开头的非空字符
print(re.match(patt4, '__Number9').group())  # __Number9

"""1-5 根据读者当地的格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数
量的街道单词，包括类型名称）。例如，美国街道地址使用如下格式：1180 Bordeaux 
Drive。使你的正则表达式足够灵活，以支持多单词的街道名称，如 3120 De la Cruz 
Boulevar"""
patt5 = '[0-9]+[\s[a-zA-Z]+]*'  # r'\d+.+'
print(re.match(patt5, '1180 Bordeaux Drive').group())  # 1180 Bordeaux Drive

"""1-6 匹配以“www”起始且以“.com”结尾的简单 Web 域名；例如，www://www. yahoo.com/。
选做题：你的正则表达式也可以支持其他高级域名，如.edu、.net 等（例如，
http://www.foothill.edu）"""
patt6 = '^http://www\.[\w+\.]+[a-zA-Z]+$'
print(re.match(patt6, 'http://www.foothill.aa.edu').group())  # http://www.foothill.aa.edu

"""1-7 匹配所有能够表示 Python 整数的字符串集"""
intSet = ['-0x260', '10', '100', '15.20', '-.6545+0J', '-786', '080', '-0490', '0x69', '51924361L', '0xDEFABCECBFBAEl']
patt7 = '([-|+]?[0x]?[0-9]+$)'
for item in intSet:
    print(re.search(patt7, item))

"""1-8 匹配所有能够表示 Python 长整数的字符串集"""
longSet = ['51924361L', '-0x19323L', '0122L', '0xDEFABCECBDAECBFBAEl', '535633629843L', '-052318172735L']
patt8 = '([-|+]?(0x)?[0-9A-Z]+[l|L]$)'
for item in longSet:
    print(re.search(patt8, item))

"""1-9 匹配所有能够表示 Python 浮点数的字符串集"""
floatSet = ['0.0', '15.20', '-21.9', '32.3+e18', '-90.0', '-32.54e100', '70.2-E12']
patt9 = '([+|-]?[0-9]+\.[0-9]+[+|-]?[e|E]?([0-9]+)?)'
for item in floatSet:
    print(re.search(patt9, item))

"""1-10 匹配所有能够表示 Python 复数的字符串集"""
complexSet = ['3.14j', '45j', '9.322e-36j', '.876j', '.6545+0J', '3e+26J', '4.53e-7j']
patt10 = '([0-9]+)?(\.)?([0-9]+)?(e)?[+|-]?([0-9]+)?[j|J]?'
for item in complexSet:
    print(re.search(patt10, item))

"""1-11 匹配所有能够表示有效电子邮件地址的集合（从一个宽松的正则表达式开始，然
后尝试使它尽可能严谨，不过要保持正确的功能"""
emailSet = ['2268228773@qq.com', 'zjdxm@sina.cn', 'houle.cf@foxmail.com', 'houle_cf@126.com', 'houle.cf@gmail.com',
            'caofei@bianfeng.com', 'caofei@jlu.edu.cn']
patt11 = '([0-9]+)?([a-zA-Z_\.]+)?@([0-9a-zA-Z\.].+)?'  # '.+@.+'
for item in emailSet:
    print(re.search(patt11, item))

"""1-12 匹配所有能够表示有效的网站地址的集合（URL）（从一个宽松的正则表达式开始，
然后尝试使它尽可能严谨，不过要保持正确的功能）"""
webSet = ['www.zhanqi.tv', 'www.sougou.com', 'www.jlu.edu.cn', 'pintia.cn', 'www.houle.tech']
patt12 = '(w{3}|\w+)?(\.\w+)+'
for item in webSet:
    print(re.search(patt12, item))

"""1-13 type()。内置函数 type()返回一个类型对象，如下所示，该对象将表示为一个 Pythonic
类型的字符串
        >>> type(0)
        <type 'int'>
        >>> type(.34)
        <type 'float'>
        >>> type(dir)
        <type 'builtin_function_or_method'>
创建一个能够从字符串中提取实际类型名称的正则表达式。函数将对类似于<type
'int' >的字符串返回 int（其他类型也是如此，如 'float' 、'builtin_function_or_method' 等）。
注意：你所实现的值将存入类和一些内置类型的__name__属性中"""
typeSet = [6, 3.1415, 9.322e-36j, 'hello', dir]
patt13 = r'class\s(\'\w+\')'
for item in typeSet:
    print(re.search(patt13, str(type(item))).group(1))

"""1-14 处理日期。1.2 节提供了来匹配单个或者两个数字字符串的正则表达式模式，来表示 1～
9 的月份(0?[1-9])。创建一个正则表达式来表示标准日历中剩余三个月的数字"""
monthSet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
patt14 = '[1][0-2]'  # '[0]?[1-9]'、'[1][0-2]'
for item in monthSet:
    print(re.search(patt14, str(item)))


"""1-15 处理信用卡号码。1.2 节还提供了一个能够匹配信用卡（CC）号码([0-9]{15,16})
的正则表达式模式。然而，该模式不允许使用连字符来分割数字块。创建一个允
许使用连字符的正则表达式，但是仅能用于正确的位置。例如，15 位的信用卡号
码使用 4-6-5 的模式，表明 4 个数字-连字符-6 个数字-连字符-5 个数字；16 位的
信用卡号码使用 4-4-4-4 的模式。记住，要对整个字符串进行合适的分组。选做题：
有一个判断信用卡号码是否有效的标准算法。编写一些代码，这些代码不但能够
识别具有正确格式的号码，而且能够识别有效的信用卡号码"""
cradSet = ['4444-666666-55555', '4444-4444-4444-4444', '333-666666-55555', '4444444444444444']
patt15 = '([0-9]{4}[-]?[0-9]{6}[-]?[0-9]{5})?(([0-9]{4})([-]?[0-9]{4}){3})?'  # '([0-9]{15,16})'
for item in cradSet:
    print(re.search(patt15, item))
