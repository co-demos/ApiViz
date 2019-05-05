# -*- encoding: utf-8 -*-

"""
wsgi file to run app in production mode from gunicorn
"""

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ['FLASK_CONFIGURATION'] = "production"
os.environ['MONGODB_MODE'] = "server"
os.environ['DOCKER_MODE'] = "docker_off"

from backend import app, log_app


if __name__ == '__main__':
	""" 
	runner for the CIS front Flask app 
	- warning : gets most of its variables at start from environment variables

	in command line just type : 
	"python wsgi.py"
	or
	"gunicorn --bind 0.0.0.0:8100 --workers=1 wsgi:app" for instance

	"""

	# set environment variable to set config later in config_app.config_env.py

	print "= "*25
	print "= = = WSGI / RERUN FLASK APP = = ="
	log_app.info
	print "= "*25

	# simple flask runner
	app.run()