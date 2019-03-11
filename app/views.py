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
	choices 	: global | endpoints | styles | routes | socials
	variables : <collection> and <doc_id>
	arguments : as_list (bool), field (str)
	example 	: http://localhost:8100/backend/api/config?as_list=true
	"""

	log_app.debug("config app route")
	log_app.debug("config app route / collection : %s", collection )
	log_app.debug("config app route / doc_id : %s", doc_id )

	### target right config collection 
	if collection in ["global" , "footer", "navbar", "endpoints" , "styles" , "routes", "socials" ] : 
		mongoColl = mongoConfigColls[collection] ### imported from . (and from there from .api.__init__ )
	else : 
		log_app.warning("error : -%s- is not a valid config collection (redirect)", collection)
		return redirect( "/error/400" )

	### get request args if any 
	as_list = request.args.get('as_list', default=False, 		type=bool)
	field 	= request.args.get('field', 	default="field", 	type=str)
	token 	= request.args.get('token', 	default=None, 		type=str)
	log_app.debug("config app route / as_list : %s", as_list )

	### filter out field arg to unique identifiers fields in documents
	if field not in ['_id', 'field'] : 
		field = 'field'
		
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


ANTI_SPAM_FIELD_NAME = "userMiddlename"



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
