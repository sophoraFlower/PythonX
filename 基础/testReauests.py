import requests
import time

# response = requests.get('https://www.zhanqi.tv/api/actives/dbqb/rank')
response = requests.get('https://www.zhanqi.tv/api/actives/qna/top')

content = response.json()
cornNums = content['data']
cornNumAll = 0
for i in range(10):
    # cornNumAll += int(cornNums[0]['cornNum'])
    cornNumAll += int(cornNums['list'][0]['star'])

print(cornNumAll)

time.sleep(3)





