#!/usr/bin/env python
# -*- encoding: utf-8 -*-

### good encoding of flash messages
### cf : https://stackoverflow.com/questions/8924014/how-to-handle-my-unicodedecodeerror
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

### import all from app.__init__
from . 	import *
from		flask 	import 	jsonify, flash, render_template, \
									url_for, make_response, request, redirect, \
									send_file

# from 	werkzeug.security 	import 	generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### AUTH - TOKEN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

########################################################################################
# Access token ### from prettyprinted youtube channel
"""
def token_required(f):
	@wraps(f)
	def decorated( *args, **kwargs ):

		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return jsonify({'message' : 'Token is missing!'}), 401

		try:
			data 			= jwt.decode(token, app.config['SECRET_KEY'])
			current_user 	= User.query.filter_by(public_id=data['public_id']).first()

		except:
			return jsonify({'message' : 'Token is invalid!'}), 401

		return f(current_user, *args, **kwargs)

	return decorated
"""


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ERRORS HANDLERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
@app.route("/error/<int:err_code>", defaults={ "error": BadRequest })
def errorHandler(error, err_code=400):
	
	if err_code == 404 : #  | error.code == 404 : 
		error_code 	= 404
		template 		= "errors/404.html" 

	elif err_code == 403 : # | error.code == 403 : 
		error_code 	= 403
		template 		= "errors/403.html" 

	elif err_code == 500 : # | error.code == 500 : 
		error_code 	= 500
		template 		= "errors/500.html" 

	else : 
		error_code 	= 400
		template 		= "errors/400.html" 

	app_config = getDocuments(mongo_config_global)

	return render_template( 
		template,
		config_name			= config_name, # prod or default...
		site_section		= "error",
		error_code			= str(error_code),
		app_metas				= app_metas,
		app_config 			= app_config,
		language				= "fr" ,

		languages_dict	= app_languages_dict ,
		# error_msg				= u"accès interdit",
		# user_infos			= current_user.get_public_infos
	), error_code




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CONFIG ROUTES - BACKEND API
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

def DocOidToString(data):
	# log_app.debug("data : %s", data) 
	obj = {}
	for key in data:
		if isinstance(data[key], ObjectId):
			obj[key] = str(data[key])
		else:
			obj[key] = data[key]
	# log_app.debug("obj : %s", obj) 
	return obj

def getDocuments(collection, query={}, oid_to_id=True, as_list=False, field="field") : 
	
	### query collection and transform as list
	results = list(collection.find(query) ) 
	# log_app.debug("config app route / results - 1 : \n%s", pformat(results) )

	### ObjectId to string
	if oid_to_id : 
		results = [ DocOidToString(i) for i in results ]
		# log_app.debug("config app route / results - 2 : \n%s", pformat(results) )

	### list to dict
	if as_list == False : 
		results = { i[field] : i for i in results }
		# log_app.debug("config app route / results - 3 : \n%s", pformat(results) )

	return results

def checkJWT(token, url_check="http://localhost:4100/api/auth/tokens/confirm_access"):
	### TO DO 
	return True


@app.route('/backend/api/config/<string:collection>/<string:doc_id>', methods=['GET','POST','DELETE'])
@app.route('/backend/api/config/<string:collection>', methods=['GET'], defaults={"doc_id" : None})
@app.route('/backend/api/config', methods=['GET'], defaults={'collection': 'global', "doc_id" : None})
def config_global(collection, doc_id=None):
	"""
	Main route to GET and POST/PUT/DELETE
	choices 	: global | endpoints | styles | routes
	variables : <collection> and <doc_id>
	arguments : as_list (bool), field (str)
	example 	: http://localhost:8100/backend/api/config?as_list=true
	"""

	log_app.debug("config app route")
	log_app.debug("config app route / collection : %s", collection )
	log_app.debug("config app route / doc_id : %s", doc_id )

	### target right config collection 
	if collection in ["global" , "endpoints" , "styles" , "routes" ] : 
		mongoColl = mongoConfigColls[collection] ### imported from . (and from there from .api.__init__ )
	else : 
		log_app.warning("error : -%s- is not a valid config collection (redirect)", collection)
		return redirect( "/error/400" )

	### get request args if any 
	as_list = request.args.get('as_list', default=False, 		type=bool)
	field 	= request.args.get('field', 	default="field", 	type=str)
	token 	= request.args.get('token', 	default=None, 		type=str)
	log_app.debug("config app route / as_list : %s", as_list )

	### build query if any 
	query = {}
	if doc_id : 
		query = {"_id" : ObjectId(doc_id)}

	### check if token allows user to POST
	if token :
  		is_authorized = checkJWT(token)

	### TO DO 
	if request.method == 'POST':
		if is_authorized : 
			return "hello config master / POST ... praise be"
		else : 
			return "noooope"

	elif request.method == 'DELETE':
		if is_authorized : 
			return "hello config master / DELETE ... praise be"
		else : 
			return "noooope"


	elif request.method == 'GET':

		app_config_dict = getDocuments(mongoColl, query=query, as_list=as_list, field=field)

		return jsonify( {
				"msg" 				: "this is the results from your query on the '%s' config collection" % collection,
				"query"				: query,
				"request"			: {
					"url" 				: request.url,
					"args" 				: request.args, 
					"method"			: request.method,
					"collection"	: collection,
					"doc_id"			: doc_id,
				},
				"app_config" 	: app_config_dict
		} )




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CLIENT ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

