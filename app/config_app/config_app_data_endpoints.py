# -*- encoding: utf-8 -*-

default_data_endpoints_config = [

	{ 
    "field"    	  	: "app_data_API_auth",
		"content"   	  : u"apiviz default API endpoint for authentication",
		"root_url"			: "http://localhost:4100/api/auth/tokens/confirm_access",
		"args_options"	: ["token"],
		"version"   	  : "0.1",
    "help"      	  : u"",
    "is_default"  	: True
	},

	{ 
    "field"     	  : "app_data_API_list",
		"content"   	  : u"apiviz default API endpoint for list results",
		"root_url"			: "http://cis-openscraper/api/",
		"args_options" 	: [
			{	"arg" : "token", 						"type": "str" }, 
			{	"arg" : "page_n", 					"type": "int" }, 
			{	"arg" : "results_per_page", "type": "int" }, 
			{	"arg" : "spider_id", 				"type": "str" },
		],
		"version"				: "0.1",
    "help"      	  : u"",
    "is_default"		: True
	},

]