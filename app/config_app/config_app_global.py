# -*- encoding: utf-8 -*-

from . import version

default_global_config = [

	### LOGO
	{ "field"       : "app_logo",
		"content"     : u"apiviz default logo",
		"url"		    	: "https://github.com/co-demos/ApiViz/blob/j_cleanviews/app/static/logos/app_default/logo_apiviz_15.png?raw=true",
		"app_version" : version,
    "help"        : u"The official default logo for your ApiViz instance",
    "is_default"  : True
	},

	### METAS
	{ "field"       : "app_title",
		"content"     : u"ApiViz",
		"app_version" : version,
    "help"        : u"Choose a title for your ApiViz instance",
    "is_default"  : True
	},

	{ "field"       : "app_description",
		"content"     : u"from API to a reactive website in seconds",
		"app_version" : version,
    "help"        : u"Choose a description for your ApiViz instance",
    "is_default"  : True
	},

	{ "field"       : "app_keywords",
		"content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",
		"app_version" : version,
    "help"        : u"Choose a set of keywords for your ApiViz instance",
    "is_default"  : True
	},

	### GLOBAL STYLES 
	{ "field"       : "app_colors",
		"content"     : {
			"primary" 	  : "purple",	
			"secondary"   : "purple",	
			"info" 		  	: "blue",	
			"warning"   	: "orange",	
			"error" 	  	: "red",	
		},
		"app_version" : version,
    "help"        : u"Choose a set of colors for your ApiViz instance",
    "is_default"  : True
	},

	{ "field"       : "app_typo_colors",
		"content"     : {
			"primary" 	  : "purple",	
			"secondary"   : "purple",	
			"info" 		  	: "blue",	
			"warning"   	: "orange",	
			"error" 	  	: "red",	
		},
		"app_version" : version,
    "help"        : u"Choose a set of colors for your typo for your ApiViz instance",
    "is_default"  : True
	},

	{ "field"       : "app_typo",
		"content"     : u"Roboto",
		"url"		    	: "",
		"app_version" : version,
    "help"        : u"Choose a typo for your ApiViz instance",
    "is_default"  : True
	},

	### SEO / INDEXING
	{ "field"       : "app_indexing",
		"content"     : u"", 
		"app_version" : version,
    "help"        : u"Choose a token for indexing your ApiViz instance",
    "activated"  	: False,
    "is_default"  : True
	},

	### REPO GITHUB
	{ "field"       : "app_code",
		"content"     : u"source code",
    "url"         : "https://github.com/co-demos/ApiViz",
		"app_version" : version,
    "help"        : u"Choose the repo for the source code of your ApiViz instance",
    "in_footer"  	: True,
    "is_default"  : True,
	},

	### SOCIAL NETWORKS
	{ "field"       : "app_twitter",
		"content"     : u"twitter",
    "url"         : "https://twitter.com/co-demos",
		"app_version" : version,
    "help"        : u"Choose the twitter account for your ApiViz instance",
    "in_footer"  	: True,
    "is_default"  : True
	},

	{ "field"       : "app_facebook",
		"content"     : u"facebook",
    "url"         : "https://www.facebook.com/co-demos/",
		"app_version" : version,
    "help"        : u"Choose the facebook account for your ApiViz instance",
    "in_footer"  	: True,
    "is_default"  : True
	},

	{ "field"       : "app_github",
		"content"     : u"github",
    "url"         : "https://www.github.com/co-demos/",
		"app_version" : version,
    "help"        : u"Choose the github account for your ApiViz instance",
    "in_footer"  	: True,
    "is_default"  : True
	},

	### ANALYTICS
	{ "field"       : "app_analytics",
		"content"     : u"your_id_or_token",
    "url"         : "",
		"app_version" : version,
    "help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
    "activated"  	: False,
    "is_default"  : True
	},

	{ "field"       : "app_support",
		"content"     : u"your_id_or_token",
    "url"         : "",
		"app_version" : version,
    "help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
    "activated"  	: False,
    "is_default"  : True
	},

]