@app.route('/', methods=['GET'])
@app.route('/home/<string:lang>', methods=['GET'])
@app.route('/home', methods=['GET'], defaults={"lang":"en"})
def home(lang="fr"):

	log_app.debug("entering new home page")

	app_config = getDocuments(mongo_config_global)
	log_app.debug("app_config :/n%s", pformat(app_config))

	if lang == "fr" : 
		template = "new-home.html"
	else : 
		template = "new-home-english.html"

	return render_template(
		template,
		config_name		= config_name, # prod, testing, default...
		app_config 		= app_config,
		app_metas			= app_metas,
		language			= lang,
	)


@app.route('/tools/<string:lang>', methods=['GET'])
@app.route('/tools', methods=['GET'], defaults={"lang":"en"})
def Tools(lang="en"):

	log_app.debug("entering tools page")
	app_config = getDocuments(mongo_config_global)

	if lang == "fr" : 
		template = "les-outils.html"
	else : 
		template = "les-outils-english.html"

	return render_template(
		template,
		config_name		= config_name, # prod, testing, default...
		app_metas			= app_metas, 
		app_config 		= app_config,
		language			= lang
	)

@app.route('/app/', methods=['GET','POST'],defaults={'path': ''})
@app.route('/app/<path:path>', methods=['GET','POST'])
def spa(path):

	log_app.debug("entering SPA page")
	app_config = getDocuments(mongo_config_global)

	return render_template(
		"spa.html",
		config_name		= config_name, # prod, testing, default...
		app_config 		= app_config,
		app_metas			= app_metas,
		language			= "fr"
	)


# @app.route('/contact', methods=['GET'])
# def contact():

# 	form = FeedbackForm()

# 	log_app.debug("entering contact page")

# 	return render_template(
# 		"contact.html",
# 		config_name		= config_name, # prod, testing, default...
# 		app_metas			= app_metas,
# 		language			= "fr",
# 		form 					= form
# 	)


ANTI_SPAM_FIELD_NAME = "userMiddlename"


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### LOGIN/LOGOUT/REGISTER ROUTES - USING FLASK-LOGIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# cf : https://runningcodes.net/flask-login-and-mongodb/
# cf : https://medium.com/@dmitryrastorguev/basic-user-authentication-login-for-flask-using-mongoengine-and-wtforms-922e64ef87fe
# cf : https://www.youtube.com/watch?v=NYWEf9bZhHQ&t=320s - flask-login and flask-admin


# from models import User, AnonymousUser

# @login_manager.user_loader
# def load_user(userEmail):
# 	"""
# 	populates the current_user flask_login object
# 	"""

# 	log_app.debug("userEmail : %s", userEmail)

# 	user = mongo_users.find_one({ "userEmail" : userEmail })
# 	# user = mongo_users.find_one({ "_id" : ObjectId(userOID) })

# 	if not user :

# 		log_app.debug( "no user found in db" )

# 		# return None
# 		return AnonymousUser()

# 	else :

# 		log_app.debug( "user : \n %s", pformat(user)  )
# 		log_app.debug( "user['_id'] : %s", str(user["_id"]) )

# 		user_ = User( )
# 		user_.populate_from_dict(dict_input=user)

