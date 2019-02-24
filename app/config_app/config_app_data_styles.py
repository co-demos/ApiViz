# -*- encoding: utf-8 -*-

from . import version

default_data_styles_config = [

	{ "field"       : "app_data_list_block",
		"content"     : u"apiviz default block",
		"version"     : "0.1",
    "help"        : u"define the options for an item card in list view",
		"options"			: {
			"background_color" : "",
		},
    "is_default"  : True
	},

	{ "field"       : "app_data_filter_navbar",
		"content"     : u"apiviz default filter",
		"version"     : "0.1",
    "help"        : u"define the options for the filter navbar",
		"options"			: {
			"background_color" : "",
		},
    "is_default"  : True
	},

]