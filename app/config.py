# -*- coding: utf-8 -*-
import os


class Config:
	def __init__(self):
		pass

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SSL_DISABLE = False
	DEBUG = True
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	MYSQL_HOST = 'localhost'
	MYSQL_PORT = 3306
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = ''
	MYSQL_DB = 'tube'

	@staticmethod
	def init_app(app):
		pass


class ProductionConfig(Config):
	def __init__(self):
		pass

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)


config = {
	'FLASK_ADMIN': 'gaowenhui2009@aliyun.com',
	'default': ProductionConfig
}
