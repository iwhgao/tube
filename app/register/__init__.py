#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@version: v1.0.0
@author: deangao 
@license: Apache Licence 
@contact: gaowenhui2012@gmail.com
@site: www.iwhgao.com
@file: __init__.py.py
@time: 2016/10/31 14:26
"""

import sys
import datetime
from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from sqlalchemy.exc import ProgrammingError
from hashlib import md5
from .. import db
from ..config import config

reload(sys)
sys.setdefaultencoding('utf8')
register = Blueprint('register', __name__)


@register.route('/')
def index():
	try:
		return render_template('register/index.html')
	except TemplateNotFound:
		abort(404)


@register.route('/start_register', methods=['POST'])
def start_register():

	try:
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		# 获取表单参数
		pwd = request.form['password']
		email = request.form['email']
		user_code = request.form['username']

		# 创建用户
		m = md5()
		m.update(pwd + config['default'].SECRET_KEY)
		encode_pwd = m.hexdigest()
		cmd = 'INSERT INTO `tube_user`(`user_code`, `user_name`, `group_id`, `password`, `email`, `create_time`, `login_time`, `last_login_time`, `login_times`) VALUES ("%s", "%s", -1, "%s", "%s", "%s", "%s", "%s", 1)' % (
			user_code, user_code, encode_pwd, email, dt, dt, dt)

		db.session.execute(cmd)
	except ProgrammingError, e:
		db.session.rollback()
		return render_template('register/error.html')
	else:
		db.session.commit()
	finally:
		db.session.close()

	# 返回个人主页
	try:
		return redirect(url_for('home.index'))
	except TemplateNotFound:
		abort(404)
