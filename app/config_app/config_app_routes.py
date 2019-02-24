# -*- encoding: utf-8 -*-

default_routes_config = [

	{ 
		"urls"		    			: ["/app/search", "/app", "app/en/search"],
		"field"							: "app-en-search",
		"route_title"				: u"Search",
		"route_description"	: u"apiviz default search page",
		"template"					: "spa.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "en",
		"version"  			  	: "0.1",
    "comment"						: u"Main search route",
    "is_default"				: True
	},

	{ 
		"urls"		    			: ["app/fr","app/fr/search"],
		"field"							: "app-fr-search",
		"route_title"				: u"Rechercher",
		"route_description"	: u"Page de recherche d'Apiviz",
		"template"					: "spa.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "fr",
		"version"  			  	: "0.1",
    "comment"						: u"Main search route in french",
    "is_default"				: True
	},

]