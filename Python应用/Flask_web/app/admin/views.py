# coding:utf-8
from . import admin


@admin.route("/")  # 配置admin的特定路由
def index():
    return "<h1 style='color:red'>this is admin</h1>"
