# coding=utf-8

import os
import re
import json

folder = "C:\\Users\\caofei\\Desktop\\Results\\UserGift\\"
dofolder = "C:\\Users\\caofei\\Desktop\\Results\\UserGoldEnd\\do_"

giftnaemlist = ["子弹", "666", "演员", "游戏手柄碎片", "打CALL", "游戏手柄", "大宝剑碎片", "改名卡", "Excuse me", "帝王套"]
noresulterror = 0
errorGift = 0

count666 = 0
countZD = 0
countYY = 0
countYXSBSP = 0
countDC = 0
countYXSB = 0
countDBJSP = 0
countGMK = 0
countEM = 0
countDWT = 0

# 用户金币流水统计
for root1, dirs1, files1 in os.walk(folder):
    print(files1)
    allgold = 0
    for file in files1:
        if re.match('^\d+\.json', file):
            fileobj = open(folder+file, 'r', encoding='utf-8')
            content = json.load(fileobj)
            # resultfile = open(dofolder+'beginBag.txt', 'ab+')
            gift = content['data']
            # 礼物统计
            giftlength = len(gift)
            for i in range(0, giftlength):
                if gift[i]["name"] == "666":
                    count666 += int(gift[i]["count"])
                elif gift[i]["name"] == "子弹":
                    countZD += int(gift[i]["count"])
                elif gift[i]["name"] == "游戏手柄":
                    countYXSB += int(gift[i]["count"])
                elif gift[i]["name"] == "Excuse me？":
                    countEM += int(gift[i]["count"])
                elif gift[i]["name"] == "打call（30天）":
                    countDC += int(gift[i]["count"])
                elif gift[i]["name"] == "帝王套":
                    countDWT += int(gift[i]["count"])
                elif gift[i]["name"] == "改名卡":
                    countGMK += int(gift[i]["count"])
                elif gift[i]["name"] == "游戏手柄碎片":
                    countYXSBSP += int(gift[i]["count"])
                elif gift[i]["name"] == "大宝剑碎片":
                    countDBJSP += int(gift[i]["count"])
                elif gift[i]["name"] == "演员":
                    countYY += int(gift[i]["count"])
                else:
                    pass

            # allgold += int(content['data']['rich']['gold'])
            # resultfile.write(("gold: " + str(content['data']['rich']['gold']) + '\t\n').encode())
            # resultfile.close()
            # resultfile.write(("gold: " + str(content['data']['rich']['gold']) + '\t\n').encode())
            # resultfile.close()
        else:
            pass
            # resultfile = open(dofolder + 'errorGift.txt', 'ab+')
            # errorGift += 1
            # resultfile.write(("errorGoldBegin: " + str(errorGift) + '\n').encode())
            # resultfile.close()
    # print("#### " + str(allgold))
    print(count666)
    print(countZD)
    print(countYY)
    print(countYXSBSP)
    print(countDC)
    print(countYXSB)
    print(countGMK)
    print(countEM)
    print(countDWT)


