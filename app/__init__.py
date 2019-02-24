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
from	bson.json_util import dumps
import	itertools
import	unidecode
import	re
from	functools import wraps
# from   threading import Thread
import	urllib2
import	uuid

import inspect

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
### FLASK-ADMIN IMPORT 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# from	flask_admin 	import Admin, AdminIndexView
# from 	flask_admin.model import typefmt
# from 	flask_admin.model.widgets import XEditableWidget

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CRYPTO IMPORT 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

import  bcrypt
import	jwt



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
# import 	pymongo
# from 	pymongo import MongoClient
# from 	pymongo import UpdateOne



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
### LOGIN MANAGER 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# from  	flask_login import 	LoginManager, login_user, logout_user, login_required, \
# 							current_user

# ### create login manager
# login_manager 						= LoginManager()
# login_manager.init_app(app)
# login_manager.login_view 	= 'login'


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CSRF 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# deprecated --> messing with form.validate_on_submit()
# csrf = CSRFProtect(app)
# csrf.init_app(app)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### EMAILING IMPORTS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### TO DO : password forgotten 

from	flask_mail import Mail, Message

### set flask-email after config
mail 	= Mail(app)



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
### CREATE ADMIN MANAGER VIEWS 
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
# cf : https://github.com/flask-admin/flask-admin/blob/master/examples/pymongo/app.py


# admin = Admin(	app, 
# 				index_view=views.MyAdminIndexView(), 
# 				name='back office',
# 				# template_mode="bootstrap2"
# 				)

# # Add views in admin interface
# admin.add_view( views.UserViewAdmin( mongo_users, 		'Users' ) )
# admin.add_view( views.FeedbackAdmin( mongo_feedbacks, 	'Feedbacks' ) )
# admin.add_view( 
# 	views.ReferencedProjectCarrierFeedback(
# 		mongo_join_message_referenced_project_carrier, 
# 		u"Porteurs de projets référencés"
# 	) 
# )
# admin.add_view( 
# 	views.NotReferencedProjectCarrierFeedback(
# 		mongo_join_message_not_referenced_project_carrier,
# 		u"Porteurs de projets non-référencés"
# 	)
# )
# admin.add_view( views.StructuresFeedback( mongo_join_message_structures, u"Structures" ) )



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

print
log_app.debug(">>> all imports are finished...\n")