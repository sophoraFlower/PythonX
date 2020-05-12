# coding:utf-8
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1

    @task()
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        # 定义requests的请求头
        header = {"User-Agent": "Zhanqi.tv Api Client", "Zhanqi-Mobile": "Zhanqi.tv"}
        r = self.client.post("/api/auth/user.login",
                         {"account": "15068890000", "password": "test666","os": 0, "geetest_ver": 3.0, "platform": 1},
                         timeout=30,
                         headers=header)

        # 这里可以使用assert断言请求是否正确
        assert r.status_code == 200

    @task(2)
    def index(self):
        self.client.get("/api/user/user.info")

    @task(1)
    def profile(self):
        self.client.get("/api/user/record.watch_list")


# 这个类设置性能测试，继承HttpLocus
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'http://beta.zhanqi.tv'
    min_wait = 5000
    max_wait = 9000

