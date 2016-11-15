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

admin = Blueprint('admin', __name__)


@admin.route('/')
def show():
	try:
		return render_template('admin/index.html')
	except TemplateNotFound:
		abort(404)
