"""
name = input('your name:')
gender = input('you are a boy?(y/n)')

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {'prefix': 'Mr.' if gender == 'y' else 'Mrs', 'name': name}
print('authorizing...')
print(welcome_str.format(**welcome_dic))
"""

"""
import re


def parse(text):
    text = re.sub(r'[^\w ]', ' ', text)
    # 转为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    # 去除空白单词
    word_list = filter(None, word_list)
    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))
"""

import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)

print(repr(data))
print(json_str)

data2 = json.loads(json_str)
print(data2["no"], data2["name"], data2["url"])
