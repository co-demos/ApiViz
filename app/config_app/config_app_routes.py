# -*- encoding: utf-8 -*-

from . import version

### ROUTES / PAGES 

default_routes_config = [

	### - - - - - - - - - - - - - - - - - ###
	### PAGES HOME
	### - - - - - - - - - - - - - - - - - ###

	{ "field"							: "app-fr-home",
		"route_title"				: u"Home",
		"route_description"	: u"apiviz default home page",
		"is_global_app_homepage" : True,
		"is_project_homepage": True,
		"in_main_navbar"		: False,
		"in_footer"					: False,
		"link_in_logo"			: True,
		"urls"		    			: ["/"],
		"template_url"			: "/static/spa.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "fr",
			"app_version"  			: version,
    "comment"						: u"Main home route in french",
		"is_dynamic"				: False,
		"dynamic_template"	: 'DynamicStatic',
		"has_navbar"				: True,
		"has_footer"				: True,
    	"is_default"				: True
	},

	### - - - - - - - - - - - - - - - - - ###
	### PAGES DATASETS
	### - - - - - - - - - - - - - - - - - ###

	### DATASETS CARTO SONUM
		{ "field"							: "carto-sonum-carte",
			"route_title"				: u"Rechercher",
			"route_description"	: u"Page de recherche d'Apiviz",
			"is_project_homepage": True,
			"in_main_navbar"		: True,
			"in_footer"					: False,
			"urls"		    			: ["/carto-sonum/carte"],
			"template_url"			: "/static/spa.html",
			"help"							: u"you can specify a remote template (f.e. a github url)",
			"language"					: "fr",
				"app_version"  			: version,
			"comment"						: u"Main search route in french",
			"is_dynamic"				: True,
			"dataset_uri"				: "sonum-carto",
			"dynamic_template"	: 'DynamicMap',
			"has_navbar"				: True,
			"has_footer"				: True,
			"deactivate_btn"		: False,
			"is_visible"				: True,
				"is_default"				: True
		},
		{ "field"							: "carto-sonum-liste",
			"route_title"				: u"Rechercher",
			"route_description"	: u"Page de recherche d'Apiviz",
			"is_project_homepage": False,
			"in_main_navbar"		: False,
			"in_footer"					: False,
			"urls"		    			: ["/carto-sonum/liste"],
			"template_url"			: "/static/spa.html",
			"help"							: u"you can specify a remote template (f.e. a github url)",
			"language"					: "fr",
				"app_version"  			: version,
			"comment"						: u"Main search route in french",
			"is_dynamic"				: True,
			"dataset_uri"				: "sonum-carto",
			"dynamic_template"	: 'DynamicList',
			"has_navbar"				: True,
			"has_footer"				: True,
			"deactivate_btn"		: False,
			"is_visible"				: True,
				"is_default"				: True
		},
		{ "field"							: "carto-sonum-detail",
			"route_title"				: u"Rechercher",
			"route_description"	: u"Page de recherche d'Apiviz",
			"is_project_homepage": False,
			"in_main_navbar"		: False,
			"in_footer"					: False,
			"urls"		    			: ["/carto-sonum/detail"],
			"template_url"			: "/static/spa.html",
			"help"							: u"you can specify a remote template (f.e. a github url)",
			"language"					: "fr",
				"app_version"  			: version,
			"comment"						: u"Main search route in french",
			"is_dynamic"				: True,
			"dataset_uri"				: "sonum-carto",
			"dynamic_template"	: 'DynamicDetail',
			"has_navbar"				: True,
			"has_footer"				: True,
			"deactivate_btn"		: False,
			"is_visible"				: True,
				"is_default"				: True
		},

	### DATASETS XP SONUM
		{ "field"							: "xp-sonum-carte",
			"route_title"				: u"Rechercher",
			"route_description"	: u"Page de recherche d'Apiviz",
			"is_project_homepage": False,
			"in_main_navbar"		: True,
			"in_footer"					: False,
			"urls"		    			: ["/xp-sonum/carte"],
			"template_url"			: "/static/spa.html",
			"help"							: u"you can specify a remote template (f.e. a github url)",
			"language"					: "fr",
				"app_version"  			: version,
			"comment"						: u"Main search route in french",
			"is_dynamic"				: True,
			"dataset_uri"				: "sonum-xp",
			"dynamic_template"	: 'DynamicMap',
			"has_navbar"				: True,
			"has_footer"				: True,
			"deactivate_btn"		: False,
			"is_visible"				: True,
				"is_default"				: True
		},
		{ "field"							: "xp-sonum-liste",
			"route_title"				: u"Rechercher",
			"route_description"	: u"Page de recherche d'Apiviz",
			"is_project_homepage": True,
			"in_main_navbar"		: False,
			"in_footer"					: False,
			"urls"		    			: ["/xp-sonum/liste"],
			"template_url"			: "/static/spa.html",
			"help"							: u"you can specify a remote template (f.e. a github url)",
			"language"					: "fr",
				"app_version"  			: version,
			"comment"						: u"Main search route in french",
			"is_dynamic"				: True,
			"dataset_uri"				: "sonum-xp",
			"dynamic_template"	: 'DynamicList',
			"has_navbar"				: True,
			"has_footer"				: True,
			"deactivate_btn"		: False,
			"is_visible"				: True,
				"is_default"				: True
		},
		{ "field"							: "xp-sonum-detail",
			"route_title"				: u"Rechercher",
			"route_description"	: u"Page de recherche d'Apiviz",
			"is_project_homepage": False,
			"in_main_navbar"		: False,
			"in_footer"					: False,
			"urls"		    			: ["/xp-sonum/detail"],
			"template_url"			: "/static/spa.html",
			"help"							: u"you can specify a remote template (f.e. a github url)",
			"language"					: "fr",
				"app_version"  			: version,
			"comment"						: u"Main search route in french",
			"is_dynamic"				: True,
			"dataset_uri"				: "sonum-xp",
			"dynamic_template"	: 'DynamicDetail',
			"has_navbar"				: True,
			"has_footer"				: True,
			"deactivate_btn"		: False,
			"is_visible"				: True,
				"is_default"				: True
		},


	### - - - - - - - - - - - - - - - - - ###
	### CUSTOM ROUTES-PAGES --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
	### - - - - - - - - - - - - - - - - - ###

	### PAGES TOOLS
	{ "field"							: "app-outils",
		"route_title"				: u"Outils",
		"route_description"	: u"Nos outils",
		"is_project_homepage": False,
		"in_main_navbar"		: False,
		"in_footer"					: True,
		"urls"		    			: ["/tools"],
		"template_url"			: "/static/les-outils.html",
		"help"							: u"you can specify a remote template (f.e. a github url)",
		"language"					: "fr",
			"app_version"  			: version,
    "comment"						: u"Main tools route in french",
		"is_dynamic"				: False,
		"dynamic_template"	: 'DynamicStatic',
		"has_navbar"				: True,
		"has_footer"				: True,
    	"is_default"				: True
	},

	### ...
]