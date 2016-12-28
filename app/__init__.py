#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@version: v1.0.0
@author: deangao 
@license: Apache Licence 
@contact: gaowenhui2012@gmail.com
@site: www.iwhgao.com
@file: __init__.py.py
@time: 2016/9/14 22:03
"""

from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    """创建Application"""

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db = SQLAlchemy(app)

    # 欢迎页面
    from .welcome import wlc as welcome_blueprint
    app.register_blueprint(welcome_blueprint, url_prefix='/')

    # 主页面
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/home')

    # 编辑界面
    from .edit import edit as edit_blueprint
    app.register_blueprint(edit_blueprint, url_prefix='/edit')

    # 后台管理页面
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # 用户个人页面
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    # 安装页面
    from .install import install as install_blueprint
    app.register_blueprint(install_blueprint, url_prefix='/install')

    # 注册页面
    from .register import register as register_blueprint
    app.register_blueprint(register_blueprint, url_prefix='/register')

    # 登录页面
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/login')

    return app
