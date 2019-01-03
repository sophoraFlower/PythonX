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
  -  click()：点击页面上支持点击的元素
  -  clear()：清除文本
  -  refresh()：刷新页面



### UI_2017/12/26


- 浏览器前进和回退

  ```python
  # 回退
  driver.back()
  # 前景
  driver.forward()
  ```

- 浏览器版本号

  ```python
  driver.capabilities['version']
  ```

- 当前页面内容

  ```python
  # 当前页面url
  drive.current_url
  # 当前页面title
  driver.title
  ```

- 模拟键盘操作（FireFox）

  ```python
  # 在浏览器中新开一个tab（标签页）
  from selenium.webdriver.common.keys import Keys  

  driver.get("http://www.baidu.com/")  
  # ctrl+t
  driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  
  ```

- 自定义浏览器窗口大小

  ```python
  # 全屏
  driver.maximize_window()           
  # 分辨率 1280*800 
  driver.set_window_size(1280,800)   
  # 获取当前窗口大小
  driver.get_window_size()
  ```

-  断言

  ```python
  try:  
      assert u"百度一下" in driver.title  
      print ('Assertion test pass.')  
  except Exception as e:  
      print ('Assertion test fail.', format(e)) 
  ```

-  综合-常用

  ```python
  # 获取页面元素大小
  element.size
  """按键操作"""
  # 首先要导入：
  from selenium.webdriver.common.keys import Keys  #需要引入keys包
  # 1.通过定位密码框，enter（回车）来代替登陆按钮
  driver.find_element_by_id("user_pwd").send_keys(Keys.ENTER)
  # 2.ctrl+a 全选输入框内容
  driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
  # 3.刷新页面
  driver.refresh()
  # 4.下拉页面(相当于滑动下拉框到底部)
  driver.find_element_by_id("kw").send_keys(Keys.PageDown)
  # 5.通过键盘和鼠标操作实现将指定的图片鼠标右键下载保存图片操作
  # 使用selenium模拟鼠标和键盘操作:将鼠标放置图像上方，点击鼠标右键，然后键盘按V就可以保存了，核心代码如下：
  from selenium.webdriver.common.action_chains import ActionChains 
  from selenium.webdriver.common.keys import Keys
  # 移动到该元素
  action = ActionChains(driver).move_to_element(element)
  # 右键点击该元素
  action.context_click(element)
  # 点击键盘向下箭头
  action.send_keys(Keys.ARROW_DOWN)
  # 键盘输入V保存图
  action.send_keys('v')
  # 执行保存
  action.perform()
  ```

- 执行js语句

  ```python
  # 用目标元素参考去拖动
  target_elem = driver.find_element_by_link_text("地区")
  driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
  ```

- 多窗口切换

  ```Python
  # 当前窗口句柄
  driver.current_window_handle
  # 当前全部窗口句柄集合
  driver.window_handles
  ```

- iframe切换

  ```Python
  # 利用switch_to.frame('iframeid')方法来切换到具体的iframe，然后才能去操作目标元素
  ```

- 处理Alert弹窗

  ```Python
  # selenium1
  driver.execute_script("window.alert('这是一个测试Alert弹窗');")  
  time.sleep(2)  
  driver.switch_to_alert().accept()  # 点击弹出里面的确定按钮  
  #driver.switch_to_alert().dismiss() # 点击弹出上面的X按钮 
  ```