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

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

install = Blueprint('install', __name__)


@install.route('/')
def index():

	#need_modules = ['', some]
	install_modules = {}

	try:
		try:
			import MySQLdb
			install_modules.update({'MySQLdb':True})
		except ImportError:
			pass

		return render_template('install/index.html', modules=install_modules)
	except TemplateNotFound:
		abort(404)