# 		### adds forgotten OID into current_user
# 		user_.userOID = str(user["_id"])

# 		return user_



# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	"""
# 	main page for login
# 	backed on flask-login classes
# 	"""
#
# 	form = LoginForm()
#
# 	if request.method == 'POST' :
#
# 		log_app.debug("login / reading form ... " )
# 		for f_field in form :
# 			log_app.info( "form name : %s / form data : %s \n", f_field.name, f_field.data )
#
#
# 		if form.validate_on_submit():
#
# 			user = mongo_users.find_one({"userEmail": form.userEmail.data})
# 			log_app.info("user - type : %s - : %s", type(user), pformat(user) )
#
# 			if user and User.validate_login( user['userPassword'], form.userPassword.data ):
#
# 				log_app.debug("user found + User.validate_login ")
#
# 				user_obj = User()
# 				user_obj.populate_from_dict(dict_input=user)
#
# 				### login with flask-login
# 				login_user( user_obj, remember=form.userRememberMe.data )
#
# 				### update login_last_at in db
# 				user["login_last_at"] 	= datetime.datetime.now()
# 				user["logins_total"]	= user["logins_total"] + 1
# 				mongo_users.save(user)
#
# 				log_app.info("Logged in successfully")
#
# 				# flash(u"Vous êtes bien connecté.e", category='light')
#
# 				return redirect(request.args.get("next") or url_for("home"))
#
# 			else :
#
# 				log_app.error("password was not validated / form.errors : %s", form.errors )
#
# 				flash(u"Email ou mot de passe incorrect(s)", category='warning')
#
# 				return redirect(url_for("login"))
#
# 		else :
#
# 			log_app.error("form was not validated / form.errors : %s", form.errors )
#
# 			flash(u"Email ou mot de passe incorrect(s)", category='warning')
#
# 			return redirect(url_for("login"))
#
#
# 	elif request.method == 'GET' :
#
# 		return render_template(	'login.html',
#
# 								config_name		= config_name, # prod or default...
# 								app_metas		= app_metas,
# 								language		= "fr" ,
# 								languages_dict	= app_languages_dict ,
#
# 								site_section	= 'login',
# 								form			= form,
# 								user_infos		= current_user.get_public_infos
#
# 								)



# POST verb is disabled until a proper solution against spam is found
# @app.route('/register', methods=['GET', 'POST'])
# @app.route('/register', methods=['GET'])
# def register():
#
# 	form = RegisterForm()
#
# 	if request.method == 'POST':
#
# 		print
# 		log_app.info("posting a new user \n")
#
# 		# for debugging purposes
# 		for f_field in form :
# 			log_app.debug( "form name : %s / form data : %s ", f_field.name, f_field.data )
#
#
# 		if form.validate_on_submit():
#
# 			# capitalize name and surname
# 			form.userName.data 		= form.userName.data.capitalize()
# 			form.userSurname.data 	= form.userSurname.data.capitalize()
#
# 			existing_user = mongo_users.find_one({"userEmail" : form.userEmail.data} )
#
# 			log_app.debug("existing_user : %s", pformat(existing_user) )
#
#
# 			if existing_user is None :
# 				is_new_user = "create_new_user"
# 			else :
# 				if existing_user["userAuthLevel"] == "visitor" :
# 					is_new_user = "update_visitor_to_user"
# 				else :
# 					is_new_user = "no"
# 					flash(u"Cet email est déjà utilisé, veuillez réessayer", category='warning')
# 					return redirect(url_for('register'))
#
# 			log_app.warning("is_new_user : %s", is_new_user )
#
# 			# if existing_user is None or existing_user["userAuthLevel"] == "visitor" :
# 			if is_new_user != "no" :
#
# 				# create hashpassword
# 				hashpass = generate_password_hash(form.registerPassword.data, method='sha256')
# 				log_app.debug("hashpass : %s", hashpass )
#
# 				# populate user class
# 				new_user 	= User( 	userPassword=hashpass,
# 										userAuthLevel="user",
# 										login_last_at=datetime.datetime.now(),
# 										logins_total=1
# 										 )
# 				new_user.populate_from_form(form=form)
# 				new_user.add_created_at()
#
# 				# check if user declared being from a partner and set 'verified_as_partner' as 'VERIFY
# 				new_user.check_if_user_structure_is_partner()
#
#
# 				if is_new_user == "create_new_user":
# 					# save user in db --> function from ModelMixin
# 					log_app.warning("inserting new_user in mongo_users" )
# 					new_user.insert_to_mongo( coll=mongo_users )
#
# 				# else : # equivalent to <--
# 				if is_new_user == "update_visitor_to_user" :
# 					# update visitor to user in db --> function from ModelMixin
# 					log_app.warning("updating new_user in mongo_users" )
# 					new_user.update_document_in_mongo( document=existing_user,  coll=mongo_users )
#
#
# 				# logout previous user if any
# 				logout_user()
#
# 				# log user with flask-login
# 				login_user(new_user)
#
#
#
#
# 				flash(u"Votre compte a bien été créé", category='success')
#
# 				return redirect(url_for('home'))
#
# 		else :
#
# 			log_app.error("form was not validated : form.errors : %s", form.errors )
#
# 			# flash(u"Problème lors de l'envoi de votre formulaire.<br>Merci de réessayer", category='warning')
#
# 			for k,errors in form.errors.iteritems() :
# 				for e in errors :
# 					flash( e , category='danger')
#
# 			return redirect(url_for('register'))
#
#
# 	elif request.method == 'GET':
#
# 		return render_template(	'register.html',
#
# 								config_name		= config_name, # prod or default...
# 								app_metas		= app_metas,
# 								language		= "fr" ,
# 								languages_dict	= app_languages_dict ,
#
# 								site_section 	= "register",
# 								form			= form,
# 								user_infos		= current_user.get_public_infos
#
# 								)
#



