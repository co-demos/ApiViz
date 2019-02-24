# -*- encoding: utf-8 -*-

from . import version

default_data_endpoints_config = [

	### USER MANAGEMENT

	{ "field"    	  	: "app_data_API_user_auth",
		"data_type" 		: "user",
		"content"   	  : u"apiviz default API endpoint for user authentication",
		"root_url"			: "http://localhost:4100/api/auth/tokens/confirm_access",
		"args_options"	: [
			{ "arg" : "token", 		"type" : "str" },
		],
		"app_version"   	: version,
    "help"      	  : u"define the endpoint for a JWT check / ",
    "is_default"  	: True
	},

	{ "field"    	  	: "app_data_API_user_register",
		"data_type" 		: "user",
		"content"   	  : u"apiviz default API endpoint for login",
		"root_url"			: "http://localhost:4100/api/usr/register",
		"args_options"	: [
			{ "arg" : "token", 		"type" : "str" },
		],
		"app_version"   	: version,
    "help"      	  : u"define the endpoint for registering a new user",
		"need_form"			: True,
    "is_default"  	: True
	},

	{ "field"    	  	: "app_data_API_user_login",
		"data_type" 		: "user",
		"content"   	  : u"apiviz default API endpoint for login",
		"root_url"			: "http://localhost:4100/api/usr/login",
		"args_options"	: [
			{ "arg" : "token", 		"type" : "str" },
		],
		"app_version"   	: version,
    "help"      	  : u"define the endpoint for login an user",
		"need_form"			: True,
    "is_default"  	: True
	},

	{ "field"    	  	: "app_data_API_user_infos",
		"data_type" 		: "user",
		"content"   	  : u"apiviz default API endpoint for user infos",
		"root_url"			: "http://localhost:4100/api/usr/register",
		"args_options"	: [
			{ "arg" : "token", 		"type" : "str" },
			{ "arg" : "doc_id", 	"type" : "str"}
		],
		"app_version"   	: version,
    "help"      	  : u"define the endpoint to get data for : an user ",
    "is_default"  	: True
	},

	### DATA ENDPOINTS

	{ "field"     	  : "app_data_API_list",
		"data_type" 		: "data",
		"content"   	  : u"apiviz default API endpoint for list results",
		"root_url"			: "http://cis-openscraper/api/data",
		"args_options" 	: [
			{	"arg" : "token", 						"type": "str" }, 
			{	"arg" : "spider_id", 				"type": "str" },
			{	"arg" : "page_n", 					"type": "int" }, 
			{	"arg" : "results_per_page", "type": "int" }, 
		],
		"app_version"		: "0.1",
    "help"      	  : u"define the endpoint to get data for : a view list",
    "is_default"		: True
	},

	{ "field"     	  : "app_data_API_detail",
		"data_type" 		: "data",
		"content"   	  : u"apiviz default API endpoint for detailled results",
		"root_url"			: "http://cis-openscraper/api/data",
		"args_options" 	: [
			{	"arg" : "item_id", 	"type": "str" }, 
		],
		"app_version"		: "0.1",
    "help"      	  : u"define the endpoint to get data for : a detailled data",
    "is_default"		: True
	},

	{ "field"     	  : "app_data_API_stats",
		"data_type" 		: "data",
		"content"   	  : u"apiviz default API endpoint for stats results",
		"root_url"			: "http://cis-openscraper/api/infos",
		"args_options" 	: [
			{	"arg" : "only_counts_simple", 	"type": "bool" }, 
			{	"arg" : "only_tags_stats", 			"type": "bool" }, 
			{	"arg" : "only_spiders_stats", 	"type": "bool" }, 
		],
		"app_version"		: "0.1",
    "help"      	  : u"define the endpoint to get data for : a stat about the dataset",
    "is_default"		: True
	},

	{ "field"     	  : "app_data_API_map",
		"data_type" 		: "data",
		"content"   	  : u"apiviz default API endpoint for map results",
		"root_url"			: "http://cis-openscraper/api/data",
		"args_options" 	: [
			{	"arg" : "token", 						"type": "str" }, 
			{	"arg" : "page_n", 					"type": "int" }, 
			{	"arg" : "results_per_page", "type": "int" }, 
			{	"arg" : "spider_id", 				"type": "str" },
		],
		"app_version"		: "0.1",
    "help"      	  : u"define the endpoint to get data for : map results",
    "is_default"		: True
	},
]