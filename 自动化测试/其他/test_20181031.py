# coding=utf-8

import os
import re
import json

# file = open("foo.txt", "w")
folder = "C:\\Users\\caofei\\Desktop\\ResultTest\\"
dofolder = "C:\\Users\\caofei\\Desktop\\ResultTest\\do_"

giftnaemlist = ["子弹", "666", "演员", "游戏手柄碎片", "打CALL", "游戏手柄", "大宝剑碎片", "改名卡", "Excuse me", "帝王套"]
uidlist = [111369861, 111369862,
           111369863, 111369864,
           111369865, 111369866,
           111369867, 111369868,
           111369869, 111369870,
           108474802, ]


noresulterror = 0
usererror = 0

# 各用户金币流水统计
for root1, dirs1, files1 in os.walk(folder):
    print(files1)
    for file in files1:
        if re.match('\d{8}-\d{4}_\d+\.json', file):
            fileobj = open(folder+file, 'r', encoding='utf-8')
            content = json.load(fileobj)
            if content['data']['uid'] in uidlist:
                resultfile = open(dofolder+str(content['data']['uid'])+'.txt', 'ab+')
                resultfile.write(("nickname: " + content['data']['nickname'] + '\t').encode())
                resultfile.write(("uid: " + str(content['data']['uid']) + '\t').encode())
                resultfile.write(("account: " + content['data']['account'] + '\t').encode())
                resultfile.write(("gold: " + str(content['data']['rich']['gold']) + '\t\n').encode())
                resultfile.write('------------------------------------------------------------------'.encode())
                resultfile.write('\n\n'.encode())
                resultfile.close()
            else:
                resultfile = open(dofolder + 'usererror.txt', 'ab+')
                usererror += 1
                resultfile.write(("usererror: " + str(usererror) + '\n').encode())
                resultfile.write('------------------------------------------------------------------'.encode())
                resultfile.write('\n\n'.encode())
                resultfile.close()
        else:
            resultfile = open(dofolder + 'noresulterror.txt', 'ab+')
            noresulterror += 1
            resultfile.write(("noresulterror: " + str(noresulterror) + '\n').encode())
            resultfile.write('------------------------------------------------------------------'.encode())
            resultfile.write('\n\n'.encode())
            resultfile.close()


# # 各用户礼物统计
# for root2, dirs2, files2 in os.walk(folder):
#     print(files2)
#     for file in files2:
#         if re.match('d+\.json', file):
#             fileobj = open(folder+file, 'r', encoding='utf-8')
#             content = json.load(fileobj)
#             if content['data']['uid'] in uidlist:
#                 resultfile = open(dofolder+str(content['data']['uid'])+'.txt', 'ab+')
#                 resultfile.write(("nickname: " + content['data']['nickname'] + '\t').encode())
#                 resultfile.write(("uid: " + str(content['data']['uid']) + '\t').encode())
#                 resultfile.write(("account: " + content['data']['account'] + '\t').encode())
#                 resultfile.write(("gold: " + str(content['data']['rich']['gold']) + '\t\n').encode())
#                 resultfile.write('------------------------------------------------------------------'.encode())
#                 resultfile.write('\n\n'.encode())
#                 resultfile.close()
#             else:
#                 resultfile = open(dofolder + 'usererror.txt', 'ab+')
#                 usererror += 1
#                 resultfile.write(("usererror: " + str(usererror) + '\n').encode())
#                 resultfile.write('------------------------------------------------------------------'.encode())
#                 resultfile.write('\n\n'.encode())
#                 resultfile.close()
#         else:
#             resultfile = open(dofolder + 'noresulterror.txt', 'ab+')
#             noresulterror += 1
#             resultfile.write(("noresulterror: " + str(noresulterror) + '\n').encode())
#             resultfile.write('------------------------------------------------------------------'.encode())
#             resultfile.write('\n\n'.encode())
#             resultfile.close()

