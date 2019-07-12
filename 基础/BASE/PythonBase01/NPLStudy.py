import re


def parse(text):

    # 去除所有的标点符号和换行符
    text = re.sub(r'[^\w]', ' ', text)

    # 大写变小写
    text = text.lower()

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


with open(r"..\..\SOS\txt\in.txt", "r") as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write("{} {}\n".format(word, freq))


attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']]

# expected outout:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

list1 = [dict(zip(attributes, v)) for v in values]
print(list1)

