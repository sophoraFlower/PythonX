# coding=utf-8


# fin = open('words.txt')
# for line in fin.readlines():
# if len(line.strip()) >= 20:
#     print(line)

# 判断字符串是否不包含e
def has_no_e(li):
    if li.find('e') != -1:
        return False
    return True


def avoids(word, forbid):
    """
        接受一个单词和一个指定禁止使用字符的字符串， 如果单词中不包含任意被禁止的字符，则返回True
    """
    for letter in word:
        if letter in forbid:
            return False
    return True


def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True


def uses_all(word, string):
    for letter in word:
        if letter in string:
            return True
    return False


def is_abecedarian(word):
    string = 'abcdefghijklmnopqrstuvwxyz'
    if string.find(word) != -1:
        return True
    return False


if __name__ == '__main__':
    # 计算百分比
    file_folder = 'words.txt'
    file = open(file_folder)
    m = 0
    n = 0
    result = 0
    while True:
        line = file.readline().strip()
        if line:
            n = n + 1
            if has_no_e(line):
                m = m + 1
            else:
                continue
        else:
            break
    result = m / n
    print(result)

print(avoids('abc', 'ghnghnghngh'))
print(avoids('abc', 'ghnghnghangh'))

print(uses_only('abc', 'abcbccbbbcbbb'))
print(uses_only('abcd', 'abcbccbbbcbbb'))

print(uses_all('ade', 'abcbccbbbcbbb'))
print(uses_all('de', 'abcbccbbbcbbb'))