@app.route('/logout', methods = ['GET'])
def logout():
	"""
	simply logout the user with flask_login.logout_user()
	"""
	logout_user()

	log_app.info("user is logged out...")

	flash(u"Vous êtes maintenant déconnecté.e", category='primary')

	return redirect(url_for('home'))




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### USER PREFERENCES ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


### TO DO
# @app.route('/preferences/user_infos', methods=['GET', 'POST'])
# @login_required
# def pref_infos():
# 	"""
# 	to update user infos
# 	"""

# 	form = UserParametersForm()

# 	# print current_user


# 	if request.method == 'POST' :

# 		print
# 		log_app.info("updating an user - POST \n")

# 		# for debugging purposes
# 		for f_field in form :
# 			log_app.info( "form name : %s / form data : %s ", f_field.name, f_field.data )


# 		if form.validate_on_submit():

# 			existing_user = mongo_users.find_one({"_id" : ObjectId(form.userOID.data)} )
# 			log_app.debug("existing_user : %s", pformat(existing_user) )


# 			### check if new email is already used by someone else
# 			is_new_email_taken = False
# 			existing_email = mongo_users.find_one( {"userEmail" : form.userEmail.data} )
# 			log_app.debug("existing_email : %s", pformat(existing_email) )
# 			if existing_email is not None :
# 				if existing_user["_id"] != existing_email["_id"] :
# 					is_new_email_taken = True

# 			if existing_user is None :
# 				flash(u"Erreur : utilisateur inexistant", category='warning')
# 				return redirect(url_for('pref_infos'))

# 			if is_new_email_taken :
# 				flash(u"Erreur : cet email déjà utilisé", category='warning')
# 				return redirect(url_for('pref_infos'))

# 			else :

# 				### saving updated infos in user
# 				user_obj = User()
# 				user_obj.populate_from_dict(dict_input=existing_user)

# 				# # update visitor to user in db --> function from ModelMixin
# 				log_app.warning("updating new_user in mongo_users" )

# 				user_obj.populate_from_form( form=form )
# 				user_obj.update_document_in_mongo( document=existing_user, coll=mongo_users )

# 				### relog user
# 				login_user( user_obj, remember=existing_user['userRememberMe'] )

# 				flash(u"Vos informations ont bien été mises à jour", category='primary')
# 				return redirect(url_for('pref_infos'))

# 		else :

# 			log_app.error("form was not validated : form.errors : %s", form.errors )

# 			flash(u"Erreur : formulaire invalide", category='warning')
# 			return redirect(url_for('pref_infos'))


# 	elif request.method == 'GET' :

# 		log_app.info("updating an user - GET \n")

# 		print current_user.__dict__

