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

wlc = Blueprint('welcome', __name__)

@wlc.route('/')
@wlc.route('/index')
def welcome():
	try:
		return render_template('welcome/index.html')
	except TemplateNotFound:
		abort(404)
