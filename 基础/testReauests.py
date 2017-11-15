import requests
from bs4 import BeautifulSoup as bs


response_data = requests.get('http://python123.io/ws/demo.html')
html_data = response_data.text

soup = bs(html_data, 'lxml')
print(soup.prettify())

# tag1 = soup.body.contents
# tag2 = soup.body.children
# tag3 = soup.body.descendants

# print(tag1)
# for tag in tag2:
#     print(tag)

# for tag in tag3:
#     print(tag)

tag4 = soup.p
tag5 = tag4.next_siblings
print(tag4)
for tag in tag5:
    print(tag)

