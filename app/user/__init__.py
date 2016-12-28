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

user = Blueprint('user', __name__)


@user.route('/')
def show():
	try:
		return render_template('user/index.html')
	except TemplateNotFound:
		abort(404)
