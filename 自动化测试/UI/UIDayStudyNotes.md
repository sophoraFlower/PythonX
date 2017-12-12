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



- 利用id定位元素

  ```python
  find_element_by_id()
  ```




### UI_2017/12/12


- 通过tag name来定位元素

  ```python
  find_element_by_tag_name()
  ```

-  利用link text定位元素

  ```
  find_element_by_link_text()
  ```

- 利用partial link text来定位页面元素

  ```
  find_element_by_partial_link_text()
  ```

- 利用元素节点中class name的值、name属性来定位页面元素

  ```
  find_element_by_class_name()
  find_element_by_name()
  ```

- 利用css定位元素

  ```
  find_element_by_css_selector()
  ```

- **小结：**一定要掌握好XPath或者css来定位元素，其他的几种了解就可以。毕竟在实际项目开发脚本阶段，很多元素是无法通过id ,css, text, name来直接定位这个网页元素，更多的还是根据XPath或者css表达式去定位

- **常用方法：**

  -  send_keys()：输入字符串到文本输入框这样的页面元素
  - click()：点击页面上支持点击的元素
  - clear()：清除文本
  - refresh()：刷新页面

- ​