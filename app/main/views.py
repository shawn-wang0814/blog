# 主业务中的视图和路由的定义

from flask import render_template, json
from . import main
from .. import db
from ..models import *

# 主页的访问路径
@main.route('/')
def main_index():
    categories = Category.query.all()

    return render_template('index.html',params=locals())

# 登录页面的访问路径
@main.route('/login')
def login_views():
    return render_template('login.html')

# 注册页面的访问路径
@main.route('/register')
def register_views():
    return render_template('register.html')