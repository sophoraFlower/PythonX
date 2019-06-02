import time
from appium import webdriver

capabilities = dict()
capabilities['platformName'] = 'Android'
capabilities['platformVersion'] = '9.0'
capabilities['deviceName'] = 'ONEPLUS A5010'
capabilities['udid'] = '4f37087f'
capabilities['appPackage'] = 'com.zhihu.android'
capabilities['appActivity'] = 'com.zhihu.android.app.ui.activity.MainActivity'
capabilities['unicodeKeyboard'] = 'True'
capabilities['resetKeyboard'] = 'True'
capabilities['noReset'] = 'True'
capabilities['noSign'] = 'True'
# 连接测试机所在服务器服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
time.sleep(6)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                             'android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.widget.HorizontalScrollView/android.widget.LinearLayout/'
                             'android.support.v7.app.a.c[5]').click()
time.sleep(0.5)

for i in range(826):

    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[6]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                                 'android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/'
                                 'android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]').click()
    time.sleep(1)
    driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                                  'android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.view.ViewGroup/'
                                  'android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/'
                                  'android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View')[0].click()
    time.sleep(1)
    driver.press_keycode(4)
    time.sleep(0.5)
    driver.press_keycode(4)

time.sleep(6)
# 断开连接
driver.quit()
