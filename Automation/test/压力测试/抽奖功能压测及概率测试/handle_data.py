# coding=utf-8

import os
import re
import json

basefolder = "C:\\Users\\caofei\\Desktop\\Results\\"


# 读取文件:*.json、*.unknow
def read_file(folder):
    for root, dirs, files in os.walk(folder):
        return files


# 金币统计
def gold_count(files, stage, pattern):
    gold = 0
    for file in files:
        if re.match(pattern, file):
            fileobj = open(basefolder+stage+'\\'+file, 'r', encoding='utf-8')
            content = json.load(fileobj)
            gold += int(content['data']['rich']['gold'])
        else:
            pass
    return gold


# 背包统计
def bag_count(files, stage, pattern):

    bags = {"子弹": 0, "666": 0, "演员": 0,
            "游戏手柄碎片": 0, "打CALL": 0, "游戏手柄": 0,
            "大宝剑碎片": 0, "改名卡": 0, "Excuse me": 0, "帝王套": 0, }
    for file in files:
        if re.match(pattern, file):
            fileobj = open(basefolder + stage + '\\' + file, 'r', encoding='utf-8')
            content = json.load(fileobj)
            # 背包礼物汇总
            contentlist = content['data']["gift"] + content['data']["prop"] + content['data']["interact"]
            for i in range(0, len(contentlist)):
                if contentlist[i]["name"] == "666":
                    bags["666"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "子弹":
                    bags["子弹"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "游戏手柄":
                    bags["游戏手柄"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "Excuse me？":
                    bags["Excuse me"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "打call（30天）":
                    bags["打CALL"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "帝王套":
                    bags["帝王套"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "改名卡（30天）":
                    bags["改名卡"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "游戏手柄碎片":
                    bags["游戏手柄碎片"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "大宝剑碎片":
                    bags["大宝剑碎片"] += int(contentlist[i]["total"])
                elif contentlist[i]["name"] == "二哈":
                    bags["演员"] += int(contentlist[i]["total"])
                else:
                    pass
        else:
            pass
    return bags


# 福袋处理
def fuku_count(files, stage, pattern):

    bags = {"子弹": 0, "666": 0, "演员": 0,
            "游戏手柄碎片": 0, "打CALL": 0, "游戏手柄": 0,
            "大宝剑碎片": 0, "改名卡": 0, "Excuse me": 0, "帝王套": 0, }
    for file in files:
        if re.match(pattern, file):
            fileobj = open(basefolder + stage + '\\' + file, 'r', encoding='utf-8')
            content = json.load(fileobj)
            # 福袋抽一次
            contentlist = content['data']
            for i in range(0, len(contentlist)):
                if contentlist[i]["name"] == "666":
                    bags["666"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "子弹":
                    bags["子弹"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "游戏手柄":
                    bags["游戏手柄"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "Excuse me":
                    bags["Excuse me"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "打CALL":
                    bags["打CALL"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "帝王套":
                    bags["帝王套"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "改名卡":
                    bags["改名卡"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "游戏手柄碎片":
                    bags["游戏手柄碎片"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "大宝剑碎片":
                    bags["大宝剑碎片"] += int(contentlist[i]["count"])
                elif contentlist[i]["name"] == "演员":
                    bags["演员"] += int(contentlist[i]["count"])
                else:
                    pass
        else:
            pass
    return bags


if __name__ == '__main__':
    # 金币统计-开始
    dofilebegingold = read_file(basefolder+'UserGoldBegin')
    allgold_a = gold_count(dofilebegingold, 'UserGoldBegin', '^A-\d+\.json')
    allgold_b = gold_count(dofilebegingold, 'UserGoldBegin', '^B-\d+\.json')
    allgold_c = gold_count(dofilebegingold, 'UserGoldBegin', '^C-\d+\.json')
    begingold = open(basefolder + 'begingold.txt', 'ab+')
    begingold.write(("GoldBeginCount: " + str(allgold_a) + '\n').encode())
    begingold.write(("GoldBeginCount: " + str(allgold_b) + '\n').encode())
    begingold.write(("GoldBeginCount: " + str(allgold_c) + '\n').encode())
    begingold.close()
    # 金币统计-结束
    dofileendgold = read_file(basefolder + 'UserGoldEnd')
    allgold_ae = gold_count(dofileendgold, 'UserGoldEnd', '^A-\d+\.json')
    allgold_be = gold_count(dofileendgold, 'UserGoldEnd', '^B-\d+\.json')
    allgold_ce = gold_count(dofileendgold, 'UserGoldEnd', '^C-\d+\.json')
    goldcount = open(basefolder + 'Endgold.txt', 'ab+')
    goldcount.write(("GoldEndnCount: " + str(allgold_ae) + '\n').encode())
    goldcount.write(("GoldEndCount: " + str(allgold_be) + '\n').encode())
    goldcount.write(("GoldEndCount: " + str(allgold_ce) + '\n').encode())
    goldcount.close()

    # 背包统计-开始
    dofilebagbegin = read_file(basefolder + 'UserBagBegin')
    allrich_a = bag_count(dofilebagbegin, 'UserBagBegin', '^A-\d+\.json')
    allrich_b = bag_count(dofilebagbegin, 'UserBagBegin', '^B-\d+\.json')
    beginrich = open(basefolder + 'beginrich.txt', 'ab+')
    beginrich.write(("richBeginCount: " + str(allrich_a) + '\n').encode())
    beginrich.write(("richBeginCount: " + str(allrich_b) + '\n').encode())
    beginrich.close()
    # 背包统计-结束
    dofilebagend = read_file(basefolder + 'UserBagEnd')
    allrich_ae = bag_count(dofilebagend, 'UserBagEnd', '^A-\d+\.json')
    allrich_be = bag_count(dofilebagend, 'UserBagEnd', '^B-\d+\.json')
    endrich = open(basefolder + 'endrich.txt', 'ab+')
    endrich.write(("RichEndnCount: " + str(allrich_ae) + '\n').encode())
    endrich.write(("RichEndCount: " + str(allrich_be) + '\n').encode())
    endrich.close()

    # 福袋结果处理
    dofileGift = read_file(basefolder + 'UserGift')
    allgift = fuku_count(dofileGift, 'UserGift', '^\d+\.json')
    allgiftfile = open(basefolder + 'gift.txt', 'ab+')
    allgiftfile.write(("GiftCount: " + str(allgift) + '\n').encode())
    allgiftfile.close()


