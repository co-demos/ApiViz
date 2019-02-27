# -*- encoding: utf-8 -*-

from . import version

default_data_styles_config = [

	### TO DO --> ADD OPTIONS FOR EACH VIEW 

	### - - - - - - - - - - - - - - - ###
	### FILTERS
	### - - - - - - - - - - - - - - - ###
	{ "field"       : "app_data_filter_navbar",
		"content"     : u"apiviz default filter config",
		"version"     : version,
    "help"        : u"define the options for the filter navbar",
		"options"			: {
			"background_color" : "",
		},
    "is_default"  : True
	},

	### - - - - - - - - - - - - - - - ###
	### VIEWS
	### - - - - - - - - - - - - - - - ###

	### VIEW LIST
	{ "field"       : "app_data_list_view",
		"content"     : u"apiviz default config for list view",
		"version"     : version,
    "help"        : u"define the options for the list view",
		"options"			: {
			"background_color"	: "",
			"background_img"		: "",
			"primary_img"				: "",
			"secondary_img"			: "",
		},
		"visible"			: True,
		"disabled"		: False,
    "is_default"  : True
	},

	### VIEW DETAIL
	{ "field"       : "app_data_detail_view",
		"content"     : u"apiviz default detailled view config",
		"version"     : version,
    "help"        : u"define the options for the detailled view",
		"options"			: {
			"blocks_fields" : [
				"title",
				"resume",
				"link"
			],
		},
		"visible"			: True,
		"disabled"		: False,
    "is_default"  : True
	},

	### VIEW MAP
	{ "field"       : "app_data_map_view",
		"content"     : u"apiviz default map config",
		"version"     : version,
    "help"        : u"define the options for the map view",
		"options"			: {
			"map_layout" : "",
		},
		"visible"			: True,
		"disabled"		: False,
    "is_default"  : True
	},

	### VIEW STAT
	{ "field"       : "app_data_stat_view",
		"content"     : u"apiviz default map config",
		"version"     : version,
    "help"        : u"define the options for the map view",
		"options"			: {
			"map_layout" : "",
		},
		"visible"			: False,
		"disabled"		: True,
    "is_default"  : True
	},

]