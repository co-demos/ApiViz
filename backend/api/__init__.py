# -*- encoding: utf-8 -*-


from .. import app, os, PyMongo, log_app, pformat, json, json_util


# set as OK to run with app.context()
with app.app_context():

  mongo = PyMongo(app)

  log_app.info(">>> starting app --- MongoDB connected")

  ### access mongodb collections ###
  # mongo_users      = mongo.db[ app.config["MONGO_COLL_USERS"] ]
  mongo_config_global         = mongo.db[ app.config["MONGO_COLL_CONFIG_GLOBAL"] ]
  mongo_config_footer         = mongo.db[ app.config["MONGO_COLL_CONFIG_FOOTER"] ]
  mongo_config_navbar         = mongo.db[ app.config["MONGO_COLL_CONFIG_NAVBAR"] ]
  mongo_config_data_endpoints = mongo.db[ app.config["MONGO_COLL_CONFIG_DATA_ENDPOINTS"] ]
  mongo_config_app_styles     = mongo.db[ app.config["MONGO_COLL_CONFIG_APP_STYLES"] ]
  mongo_config_routes         = mongo.db[ app.config["MONGO_COLL_CONFIG_ROUTES"] ]
  mongo_config_socials        = mongo.db[ app.config["MONGO_COLL_CONFIG_SOCIALS"] ]
  # mongo_feedbacks  = mongo.db[ app.config["MONGO_COLL_FEEDBACKS"] ]
  # mongo_join_message_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_REFERENCED_PROJECT_CARRIER"] ]
  # mongo_join_message_not_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_NOT_REFERENCED_PROJECT_CARRIER"] ]
  # mongo_join_message_structures = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_STRUCTURES"] ]

  mongoColls = {
    # "users"  : mongo_users,
    app.config["MONGO_COLL_CONFIG_GLOBAL"]          : mongo_config_global,
    app.config["MONGO_COLL_CONFIG_FOOTER"]          : mongo_config_footer,
    app.config["MONGO_COLL_CONFIG_NAVBAR"]          : mongo_config_navbar,
    app.config["MONGO_COLL_CONFIG_DATA_ENDPOINTS"]  : mongo_config_data_endpoints,
    app.config["MONGO_COLL_CONFIG_APP_STYLES"]      : mongo_config_app_styles,
    app.config["MONGO_COLL_CONFIG_ROUTES"]          : mongo_config_routes,
    app.config["MONGO_COLL_CONFIG_SOCIALS"]         : mongo_config_socials,
    # app.config["MONGO_COLL_USERS"]                : mongo_users,
    # app.config["MONGO_COLL_FEEDBACKS"]            : mongo_feedbacks,
  }

mongoConfigColls ={
  "global"    : mongo_config_global,
  "footer"    : mongo_config_footer,
  "navbar"    : mongo_config_navbar,
  "endpoints" : mongo_config_data_endpoints,
  "styles"    : mongo_config_app_styles,
  "routes"    : mongo_config_routes,
  "socials"   : mongo_config_socials,
}

log_app.debug(">>> MongoDB / mongoColls.keys() : \n %s", pformat( mongoColls.keys() ) )

# log_app.info(">>> MongoDB : mongo_users     : \n %s", mongo_users  )
# log_app.info(">>> MongoDB : mongo_feedbacks   : \n %s", mongo_feedbacks  )


### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
### CREATE DEFAULT GLOBAL CONFIG IF COLLECTION IS EMPTY
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
def setupDefaultConfig(collection, defaultList, uniqueField="field") :
  """ 
  main function to set up config collections
  """
  
  ### delete all previous default items in collection
  collection.delete_many({"is_default" : True })
  
  ### set up 
  for config_app_item in defaultList : 
    
    # print ("- - - "*10 )
    # log_app.debug(">>> config_item : \n%s", pformat(config_app_item)) 

    current_app_config_item = collection.find_one({ uniqueField : config_app_item[ uniqueField ] })
    # log_app.debug(">>> current_app_config_item : \n%s", pformat(current_app_config_item))
    
    if current_app_config_item == None : 
      # log_app.debug(">>> current_app_config_item is None --> add : %s", config_app_item[uniqueField])
      collection.insert(config_app_item)

    else : 
      if current_app_config_item["is_default"] : 
        # log_app.debug(">>> current_app_config_item is default --> update : %s", current_app_config_item[uniqueField])
        current_app_config_item_id = current_app_config_item["_id"]
        collection.replace_one( {"_id": current_app_config_item_id}, config_app_item )

from backend.config_app.config_app_global         import default_global_config
from backend.config_app.config_app_footer         import default_app_footer
from backend.config_app.config_app_navbar         import default_app_navbar
from backend.config_app.config_app_data_endpoints import default_data_endpoints_config
from backend.config_app.config_app_styles         import default_app_styles_config
from backend.config_app.config_app_routes         import default_routes_config
from backend.config_app.config_app_socials        import default_socials_config