# 		# prepopulate input fields
# 		form.userOID.data 				= str(current_user.userOID)
# 		form.userName.data 				= current_user.userName.capitalize()
# 		form.userSurname.data 			= current_user.userSurname.capitalize()
# 		form.userEmail.data 			= current_user.userEmail
# 		form.userOtherStructure.data 	= current_user.userOtherStructure

# 		# prepopulate select fields
# 		form.userProfile.process_data(current_user.userProfile)
# 		form.userPartnerStructure.process_data(current_user.userPartnerStructure)
# 		form.userStructureProfile.process_data(current_user.userStructureProfile)

# 		# prepopulate boolean fields
# 		form.userHaveProjects.process_data(current_user.userHaveProjects)
# 		form.userJoinCollective.process_data(current_user.userJoinCollective)
# 		form.userNewsletter.process_data(current_user.userNewsletter)


# 		return render_template('user_preferences/user_parameters.html',

# 								config_name		= config_name, 						# prod or default...
# 								app_metas		= app_metas,
# 								language		= "fr" ,
# 								languages_dict	= app_languages_dict ,

# 								site_section 	= "preferences",
# 								site_subsection = "infos",
# 								form			= form,
# 								user_infos		= current_user.get_public_infos 	# cf model_user.py

# 								)


# @app.route('/preferences/user_password', methods=['GET', 'POST'])
# @login_required
# def pref_password():
# 	"""
# 	to update user infos
# 	"""

# 	form = UserNewPassword()

# 	# print current_user


# 	if request.method == 'POST' :

# 		print
# 		log_app.info("updating user password \n")

# 		# for debugging purposes
# 		for f_field in form :
# 			log_app.info( "form name : %s / form data : %s ", f_field.name, f_field.data )

# 		if form.validate_on_submit():

# 			existing_user = mongo_users.find_one({"_id" : ObjectId(form.userOID.data) } )
# 			# existing_user = mongo_users.find_one({"userEmail" : form.userEmailHidden.data} )

# 			log_app.debug("existing_user : %s", pformat(existing_user) )

# 			if existing_user is None :
# 				flash(u"Erreur : utilisateur inexistant", category='warning')
# 				return redirect(url_for('pref_password'))

# 			else :

# 				### check if old password is correct
# 				log_app.info ( "checking oldPassword : ", User.validate_login( existing_user['userPassword'], form.oldPassword.data ) )

# 				### update password / create new hashpassword
# 				new_hashpass = generate_password_hash(form.newPassword.data, method='sha256')
# 				log_app.debug("new_hashpass : %s", new_hashpass )

# 				### saving new password in user
# 				user_obj = User()
# 				user_obj.populate_from_dict(dict_input=existing_user)
# 				user_obj.userPassword = new_hashpass

# 				### TO DO
# 				# # update visitor to user in db --> function from ModelMixin
# 				log_app.warning("updating user_obj in mongo_users" )

# 				user_obj.update_document_in_mongo( document=existing_user, coll=mongo_users )

# 				### re-log user
# 				### login with flask-login
# 				login_user( user_obj, remember=existing_user['userRememberMe'] )


# 				flash(u"Votre mot de passe a  bien été mis à jour", category='primary')
# 				return redirect(url_for('pref_password'))

# 		else :

# 			log_app.error("form was not validated : form.errors : %s", form.errors )

# 			flash(u"Erreur : formulaire invalide", category='warning')
# 			return redirect(url_for('pref_password'))


# 	elif request.method == 'GET' :

# 		# prepopulate input fields
# 		form.userOID.data 				= current_user.userOID
# 		# form.userEmailHidden.data 	= current_user.userEmail

# 		return render_template('user_preferences/user_parameters.html',

# 								config_name		= config_name, 						# prod or default...
# 								app_metas		= app_metas,
# 								language		= "fr" ,
# 								languages_dict	= app_languages_dict ,

# 								site_section 	= "preferences",
# 								site_subsection = "password",
# 								form			= form,
# 								user_infos		= current_user.get_public_infos 	# cf model_user.py

# 								)



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ADMIN ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### to customize admin views check : https://www.youtube.com/watch?v=BIcjT2Zz4bU

### flask-admin formatters
### cf : http://flask-admin.readthedocs.io/en/latest/api/mod_model/#flask_admin.model.BaseModelView.column_type_formatters

