#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
@version: v1.0.0
@author: deangao 
@license: Apache Licence 
@contact: gaowenhui2012@gmail.com
@site: www.iwhgao.com
@file: __init__.py.py
@time: 2016/10/31 14:22
"""

from flask import Blueprint, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
from sqlalchemy.exc import ProgrammingError
from hashlib import md5
from .. import db
from ..config import config

auth = Blueprint('auth', __name__)


@auth.route('/')
@auth.route('/index')
def index():
    try:
        return render_template('auth/index.html')
    except TemplateNotFound:
        abort(404)
        
        
@auth.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']

    m = md5()
    m.update(password + config['default'].SECRET_KEY)
    encode_pwd = m.hexdigest()

    cmd = "SELECT COUNT(1) FROM `tube_user` WHERE `user_code`='{0}' AND `password`='{1}'".format(username, encode_pwd)
    try:
        res = db.session.execute(cmd)
        rows = res.fetchall()
    except Exception, e:
        db.session.rollback()
    finally:
        db.session.close()

    if rows[0][0] == 1:
        return redirect(url_for('home.index'))
    else:
        return redirect(url_for('auth.index'))


