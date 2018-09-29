# coding=utf-8

import os

'2018-01-05 13:35:49.239941'
filePath = 'C:\\Users\\caofei\\Desktop\\screenshots\\'
for parent, dirs, files in os.walk(filePath):
    fileSize = 0
    for file in files:
        currentPath = os.path.join(parent, file)
        newFileSize = int(str(os.path.getsize(currentPath))[0:3])
        if newFileSize != fileSize:
            localTimeDay = str(file)[0:4] + '-' + str(file)[4:6] + '-' + str(file)[6:8]
            localTimeHour = str(file)[8:10] + ':' + str(file)[10:12] + ':' + str(file)[12:14]
            localTime = localTimeDay + ' ' + localTimeHour
            with open(filePath + 'result.txt', "a+") as f:
                print(localTime)
        else:
            pass
        fileSize = newFileSize