# def date_format(view, value):
# 	return value.strftime('%d.%m.%Y')

# MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
# MY_DEFAULT_FORMATTERS.update({
# 		type(None): typefmt.null_formatter,
# 		date: date_format
# 	})

# class CustomWidget(XEditableWidget):
# 	def get_kwargs(self, subfield, kwargs):
# 		if subfield.type == 'TextAreaField':
# 			kwargs['data-type'] = 'textarea'
# 			kwargs['data-rows'] = '20'
# 		# elif: kwargs for other fields

# 		return kwargs

# class MyAdminIndexView(AdminIndexView) :

# 	def is_accessible(self) :
# 		"""
# 		make it accessible via flask-login
# 		"""
# 		log_app.debug("current_user : \n %s", pformat(current_user.__dict__))

# 		# using custom property class
# 		return current_user.is_staff_level # instead of : return current_user.is_authenticated

# 	def inaccessible_callback(self, name, **kwargs) :

# 		# TO DO : flash if auth level not enough
# 		flash(u"Vous ne pouvez pas accéder à cette section", category='warning')
# 		return redirect(url_for('home'))

# class UserViewAdmin(ModelView):
# 	"""
# 	view of an user in flask-admin
# 	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
# 	"""
# 	### for flask-login
# 	column_type_formatters = MY_DEFAULT_FORMATTERS

# 	list_template 	= 'admin/list.html'
# 	create_template = 'admin/create.html'
# 	edit_template 	= 'admin/edit.html'

# 	can_export = True
#  	can_set_page_size = True

# 	def is_accessible(self) :
# 		"""
# 		make it accessible via flask-login
# 		"""

# 		# using custom property class
# 		return current_user.is_admin_level # instead of : return current_user.is_authenticated

# 	def inaccessible_callback(self, name, **kwargs) :

# 		# TO DO : flash if auth level not enough
# 		flash(u"Vous ne pouvez pas accéder à cette section", category='warning')

# 		return redirect(url_for('home'))

# 	def get_list_form(self):
# 		return self.scaffold_list_form(widget=CustomWidget)

# 	### for flask-admin

# 	column_list 			= (
# 								'userName', 'userSurname', 'userEmail',
# 								'userProfile',
# 								# 'last_modified_at',
# 								'logins_total',
# 								'userPartnerStructure', 'userOtherStructure','verified_as_partner',
# 								'userAuthLevel',
# 								'userHaveProjects','userJoinCollective',
# 								'userMessage',
# 								'follow_up_user',
# 								# 'created_at',
# 								'login_last_at',
# 							)
# 	column_details_list = column_list + ('created_at', 'last_modified_at', '_id')
# 	can_view_details = True

# 	column_searchable_list 		= ( 'userName', 'userSurname', 'userEmail',
# 									'userPartnerStructure', 'userOtherStructure',
# 									'verified_as_partner',
# 									'userProfile',
# 									'userAuthLevel',
# 									)
# 	column_sortable_list	= column_list
# 	# column_sortable_list 	= (	'userName', 'userSurname', 'userEmail',
# 	# 							'userPartnerStructure','userOtherStructure'
# 	# 							)

# 	# column_filters = (BooleanEqualFilter(column=UserID.userName, name='userName'),)


# 	column_labels = dict(	userName				= 'Name',
# 							userSurname				= 'Last Name',
# 							userEmail				= 'Email',
# 							userProfile				= 'Profile',
# 							userPartnerStructure	= 'Structure (partner)',
# 							userOtherStructure		= 'Structure (other)',
# 							userAuthLevel			= 'Auth Level',
# 							userHaveProjects		= 'Have Projects',
# 							userJoinCollective		= 'Wants to join collective',
# 							userMessage				= 'Message',
# 							follow_up_user			= 'Suivi',

# 						)

# 	form 					= UserAdminInfos

# 	# custom field rendering in admin interface
# 	# cf : https://stackoverflow.com/questions/21727129/how-to-make-a-field-non-editable-in-flask-admin-view-of-a-model-class
# 	form_widget_args = {
# 		'userEmail'			: { 'readonly' : True },
# 		'created_at'		: { 'readonly' : True },
# 		'userPublicKeyAPI'	: { 'readonly' : True },
# 		'temp_pwd'			: { 'readonly' : True },
# 	}


