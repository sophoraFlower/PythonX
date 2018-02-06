import requests

response = requests.get('https://www.zhanqi.tv/api/actives/dbqb/rank')
content = response.json()
cornNums = content['data']
cornNumAll = 0
for i in range(30):
    cornNumAll += int(cornNums[0]['cornNum'])

print(cornNumAll)





