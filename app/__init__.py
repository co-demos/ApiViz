# -*- encoding: utf-8 -*-


"""
front app du Carrefour des Innovations Sociales : 
-------------------------------------------------
version : 0.1
-------------------------------------------------
- framework back 	: flask
- landing page 		: pure html + Bulma
- logged pages 		: Vue.js ?

"""


print
print "__init__ / global imports for functions"


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### GLOBAL IMPORTS  
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  os
from    os import environ
import	time, datetime
from	datetime import timedelta
from 	datetime import date
import	json
from 	pprint import pprint, pformat
from	bson import json_util
from	bson.objectid import ObjectId
import	re
from	functools import wraps


# ### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# ### SET LOGGER 
# ### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from config_app.config_logging import log_app
log_app.debug('>>> TESTING LOGGER')

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FLASK IMPORTS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask 			import Flask, g, current_app, session, request
from 	flask_wtf.csrf 	import CSRFProtect
# from	flask import jsonify, flash, render_template, url_for, make_response, request, redirect

import  socket

try : 
	host_IP = socket.gethostbyname( socket.gethostname() )
	log_app.info( ">>> host IP : %s " , host_IP )
except: 
	log_app.error(">>> no IP host detected")




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SCHEDULER IMPORT  
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### no need for now 
# from flask_apscheduler import APScheduler
# from flask_apscheduler.auth import HTTPBasicAuth



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### MONGO DB IMPORTS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from	flask_pymongo import PyMongo ### flask_pymongo instead of flask.ext.pymongo




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### SETTINGS AT MAIN LEVEL 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### create Flask app 
app		= Flask( __name__ )

### FOR DEBUGGING PURPOSES
### LOG / PRINT HEADERS
@app.before_request
def before_request():
	
	print
	print "+ - "*25

	log_app.debug( '/// NEW REQUEST /// ' )

	### print headers
	# log_app.debug( '/// REQUEST HEADERS : \n %s ', request.headers )
	### NOTE BUG : 
	### SAFARI HEADERS DON'T CONTAIN COOKIE, THEREFORE NOR CSRF VALUE
	


### set environment and app variables
log_app.debug(">>> configuring app's env vars...\n")

from .config_app import app_metas
from .config_app.config_env import * 

configure_app(app)

if config_name == "default" or config_name == "production" or config_name == "testing"  :
	log_app.info('>>> config_name : %s \n', config_name )
	log_app.info(	">>> ENVIRONMENT VARIABLES / to understand what the fuck is goin on ... : \n %s \n", 
		pformat({ k : v for k,v in  os.environ.iteritems() }) )
	log_app.info(	">>> APP.CONFIG / to understand what the fucking fuck is goin on ... : \n %s \n", 
		pformat({ k : v for k,v in  app.config.iteritems() }) )
print



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CSRF 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# deprecated --> messing with form.validate_on_submit()
# csrf = CSRFProtect(app)
# csrf.init_app(app)




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INITIATE MONGO DB AND IMPORT MAIN CLASSES 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# settings classes : global variable for app
from 	settings 	import *
log_app.info(">>> LIST_PARTNERS : \n %s", pformat(LIST_PARTNERS) )

# utils 
from 	utils		import *

# models :
from 	models 	import *

# set Anonymous user class
# login_manager.anonymous_user = AnonymousUser

# forms classes :
from forms import * # LoginForm, UserRegisterForm, UserUpdateForm, UserHistoryAloesForm, RequestCabForm


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### INITIATE MONGO DB 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# db classes and functions
from api import *


reboot_datetime = datetime.datetime.now().strftime("%Y-%m-%d-h%H-m%M-s%S")
# backup_mongo_collection(mongo_users,	 cwd + "/app/_backups_collections/backup_coll_users-"+reboot_datetime +".json")
# backup_mongo_collection(mongo_feedbacks, cwd + "/app/_backups_collections/backup_coll_feedbacks-"+reboot_datetime +".json")



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### IMPORT VIEWS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

from . import views



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

print
log_app.debug(">>> all imports are finished...\n")