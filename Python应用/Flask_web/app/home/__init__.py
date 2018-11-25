# coding:utf-8

from flask import Blueprint

# 生成一个蓝图，蓝图名为home
home = Blueprint("home", __name__)

import app.home.views

