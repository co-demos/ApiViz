# -*- encoding: utf-8 -*-


from .. import app, PyMongo, log_app, pformat, json, json_util


# set as OK to run with app.context()
with app.app_context():

	mongo = PyMongo(app)

	log_app.info(">>> starting app --- MongoDB connected")

	### access mongodb collections ###
	# mongo_users			= mongo.db[ app.config["MONGO_COLL_USERS"] ]
	mongo_config_global					= mongo.db[ app.config["MONGO_COLL_CONFIG_GLOBAL"] ]
	mongo_config_data_endpoints	= mongo.db[ app.config["MONGO_COLL_CONFIG_DATA_ENDPOINTS"] ]
	mongo_config_data_styles		= mongo.db[ app.config["MONGO_COLL_CONFIG_DATA_STYLES"] ]
	mongo_config_routes					= mongo.db[ app.config["MONGO_COLL_CONFIG_ROUTES"] ]
	# mongo_feedbacks	= mongo.db[ app.config["MONGO_COLL_FEEDBACKS"] ]
	# mongo_join_message_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_REFERENCED_PROJECT_CARRIER"] ]
	# mongo_join_message_not_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_NOT_REFERENCED_PROJECT_CARRIER"] ]
	# mongo_join_message_structures = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_STRUCTURES"] ]

	mongoColls = {
		# "users"	: mongo_users,
		app.config["MONGO_COLL_CONFIG_GLOBAL"]					: mongo_config_global,
		app.config["MONGO_COLL_CONFIG_DATA_ENDPOINTS"]	: mongo_config_data_endpoints,
		app.config["MONGO_COLL_CONFIG_DATA_STYLES"]			: mongo_config_data_styles,
		app.config["MONGO_COLL_CONFIG_ROUTES"]					: mongo_config_routes,
		# app.config["MONGO_COLL_USERS"]								: mongo_users,
		# app.config["MONGO_COLL_FEEDBACKS"]						: mongo_feedbacks,
	}


log_app.debug(">>> MongoDB / mongoColls.keys() : \n %s", pformat( mongoColls.keys() ) )

# log_app.info(">>> MongoDB : mongo_users 		: \n %s", mongo_users  )
# log_app.info(">>> MongoDB : mongo_feedbacks 	: \n %s", mongo_feedbacks  )


### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
### CREATE DEFAULT GLOBAL CONFIG IF COLLECTION IS EMPTY
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###

from app.config_app.config_app_global import default_global_config
# from app.config_app.config_app_routes import default_global_routes
# from app.config_app.config_app_data import default_global_data

existing_app_config = list( mongo_config_global.find({}) )
log_app.debug(">>> existing_app_config : \n%s \n", pformat(existing_app_config))

for config_app_item in default_global_config : 
	print ("- - - "*10 )
	# log_app.debug(">>> config_item : \n%s", pformat(config_app_item)) 

	current_app_config_item = mongo_config_global.find_one({"field" : config_app_item["field"]})
	# log_app.debug(">>> current_app_config_item : \n%s", pformat(current_app_config_item))
	
	if current_app_config_item == None : 
		log_app.debug(">>> current_app_config_item is None --> add it...")
		mongo_config_global.insert(config_app_item)

	else : 
		if current_app_config_item["is_default"] : 
			log_app.debug(">>> current_app_config_item is default --> update it...")
			current_app_config_item_id = current_app_config_item["_id"]
			mongo_config_global.replace_one( {"_id": current_app_config_item_id}, config_app_item )




def backup_mongo_collection(coll, filepath) :
	"""
	dumps all documents in collection in _backups_collections 
	"""

	cursor 		= coll.find({})
	backup_file = open(filepath, "w")
	backup_file.write('[')
	for document in cursor:
		backup_file.write(json.dumps(document,indent=4, default=json_util.default))
		backup_file.write(',')
	backup_file.write(']')



print 
