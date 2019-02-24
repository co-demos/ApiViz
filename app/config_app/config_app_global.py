# -*- encoding: utf-8 -*-

default_global_config = [

	{ 
    "field"       : "app_logo",
		"content"     : u"apiviz default logo",
		"url"		    	: "https://github.com/co-demos/ApiViz/blob/j_cleanviews/app/static/logos/app_default/logo_apiviz_15.png?raw=true",
		"version"     : "0.1",
    "help"        : u"The official default logo for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_title",
		"content"     : u"ApiViz",
		"version"     : "0.1",
    "help"        : u"Choose a title for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_description",
		"content"     : u"from API to a reactive website in seconds",
		"version"     : "0.1",
    "help"        : u"Choose a description for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_keywords",
		"content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",
		"version"     : "0.1",
    "help"        : u"Choose a set of keywords for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_colors",
		"content"     : {
			"primary" 	  : "purple",	
			"secondary"   : "purple",	
			"info" 		  	: "blue",	
			"warning"   	: "orange",	
			"error" 	  	: "red",	
		},
		"version"     : "0.1",
    "help"        : u"Choose a set of colors for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_typo_colors",
		"content"     : {
			"primary" 	  : "purple",	
			"secondary"   : "purple",	
			"info" 		  	: "blue",	
			"warning"   	: "orange",	
			"error" 	  	: "red",	
		},
		"version"     : "0.1",
    "help"        : u"Choose a set of colors for your typo for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_typo",
		"content"     : u"Roboto",
		"url"		    	: "",
		"version"     : "0.1",
    "help"        : u"Choose a typo for your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_indexing",
		"content"     : u"", 
		"version"     : "0.1",
    "help"        : u"Choose a token for indexing your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_code",
		"content"     : u"source code",
    "url"         : "https://github.com/co-demos/ApiViz",
		"version"     : "0.1",
    "help"        : u"Choose the repo for the source code of your ApiViz instance",
    "is_default"  : True
	},
  
	{ 
    "field"       : "app_analytics",
		"content"     : u"your_id_or_token",
    "url"         : "",
		"version"     : "0.1",
    "help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
    "is_default"  : True
	},

	{ 
    "field"       : "app_support",
		"content"     : u"your_id_or_token",
    "url"         : "",
		"version"     : "0.1",
    "help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
    "is_default"  : True
	},

]