
import os

from .. import log_app, pformat

config_name    = os.getenv('FLASK_CONFIGURATION', 'default')
config_mongodb = os.getenv('MONGODB_MODE', 'local')
config_docker  = os.getenv('DOCKER_MODE',  'docker_off')

print
log_app.info("$ config_name : %s", config_name)  
log_app.info("$ config_mongodb : %s", config_mongodb)  
log_app.info("$ config_docker : %s", config_docker)  

correction_env_path = {
  "development"   : "",
  "testing"       : "",
  "production"    : "",
  "preprod"       : "",
  "default"       : ""       ### 'default' for local development
}
repath_env_vars = correction_env_path[config_name]


### set environment default variables from gitignored : config_secret_vars_prod.py
try :
  
  ### load secret env vars and keys from secret | public file

  if config_name in ["default"] : 
    from .config_secret_vars_example import *

  elif config_name in ["testing", "preprod", "production"] : 
    from .config_secret_vars_prod import *

  ### load env vars

  os.environ["SECRET_KEY"] = SECRET_KEY
  os.environ["SERVER_NAME_TEST"] = SERVER_NAME_TEST

  try : 
    os.environ["ALLOWED_HOSTS"]	= ALLOWED_HOSTS
  except :
    log_app.info("no ALLOWED_HOSTS env var") 

  # os.environ["PORT_EVENTLET"]		= PORT_EVENTLET




  ### load correct MONGO_URI given env vars
  # config_name : default | testing | preprod | production
  # x 
  # config_docker : true | false
  # x 
  # config_mongodb : local | distant | server


  # temporary dicts
  mongodb_roots_dict = {
    "local"  : { 
      "docker_off" : MONGO_ROOT_LOCAL,  
      "docker_on"  : MONGO_ROOT_DOCKER  
    },
    "server" : { 
      "docker_off" : MONGO_ROOT_SERVER, 
      "docker_on"  : MONGO_ROOT_DOCKER  
    },
  }

  mongodb_ports_dict = {
    "local"  : MONGO_PORT_LOCAL,
    "server" : MONGO_PORT_SERVER,
  }

  mongodb_dbnames_dict = {
    "default"     : MONGO_DBNAME,
    "testing"     : MONGO_DBNAME_TEST,
    "preprod"     : MONGO_DBNAME_PREPROD,
    "production"  : MONGO_DBNAME
  }

  ### get DB name
  mongodb_dbname = mongodb_dbnames_dict[config_name]

  ### get MONGODB FULL URI 
  ### format : mongodb://<USER>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>?<OPTIONS>

  if config_mongodb == "distant" :
    mongodb_uri = "{}/{}{}".format(MONGO_DISTANT_URI, mongodb_dbname, MONGO_DISTANT_URI_OPTIONS)
  
  else : 
    mongodb_root = mongodb_roots_dict[config_mongodb][config_docker]
    mongodb_port = mongodb_ports_dict[config_mongodb]

    ### get login if mongodb hosted on a server
    mongodb_login = "" 
    mongodb_options = "" 
    if config_name == "server" : 
      mongodb_login = "{}:{}@".format(MONGO_USER_SERVER, MONGO_PASS_SERVER)
      mongodb_options = MONGO_OPTIONS_SERVER ### must begin with "?"

    mongodb_uri = "mongodb://{}{}:{}/{}{}".format(mongodb_login, mongodb_root, mongodb_port, mongodb_dbname, mongodb_options)

  os.environ["MONGODB_URI"] = mongodb_uri 




### except if no production env 
except : 
  log_app.error(" --- ENV VARS WERE NOT LOADED CORRECTLY --- ") 



class Config(object):
  
  """ BASIC Config Class """

  """ GLOBAL_FLASK """
  static_dir  = '/static'
  uploads_dir = '/static/uploads'

  SITE_ROOT			= os.path.realpath(os.path.dirname(__file__))
  SITE_STATIC		= SITE_ROOT   +  static_dir
  SITE_UPLOADS	= SITE_ROOT   +  uploads_dir

  """ HOST """
  DOMAIN_NAME			=  os.getenv("DOMAIN_NAME")
  DOMAIN_ROOT			=  os.getenv("DOMAIN_ROOT")
  DOMAIN_PORT			=  os.getenv("DOMAIN_PORT")
  
  # SERVER_NAME		=  os.getenv("SERVER_NAME")
  SERVER_NAME_TEST	= os.getenv("SERVER_NAME_TEST")
  if SERVER_NAME_TEST == "True" :
    SERVER_NAME  	=  os.getenv("SERVER_NAME")

  """ SESSIONS """
  SECRET_KEY					= os.getenv("SECRET_KEY")

  """ JWT """
  # JWT_SECRET_KEY		= os.getenv("JWT_SECRET_KEY")
  
  """ MONGODB """
  # MONGO_DBNAME								= 'apiviz'
  MONGO_URI	= os.getenv("MONGODB_URI")
  MONGO_COLL_CONFIG_GLOBAL					= "config_global"
  MONGO_COLL_CONFIG_FOOTER					= "config_footer"
  MONGO_COLL_CONFIG_NAVBAR					= "config_navbar"
  MONGO_COLL_CONFIG_APP_STYLES			= "config_app_styles"
  MONGO_COLL_CONFIG_DATA_ENDPOINTS	= "config_data_endpoints"
  MONGO_COLL_CONFIG_ROUTES					= "config_routes"
  MONGO_COLL_CONFIG_SOCIALS					= "config_socials"


class DevelopmentConfig(Config):

  """ Development Config Class """
  DEBUG = True
 
  """ RUNNING ENVIRONNEMENT """
  RUNNING_ENV = "local" # local | preprod | prod


class PreprodConfig(Config):
  
  """ PRODUCTION Config Class """
  DEBUG = True
  ALLOWED_HOSTS		= os.getenv("ALLOWED_HOSTS")


  """ RUNNING ENVIRONNEMENT """
  RUNNING_ENV	= os.getenv("RUNNING_ENV", "preprod")


class ProductionConfig(Config):
  
  """ PRODUCTION Config Class """
  DEBUG = False
  ALLOWED_HOSTS		= os.getenv("ALLOWED_HOSTS")


  """ RUNNING ENVIRONNEMENT """
  RUNNING_ENV	= os.getenv("RUNNING_ENV", "production")



class TestingConfig(DevelopmentConfig, Config):
  
  """ TESTING Config Class """
  DEBUG = True
  TESTING = True



### config dict to reroute to correct objects
config = {
  "development"	: "%sapp.config_app.config_env.DevelopmentConfig"    %(repath_env_vars),
  "testing"			: "%sapp.config_app.config_env.TestingConfig"        %(repath_env_vars),
  "production"	: "app.config_app.config_env.ProductionConfig",     #%(repath_env_vars),    	
  "preprod"	    : "app.config_app.config_env.PreprodConfig",     #%(repath_env_vars),    	
  "default"			: "app.config_app.config_env.DevelopmentConfig"      ### 'default' for local 
}


### main function to configure app
def configure_app(app):
  """ configure Flask app from object created above """

  log_app.info("$ config[config_name] : %s ",  config[config_name]  )

  log_app.info("$ creating app.config from object...")
  app.config.from_object( config[config_name] )

  log_app.info("$ app.config['RUNNING_ENV']  : %s ", app.config["RUNNING_ENV"] )
  # log_app.info("$ app.config['MONGO_DBNAME'] : %s ", app.config["MONGO_DBNAME"] ) 
  print