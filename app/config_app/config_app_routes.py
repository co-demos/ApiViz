# -*- encoding: utf-8 -*-

from . import version

default_routes_config = [

	{ "field"							: "app-en-search",
		"route_title"				: u"Search",
		"route_description"	: u"apiviz default search page",
		"in_main_navbar"		: True,
		"in_footer"					: False,
		"urls"		    			: ["/app", "/app/search", "app/en/search"],
		"template_url"			: "/static/spa.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "en",
		"app_version"  			: version,
    "comment"						: u"Main search route in english",
    "is_default"				: True
	},

	{ "field"							: "app-fr-recherche",
		"route_title"				: u"Rechercher",
		"route_description"	: u"Page de recherche d'Apiviz",
		"in_main_navbar"		: True,
		"in_footer"					: False,
		"urls"		    			: ["app/fr","app/fr/search"],
		"template_url"			: "/static/spa.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "fr",
		"app_version"  			: version,
    "comment"						: u"Main search route in french",
    "is_default"				: True
	},

	{ "field"							: "app-fr-outils",
		"route_title"				: u"Outils",
		"route_description"	: u"Nos outils",
		"in_main_navbar"		: True,
		"in_footer"					: True,
		"urls"		    			: ["tools","tools/fr"],
		"template_url"			: "/static/les-outils.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "fr",
		"app_version"  			: version,
    "comment"						: u"Main tools route in french",
    "is_default"				: True
	},

	{ "field"							: "app-en-tools",
		"route_title"				: u"Tools",
		"route_description"	: u"Our tools",
		"in_main_navbar"		: True,
		"in_footer"					: True,
		"urls"		    			: ["tools/en"],
		"template_url"			: "/static/les-outils-english.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "en",
		"app_version"  			: version,
    "comment"						: u"Main tools route in english",
    "is_default"				: True
	},

]