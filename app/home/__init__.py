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

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from sqlalchemy.exc import ProgrammingError

from .. import db

home = Blueprint('home', __name__)

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def execute_sql_file(sql_file_path):
	"""执行sql文件"""

	try:
		f = open(sql_file_path, 'r')
		line = f.read()
		f.close()
		db.session.execute(line)
	except ProgrammingError, e:
		print 'dddd %s' % e


@home.route('/', methods=['GET', 'POST'])
def index():
	try:
		res = db.session.execute('show tables;').fetchall()

		execute_sql_file(os.path.join(basedir, 'public', 'database', 'db_init.sql'))

		return render_template('home/index.html', res=res)
	except TemplateNotFound:
		abort(404)
