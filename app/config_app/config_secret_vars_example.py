# -*- encoding: utf-8 -*-

"""
main config file --> to keep secret 
stores main secret keys and app passwords
"""

""" APP SECRET KEY """
SECRET_KEY					= "app_very_secret_key"


""" HOST / PORT / DOMAIN / SERVER """
SERVER_NAME_TEST		= "True" 


# """ PORT SOCKETIO """
# PORT_EVENTLET		= "4000"


""" MONGODB """
MONGO_ROOT_LOCAL     = "localhost"
MONGO_ROOT_DOCKER    = "host.docker.internal"

MONGO_DBNAME         = 'apiviz'
MONGO_DBNAME_TEST    = 'apiviz-test'
MONGO_DBNAME_PREPROD = 'apiviz-preprod'
MONGO_DBNAME_PROD    = 'apiviz-prod'

MONGO_PORT_LOCAL     = "27017"

MONGO_ROOT_SERVER    = "127.0.0.1" # IP depending on your server's mongoDB configuration
MONGO_PORT_SERVER    = "27017"
MONGO_USER_SERVER    = "MY-MONGODB-SERVER-USERNAME"
MONGO_PASS_SERVER    = "MY-MONGODB-SERVER-USER-PASSWORD"
MONGO_OPTIONS_SERVER = "?MY-MONGODB-SERVER-OPTIONS" ### must begin with "?"

MONGO_DISTANT_URI          = "mongodb://<DISTANT-USERNAME>:<DISTANT-PASSWORD>@<DISTANT-HOST>:<DISTANT-PORT>"  
MONGO_DISTANT_URI_OPTIONS  = "?ssl=true&replicaSet=APIVIZ-configs-shard-0&authSource=admin&retryWrites=true"
