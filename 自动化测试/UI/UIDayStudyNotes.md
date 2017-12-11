### UI_2017/12/11

-  XPath工具：firepath、firebug

- Firefox版本选择

- Flash版本过低

- code1:

  ```python
  # selenium的page_source方法可以获取到页面源码，结合python的re模块用正则表达式爬出页面上的所以url等
  # coding:utf-8
  from selenium import webdriver
  import re
  driver = webdriver.Firefox()
  driver.get("http://www.cnblogs.com/yoyoketang/")
  page = driver.page_source
  # print page
  # "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
  url_list = re.findall('href=\"(.*?)\"', page, re.S)
  url_all = []
  for url in url_list:
      if "http" in url:
          print url
          url_all.append(url)
  # 最终的url集合
  print url_all
  ```



- 理由id定位元素

  ```
  find_element_by_id()
  ```

  ​