# coding:utf-8
from . import home


@home.route("/")  # 配置home的特定路由
def index():
    return "<h1 style='color:green'>this is home</h1>"
