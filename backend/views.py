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

def getValueFromDictAndPathString(dictToSearch, path) : 
  """ 
  """ 
  print " "
  currentValue = dictToSearch
  path_splitted = path.split('/')
  while(len(path_splitted)):
    key = path_splitted.pop(0)
    currentValue = currentValue.get(key)
    if (type(currentValue) is not dict and len(path_splitted)):
      print("Path does not exist!")
      return None 

  return currentValue

  
def checkJWT(token, roles_to_check, uuid="", url_check="http://localhost:4100/api/auth/tokens/confirm_access"):
  """ 
  authenticate a token 
  sending request to the auth url / service 
  specified in config
  ... doing so to avoid middle man risk when editing
  """

  print ". "*50

  # is_authorized = True

  ### set the collection to user
  mongoColl = mongoConfigColls['endpoints']
  auth_mode = app.config['AUTH_MODE']
  log_app.debug("checkJWT / auth_mode : %s", auth_mode )
  log_app.debug("checkJWT / roles_to_check : %s", roles_to_check )

  ### retrieving the root_url for authentication in general given the AUTH_MODE
  root_auth_doc = mongoColl.find_one({'apiviz_front_uuid': uuid, 'field' : 'app_data_API_root_auth'})
  log_app.debug("checkJWT / root_auth_doc : \n%s", pformat(root_auth_doc) )

  auth_url = root_auth_doc['root_url'][auth_mode]
  log_app.debug( "checkJWT / auth_url : %s", pformat(auth_url) )

  ### retrieving the root_url and args for authentication
  confirm_auth_doc = mongoColl.find_one({'apiviz_front_uuid': uuid, 'field' : 'app_data_API_user_auth'})
  confirm_rooturl = confirm_auth_doc['root_url']
  confirm_user_role_path = confirm_auth_doc['resp_fields']['user_role']['path']
  log_app.debug( "checkJWT / confirm_user_role_path : %s", confirm_user_role_path) 

  confirm_basestring = auth_url + confirm_rooturl
  # log_app.debug( "checkJWT / confirm_basestring : %s", pformat(confirm_basestring) )
  
  confirm_options = confirm_auth_doc['args_options']
  confirm_token_arg = ''
  for arg in confirm_options : 
    if arg['app_arg'] == 'authToken' : 
      confirm_arg = '?{}={}'.format(arg['arg'], token)
  
  confirm_url = confirm_basestring + confirm_arg
  log_app.debug( "checkJWT / confirm_url : %s", pformat(confirm_url) )

  ### send request to service and read response
  auth_response = requests.get(confirm_url)
  auth_response_status = auth_response.status_code
  log_app.debug( "checkJWT / auth_response_status : %s", auth_response_status )
  auth_response_data = auth_response.json()
  log_app.debug( "checkJWT / auth_response : \n%s", pformat(auth_response_data) )

  ### get role to check value in response
  auth_response_user_role = getValueFromDictAndPathString(auth_response_data, confirm_user_role_path)
  log_app.debug( "checkJWT / auth_response_user_role : %s", auth_response_user_role) 


  print ". "*50

  # return is_authorized
  return auth_response_user_role in roles_to_check or 'all' in roles_to_check

