# -*- coding: utf-8 -*-
import os


class Config:
	def __init__(self):
		pass

	SECRET_KEY = 'hard to guess string'
	SSL_DISABLE = False
	DEBUG = True
	FLASK_ADMIN = 'gaowenhui2009@aliyun.com'

	MYSQL_HOST = 'localhost'
	MYSQL_PORT = 3306
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = ''
	MYSQL_DB = 'tube'

	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)
	SQLALCHEMY_TRACK_MODIFICATIONS = True

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
	'default': ProductionConfig
}
