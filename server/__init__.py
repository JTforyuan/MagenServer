#! /usr/env/bin python
# -*- coding:utf-8 -*-

from flask import *
from werkzeug.utils import import_string

blueprints = ['server.main_bp:main_bp']

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)
	
	for bp_name in blueprints:
		bp = import_string(bp_name)
		
		# 参数为蓝图对象
		app.register_blueprint(bp)
	
	return app

