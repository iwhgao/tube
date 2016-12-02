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

import os
import sys
import datetime
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from sqlalchemy.exc import ProgrammingError
from hashlib import md5
from .. import db
from ..config import config

reload(sys)
sys.setdefaultencoding('utf8')

install = Blueprint('install', __name__)

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def execute_sql_file(sql_file_path):
	"""执行sql文件"""

	try:
		f = open(sql_file_path, 'r')
		line = f.read()
		f.close()
		db.session.execute(line)
		db.session.commit()
	except ProgrammingError, e:
		db.session.rollback()
	finally:
		db.session.close()


def check_is_installed():
	"""检测是否存在install.lock文件"""

	if os.path.exists(os.path.join(basedir, 'public', 'install.lock')):
		return True
	return False


@install.route('/')
@install.route('/index')
def index():
	# need_modules = ['', some]
	install_modules = {}

	try:
		# 检测是否已经存在安装锁定文件
		is_installed = check_is_installed()

		if is_installed:
			return render_template('install/check_install.html')

		# 安装步骤页面
		try:
			# TODO： 检测各版本是否准确安装
			import MySQLdb
			install_modules.update({'MySQLdb': True})
		except ImportError:
			install_modules.update({'MySQLdb': False})
			pass

		try:
			import MySQL
			install_modules.update({'MySQL': True})
		except ImportError:
			install_modules.update({'MySQL': False})
			pass

		return render_template('install/index.html', modules=install_modules)

	except TemplateNotFound:
		abort(404)


def install_step1():
	"""创建表"""
	execute_sql_file(os.path.join(basedir, 'public', 'database', 'db_init.sql'))


def install_step2(pwd, email):
	"""创建超级用户"""

	# 检查是否是第一次插入
	cmd = 'SELECT COUNT(*) FROM `tube_group` WHERE `parent_group_id`=-1'
	res = db.session.execute(cmd).fetchall()

	if res[0][0] != 0:
		db.session.close()
		raise Exception('已经安装过了!!!')

	try:
		# 创建组
		dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		cmd = 'INSERT INTO `tube_group`(`parent_group_id`, `group_name`, `group_description`, `create_time`) VALUES (%d, "%s", "%s", "%s");' % (
			0, 'admin', 'admin', dt)
		db.session.execute(cmd)
		db.session.commit()

		# 创建用户
		m = md5()
		m.update(pwd + config['default'].SECRET_KEY)
		encode_pwd = m.hexdigest()
		cmd = 'INSERT INTO `tube_user`(`user_code`, `user_name`, `group_id`, `password`, `email`, `create_time`, `login_time`, `last_login_time`, `login_times`) VALUES ("superadmin", "%s", 1, "%s", "%s", "%s", "%s", 1)' % (
			"超级管理员", email, encode_pwd, dt, dt, dt)
		db.session.execute(cmd)
		db.session.commit()

	except ProgrammingError, e:
		db.session.rollback()
	finally:
		db.session.close()


def install_step3():
	"""创建install.lock文件"""

	f = open(os.path.join(basedir, 'public', 'install.lock'), 'w')
	f.close()


@install.route('/start_install', methods=['POST'])
def installing():
	"""逐步安装"""

	try:
		install_step1()
		install_step2(request.form['super_password'], request.form['email'])
		install_step3()
	except Exception, e:
		return render_template('install/error.html', errors=e)

	# print request.form
	return render_template('install/start_install.html', install_info=None)
