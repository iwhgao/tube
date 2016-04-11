#!/usr/bin/python
# -*- coding: utf8 -*-

# ===============================
# Author: deangao
# Email: gaowenhui2012@gmail.com
# Create Date: 
# ===============================


from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
