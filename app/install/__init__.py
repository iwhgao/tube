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
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

install = Blueprint('install', __name__)

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def check_is_installed():
	"""检测是否存在install.lock文件"""

	if os.path.exists(os.path.join(basedir, 'public', 'install.lock')):
		return True
	return False


@install.route('/')
@install.route('/index')
def index():

	#need_modules = ['', some]
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
			install_modules.update({'MySQLdb':True})
		except ImportError:
			install_modules.update({'MySQLdb':False})
			pass

		try:
			import MySQL
			install_modules.update({'MySQL':True})
		except ImportError:
			install_modules.update({'MySQL':False})
			pass

		return render_template('install/index.html', modules=install_modules)

	except TemplateNotFound:
		abort(404)


def install_step1():
	"""创建表"""
	pass


def install_step2():
	"""创建超级用户"""
	pass


def install_step3():
	"""创建install.lock文件"""

	f = open(os.path.join(basedir, 'public', 'install.lock'), 'w')
	f.close()


@install.route('/start_install', methods=['POST'])
def installing():
	"""逐步安装"""

	try:
		install_step1()
		install_step2()
		install_step3()
	except Exception, e:
		return render_template('install/error.html', errors=e)

	#print request.form
	return render_template('install/start_install.html', install_info=None)