@app.route('/backend/api/config/<string:collection>/<string:doc_id>', methods=['GET','POST','DELETE'])
@app.route('/backend/api/config/<string:collection>', methods=['GET', 'POST'], defaults={"doc_id" : None})
@app.route('/backend/api/config', methods=['GET'], defaults={'collection': 'global', "doc_id" : None})
def backend_configs(collection, doc_id=None):
  """
  Main route to GET and POST/PUT/DELETE
  choices 	: global | endpoints | styles | routes | socials
  variables : <collection> and <doc_id>
  arguments : as_list (bool), field (str)
  example 	: http://localhost:8100/backend/api/config?as_list=true
  """

  print ""
  log_app.debug("config app route")
  log_app.debug("config app route / method : %s", request.method )
  log_app.debug("config app route / collection : %s", collection )
  log_app.debug("config app route / doc_id : %s", doc_id )

  ### target right config collection
  if collection in ["global" , "footer", "navbar", "tabs", "endpoints" , "styles" , "routes", "socials" ] :
    mongoColl = mongoConfigColls[collection] ### imported from . (and from there from .api.__init__ )
  else :
    log_app.warning("error : -%s- is not a valid config collection (redirect)", collection)
    return redirect( "/error/400" )

  ### get request args if any
  apiviz_uuid = request.args.get('uuid',    default="", 	type=str)
  log_app.debug("config app route / apiviz_uuid : %s", apiviz_uuid )

  field 	= request.args.get('field', 	default='field', type=str)
  as_list = request.args.get('as_list', default=False,   type=bool)


  # role_to_check = request.args.get('role',    default='admin', type=str)
  roles_to_check = COLLECTIONS_AUTH_MODIFICATIONS[collection][request.method]
  log_app.debug("config app route / roles_to_check : %s", roles_to_check )

  # req_data 	  = request.data
  # log_app.debug("config app route / request.data : \n%s", pformat(request.data ))
  req_json    = request.get_json()
  log_app.debug("config app route / req_json : \n%s", pformat(req_json) )

  ### retrieve access token 
  token = request.args.get('token', default='', type=str)
  if req_json : 
    token = req_json.get('token', '')

  ### example of access token :
  # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTcwODI3OTQsIm5iZiI6MTU1NzA4Mjc5NCwianRpIjoiNjA4YWRhMDktMzA4My00ZmE1LTg1NDMtNjRkNDJmM2E4ZmZhIiwiZXhwIjoxNTU3MTI1OTk0LCJpZGVudGl0eSI6IjVjY2YzMmExODYyNmEwM2MzNmY1MzYzNCIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsInVzZXJfY2xhaW1zIjp7Il9pZCI6IjVjY2YzMmExODYyNmEwM2MzNmY1MzYzNCIsImluZm9zIjp7Im5hbWUiOiJFbGlub3IiLCJzdXJuYW1lIjoiT3N0cm9tIiwiZW1haWwiOiJlbGlub3Iub3N0cm9tQGVtYWlsbmEuY28iLCJwc2V1ZG8iOiJBbm9ueW1vdXMgVXNlciJ9LCJhdXRoIjp7InJvbGUiOiJndWVzdCIsImNvbmZfdXNyIjpmYWxzZX0sInByb2ZpbGUiOnsibGFuZyI6ImVuIiwiYWdyZWVtZW50IjpmYWxzZSwidXNyX3ZpZXciOiJtaW5pbWFsIiwidXNyX3Byb2ZpbGVzIjpbXX19fQ.Iux2Grzvv-6VBXzKME5ub31iLtl-LHYea_0JSdQ22eM

  ### filter out field arg to unique identifiers fields in documents
  if field not in ['_id', 'field'] :
    field = 'field'

  ### build basic query
  query = {'apiviz_front_uuid' : apiviz_uuid}
  # query = {"apiviz_front_uuid" : apiviz_uuid }
  if doc_id :
    query["_id"] = ObjectId(doc_id)

  log_app.debug("config app route / query : \n%s", query )


  ### check if token allows user to POST
  # if True : ### only for tests
  if token != '' :
    log_app.debug("config app route / checking jwt..." )

  ### TO DO
  if request.method != 'GET':

    if request.method == 'POST':

      log_app.debug("config app route / POST" )
      is_authorized = checkJWT(token, roles_to_check, uuid=apiviz_uuid)

      if is_authorized :
        return "hello config master / POST ... praise be"
      else :
        return "noooope"

    elif request.method == 'DELETE':

      log_app.debug("config app route / DELETE" )
      is_authorized = checkJWT(token, roles_to_check, uuid=apiviz_uuid)

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

# @app.route('/', methods=['GET'])
# @app.route('/home/<string:lang>', methods=['GET'])
# @app.route('/home', methods=['GET'], defaults={"lang":"en"})
# def home(lang="fr"):

#   log_app.debug("entering new home page")

#   app_config = getDocuments(mongo_config_global)
#   log_app.debug("app_config :/n%s", pformat(app_config))

#   if lang == "fr" :
#     template = "new-home.html"
#   else :
#     template = "new-home-english.html"

#   return render_template(
#     template,
#     config_name		= config_name, # prod, testing, default...
#     app_config 		= app_config,
#     app_metas			= app_metas,
#     language			= lang,
#   )


# @app.route('/tools/<string:lang>', methods=['GET'])
# @app.route('/tools', methods=['GET'], defaults={"lang":"en"})
# def Tools(lang="en"):

#   log_app.debug("entering tools page")
#   app_config = getDocuments(mongo_config_global)

#   if lang == "fr" :
#     template = "les-outils.html"
#   else :
#     template = "les-outils-english.html"

#   return render_template(
#     template,
#     config_name		= config_name, # prod, testing, default...
#     app_metas			= app_metas,
#     app_config 		= app_config,
#     language			= lang
#   )


# @app.route('/sonum-banner-carto/<string:lang>', methods=['GET'])
# @app.route('/sonum-banner-carto', methods=['GET'], defaults={"lang":"fr"})
# def Banner(lang="fr"):

#   log_app.debug("entering test banner-carto page")
#   app_config = getDocuments(mongo_config_global)

#   if lang == "fr" : 
#     template = "sonum-banner-carto.html"
#   else : 
#     template = "sonum-banner-carto.html"

#   return render_template(
#     template,
#     config_name		= config_name, # prod, testing, default...
#     app_metas			= app_metas, 
#     app_config 		= app_config,
#     language			= lang
#   )

@app.route('/', methods=['GET','POST'],defaults={'path': ''})
@app.route('/<path:path>', methods=['GET','POST'])
def spa(path):

  log_app.debug("entering SPA page")
  app_config = getDocuments(mongo_config_global)

  run_mode = config_name
  if config_docker == "docker_on" and config_name == "default":
    run_mode = "default_docker"

  return render_template(
    "spa.html",
    config_name		= run_mode, # prod, testing, default, default_docker...
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