### retrieve default config for every collection
existing_app_config             = list( mongo_config_global.find({}) )
# log_app.debug(">>> existing_app_config : \n%s \n", pformat(existing_app_config))

existing_app_footer_config      = list( mongo_config_footer.find({}) )
# log_app.debug(">>> existing_app_config : \n%s \n", pformat(existing_app_footer_config))

existing_app_navbar_config      = list( mongo_config_navbar.find({}) )
# log_app.debug(">>> existing_app_config : \n%s \n", pformat(existing_app_navbar_config))

existing_data_endpoints_config   = list( mongo_config_data_endpoints.find({}) )
# log_app.debug(">>> existing_data_endpoints_config : \n%s \n", pformat(existing_data_endpoints_config))

existing_app_styles_config       = list( mongo_config_app_styles.find({}) )
# log_app.debug(">>> existing_app_styles_config : \n%s \n", pformat(existing_app_styles_config))

existing_routes_config           = list( mongo_config_routes.find({}) )
# log_app.debug(">>> existing_routes_config : \n%s \n", pformat(existing_routes_config))

existing_socials_config         = list( mongo_config_socials.find({}) )
# log_app.debug(">>> existing_socials_config : \n%s \n", pformat(existing_socials_config))

### setup every collection with default
setupDefaultConfig( mongo_config_global,           default_global_config )
setupDefaultConfig( mongo_config_footer,           default_app_footer )
setupDefaultConfig( mongo_config_navbar,           default_app_navbar )
setupDefaultConfig( mongo_config_data_endpoints,   default_data_endpoints_config )
setupDefaultConfig( mongo_config_app_styles,       default_app_styles_config )
setupDefaultConfig( mongo_config_routes,           default_routes_config )
setupDefaultConfig( mongo_config_socials,          default_socials_config )



def backup_mongo_collection(coll, filepath) :
  """
  dumps all documents in collection in _backups_collections 
  """

  cursor      = coll.find({})
  backup_file = open(filepath, "w")
  backup_file.write('[')
  for document in cursor:
    backup_file.write(json.dumps(document,indent=4, default=json_util.default))
    backup_file.write(',')
  backup_file.write(']')



print 



# create fields in user documents if fields doesn't exit yet
# mongo_users.update_many({'verified_as_partner'  : {"$exists" : False}}, {"$set": {'verified_as_partner'  : 'no'}})
# mongo_users.update_many({'created_at'      : {"$exists" : False}}, {"$set": {'created_at'      : datetime.datetime.now() }})
# mongo_users.update_many({'last_modified_by'    : {"$exists" : False}}, {"$set": {'last_modified_by'  : "system" }})
# mongo_users.update_many({'login_last_at'    : {"$exists" : False}}, {"$set": {'login_last_at'    : datetime.datetime.now() }})
# mongo_users.update_many({'logins_total'      : {"$exists" : False}}, {"$set": {'logins_total'    : 1 }})
# mongo_users.update_many({'follow_up_user'    : {"$exists" : False}}, {"$set": {'follow_up_user'    : "- suivi des échanges avec l'utilisateur -" }})

# mongo_users.update_many({'follow_up_user'    : {"$exists" : False}}, {"$set": {'follow_up_user'    : "- suivi des échanges avec l'utilisateur -" }})
# mongo_users.update_many({'userNewsletter'    : {"$exists" : False}}, {"$set": {'userNewsletter'    : True }})

# for user in mongo_users.find({}):
#   # mod_doc = modify_doc(doc)
#   user['userName']  = user['userName'].capitalize()
#   user['userSurname'] = user['userSurname'].capitalize()
#   mongo_users.save(user)


# create fields in feedback documents if fields doesn't exit yet
# note : files created are ignored by .gitignore
# mongo_feedbacks.update_many({'created_at'      : {"$exists" : False}}, {"$set": {'created_at'      : datetime.datetime.today() }})
# mongo_feedbacks.update_many({'follow_up_feedback'  : {"$exists" : False}}, {"$set": {'follow_up_feedback'  : "- suivi du message de l'utilisateur -" }})

# for user in mongo_feedbacks.find({}):
#   # mod_doc = modify_doc(doc)
#   user['userName']  = user['userName'].capitalize()
#   user['userSurname'] = user['userSurname'].capitalize()
#   mongo_feedbacks.save(user)

### TEMPORARY FUNCTIONS FOR CLEANING WHILE DEVELOPPING
### WARNING : COMMENT THIS BEFORE PUSHING TO PROD
# mongo_users.update_many({}, {"$set": { "last_modified_by": "" } } )
# mongo_users.update_many({}, {"$unset": { "userCreatedAt":1 } } )
# mongo_users.update_many({}, {"$unset": { "userLastModifiedAt":1 } } )


# backup all collections when restart in ./_backups_collections
cwd = os.getcwd()
log_app.debug('>>> BACKUP MONGO COLLECITONS : cwd : %s', cwd )