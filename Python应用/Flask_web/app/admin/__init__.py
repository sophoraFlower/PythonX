# coding:utf-8

from flask import Blueprint

# 生成一个蓝图，蓝图名为admin
admin = Blueprint("admin", __name__)

import app.admin.views
