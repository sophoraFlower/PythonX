# coding:utf-8

from flask import Flask
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from flask import render_template

app = Flask(__name__)
app.debug = True

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
print(app.url_map)


# 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