# class FeedbackAdmin(ModelView):
# 	"""
# 	view of a message in flask-admin
# 	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
# 	"""

# 	### for flask-login
# 	column_type_formatters = MY_DEFAULT_FORMATTERS

# 	list_template 	= 'admin/list.html'
# 	create_template = 'admin/create.html'
# 	edit_template 	= 'admin/edit.html'

# 	can_export = True
#  	can_set_page_size = True

# 	def is_accessible(self) :
# 		"""
# 		make it accessible via flask-login
# 		"""
# 		# using custom property class
# 		# return current_user.is_admin_level # instead of : return current_user.is_authenticated
# 		return current_user.is_staff_level # instead of : return current_user.is_authenticated

# 	def inaccessible_callback(self, name, **kwargs) :

# 		# TO DO : flash if auth level not enough

# 		return redirect(url_for('home'))


# 	### for flask-admin

# 	column_list 			= (
# 								'userName', 'userSurname', 'userEmail',
# 								'userOtherStructure',
# 								'userFeedbackTopic',
# 								'userMessage',
# 								'created_at',
# 								'follow_up_user'
# 							)
# 	column_searchable_list 		= column_list
# 	column_sortable_list	= column_list

# 	column_labels = dict(	userName				= u'Prénom',
# 							userSurname				= u'Nom',
# 							userEmail				= u'Email',
# 							userOtherStructure		= u'Structure',
# 							userFeedbackTopic		= u'Sujet',
# 							userMessage				= u'Message',
# 							follow_up_user			= u'Suivi',
# 							created_at				= u'Reçu le'
# 						)

# 	form 					= MessagesFromLandingAdmin

# 	# custom field rendering in admin interface
# 	form_widget_args = {
# 		'userEmail'	: {'readonly': True},
# 		'created_at': {'readonly': True },
# 	}


# class ReferencedProjectCarrierFeedback(ModelView):
# 	"""
# 	view of a message in flask-admin
# 	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
# 	"""

# 	### for flask-login
# 	column_type_formatters = MY_DEFAULT_FORMATTERS

# 	list_template 	= 'admin/list.html'
# 	create_template = 'admin/create.html'
# 	edit_template 	= 'admin/edit.html'

# 	can_export = True
#  	can_set_page_size = True

# 	def is_accessible(self) :
# 		"""
# 		make it accessible via flask-login
# 		"""
# 		# using custom property class
# 		# return current_user.is_admin_level # instead of : return current_user.is_authenticated
# 		return current_user.is_staff_level # instead of : return current_user.is_authenticated

# 	def inaccessible_callback(self, name, **kwargs) :

# 		# TO DO : flash if auth level not enough

# 		return redirect(url_for('index'))



# 	### for flask-admin

# 	column_list 			= (
# 								'partnerStructureName',
# 								'partnerStructureWebsite',
# 								'partnerStructureContactName',
# 								'partnerStructureContactEmail',
# 								'message',
# 								'created_at',
# 								'follow_up'
# 							)
# 	column_searchable_list 		= column_list

# 	column_sortable_list	= column_list

# 	column_labels = dict(	partnerStructureName			= 'Nom structure',
# 							partnerStructureWebsite			= 'Site structure',
# 							partnerStructureContactName		= 'Contact chez la structure',
# 							partnerStructureContactEmail	= 'Email contact',
# 							message							= 'Message',
# 							created_at						= 'Reçu le',
# 							follow_up						= 'Suivi'
# 						)

# 	form 					= ReferencedProjectCarrierForm

# 	# custom field rendering in admin interface
# 	form_widget_args = {
# 		'created_at': {'readonly': True }
# 	}


# class NotReferencedProjectCarrierFeedback(ModelView):
# 	"""
# 	view of a message in flask-admin
# 	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
# 	"""

# 	### for flask-login
# 	column_type_formatters = MY_DEFAULT_FORMATTERS

# 	list_template 	= 'admin/list.html'
# 	create_template = 'admin/create.html'
# 	edit_template 	= 'admin/edit.html'

# 	can_export = True
#  	can_set_page_size = True

# 	def is_accessible(self) :
# 		"""
# 		make it accessible via flask-login
# 		"""
# 		# using custom property class
# 		# return current_user.is_admin_level # instead of : return current_user.is_authenticated
# 		return current_user.is_staff_level # instead of : return current_user.is_authenticated

