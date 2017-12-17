#### 备忘

&emsp;&emsp;Web UI自动化测试目前看不太适合战旗TV（PC页面）的测试，效率较低，维护成本高

​        截图验证？Dom节点？核心、稳定的业务功能（发送弹幕、老虎机、金币流水、推荐位是否未直播等）

&emsp;&emsp;Pycharm出现激活验证的话，关闭，在hosts中加下面代码，屏蔽掉Pycharm对激活码的验证

```
0.0.0.0 account.jetbrains.com
```

#### 依赖库

- chromedriver.exe（chrome浏览器驱动）放置路径：D:\Program Files\Python36

-  unittest

- selenium

- 安装：参考Python库安装

  -  示例

    ```dos
    pip install selenium
    ```

#### 专门的一套自动化测试账号（战旗，第三方等）

#### 执行顺序

- ```python
   sign_out_UItest.py：执行开始和结束各执行一次
   ```
  ```


- ```python
  sign_out_UItest.py > thirdParty_sign_on_by_wb_UItest.py > send_barrage_by_hotWord_UItest.py > sign_out_UItest.py
  ```

#### 公共方法（待完成，计划中）> 模块化

- 清除cookie
- 退出浏览器
- 获取cookie
- 简易登录
- 悬停，点击
- 页面刷新
- 单双击、表单填充
- 测试用例耦合度低
- 元素是否存在




#### 应用计划（战旗）

-  战旗任务日常
- 直播间签到
- 商城 > 道具 > 兑换“10打call礼包”（当战旗币大于8000）
- 个人中心（战旗币、子弹、金币、关注主播、直播状态、浏览记录（清空））
- 发送弹幕（特定弹幕）
- 自动化执行

####  任务分解

-  战旗任务日常