# 	def inaccessible_callback(self, name, **kwargs) :

# 		# TO DO : flash if auth level not enough

# 		return redirect(url_for('index'))



# 	### for flask-admin

# 	column_list 			= (
# 								'projectName',
# 								'projectStructureName',
# 								'projectContactName',
# 								'projectContactEmail',
# 								'projectAddress',
# 								'projectActionArea',
# 								'projectActionAreaLocalDetails',
# 								'projectCategories',
# 								'projectCategoriesOther',
# 								'projectAudiences',
# 								'projectAudiencesOther',
# 								'projectStartYear',
# 								'projectStage',
# 								'projectDescription',
# 								'projectInnovation',
# 								'projectFundingAndPartners',
# 								'projectRewards',
# 								'projectWebsite',
# 								'projectAttachment'
# 							)
# 	column_searchable_list 		= column_list

# 	column_sortable_list	= column_list

# 	column_labels = dict()

# 	form 					= NotReferencedProjectCarrierForm

# 	# custom field rendering in admin interface
# 	form_widget_args = {
# 		'created_at': {'readonly': True }
# 	}


# class StructuresFeedback(ModelView):
# 	"""
# 	view of a message in flask-admin
# 	cf : https://github.com/mrjoes/flask-admin/blob/master/examples/pymongo/app.py
# 	"""

# 	### for flask-login
# 	column_type_formatters = MY_DEFAULT_FORMATTERS

# 	list_template 	= 'admin/list.html'
# 	create_template = 'admin/create.html'
# 	edit_template 	= 'admin/edit.html'

# 	can_export = True
#  	can_set_page_size = True

# 	def is_accessible(self) :
# 		"""
# 		make it accessible via flask-login
# 		"""
# 		# using custom property class
# 		# return current_user.is_admin_level # instead of : return current_user.is_authenticated
# 		return current_user.is_staff_level # instead of : return current_user.is_authenticated

# 	def inaccessible_callback(self, name, **kwargs) :

# 		# TO DO : flash if auth level not enough

# 		return redirect(url_for('index'))



# 	### for flask-admin

# 	column_list 			= (
# 								'structureName',
# 								'structureWebsite',
# 								'structureContactName',
# 								'structureContactRole',
# 								'structureContactEmail',
# 								'structureInterests',
# 								'structureReasonToJoin',
# 								'structureListHow',
# 								'structureListHowOther',
# 								'structureProjectsToShareCount',
# 								'structureProjectsToShareInfos',
# 								'structureProjectsToShareFormat',
# 								'structureProjectsToShareWebsite',
# 								'structureProjectsToShareAttachment'
# 							)
# 	column_searchable_list 		= column_list

# 	column_sortable_list	= column_list

# 	column_labels = dict()

# 	form 					= NotReferencedProjectCarrierForm

# 	# custom field rendering in admin interface
# 	form_widget_args = {
# 		'created_at': {'readonly': True }
# 	}




### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### FILES ROUTES
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


@app.route('/download/<file_ext>/<file_name>', methods=['GET'] ) # this is a job for GET, not POST
def download_file(file_ext, file_name):
	"""
	send file from server
	"""

	log_app.debug("file_name : %s ", 	file_name)
	log_app.debug("file_ext : %s ", 	file_ext)
	log_app.info("file_ext in AUTHORIZED_FILETYPES_LIST: %s", (file_ext in AUTHORIZED_FILETYPES_LIST) )


	if file_ext in AUTHORIZED_FILETYPES_LIST :

		file_mimetype 		= AUTHORIZED_FILETYPES_DICT[file_ext]["mimetype"]
		file_foldername 	= AUTHORIZED_FILETYPES_DICT[file_ext]["folder"]
		file_folder 		= "static/{}/".format(file_foldername)
		file_name_ext 		= "{}.{}".format(file_name, file_ext)
		full_filepath 		= file_folder + file_name_ext

		try :

			return send_file(	full_filepath,
								mimetype			= file_mimetype,
								attachment_filename	= file_name_ext,
								as_attachment		= True
							)
		except :

			log_app.error("downloading this file is not working: %s.%s ", file_name, file_ext )

			return redirect(url_for('home'))

	else :

		log_app.error("downloading this file is not authorized: %s.%s ", file_name, file_ext )

		return redirect(url_for('home'))
