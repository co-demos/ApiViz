# -*- encoding: utf-8 -*-

from . import version

default_global_config = [

	### LANGUAGES
		{ "field"       : "app_languages",
			"languages"		: ["en", "fr"],
			"default_lan"	: "fr",
			"app_version" : version,
			"help"        : u"The default homepage for your ApiViz instance",
			"is_default"  : True
		},

	### BANNER
		{ "field"       : "app_banner",
			"languages"		: ["fr"],
			"default_lan"	: "fr",
			"app_version" : version,
			"help"        : u"The default banner for your ApiViz instance (between navbar and filter)",
			"template_url"      : "/static/spa.html",
			"is_dynamic"        : False,
			"dynamic_template"  : 'DynamicBanner',
			"is_visible"          : False,
			"is_dismisible"       : True,
			"is_disapearing"      : False,
			"disapearing_timeout" : 5, ## in seconds
			"is_default"     : True
		},

	### FOOTER
		{ "field"       : "app_footer",
			"languages"		: ["fr"],
			"default_lan"	: "fr",
			"app_version" : version,
			"help"        : u"The default footer for your ApiViz instance",

			"template_url"      : "/static/spa.html",
			"is_dynamic"        : False,
			"dynamic_template"  : 'DynamicFooter',

			"contents_options" : {

				"static_texts_left"  : [
					{ "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
						"position"    : "block_top_left", 
						"is_visible"  : False, 
						"locale"      : "fr" 
					}
				],
				"static_texts_middle" : [
					{ "title_block" : [{ "locale" : "fr", "text" : "Sites publics", "is_visible" : False}],
						"position"    : "block_top_middle", 
						"is_visible"  : False, 
						"locale"      : "fr" 
					}
				],
				"static_texts_right" : [
					{ "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
						"position"    : "block_top_right", 
						"is_visible"  : False, 
						"locale"      : "fr" 
					}
				],

			},

			"ui_options" : {

					"card_color" : { "value" : "", "default" : "grey", },
					"text_color" : { "value" : "", "default" : "white", },

					"footer_logos" : [
						{ "src_image" : "", 
						  "link_to" : "/" , 
							"position" : "block_top_left" 
						}
					],

			},

			"links_options" : {

				"block_links_left" : {
					"is_visible"  : False,
					"position"    : "block_top_left",
					"title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
					"links"       : []
				},

				"block_links_middle" : {
					"is_visible"  : True,
					"position"    : "block_top_right",
					"title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
					"links"       : [

						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "gouvernement.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "service-public.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "legifrance.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "data.gouv.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "elysee.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "société numérique" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "kit d'intervention rapide" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "plateforme des territoires" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},

					]
				},

				"block_links_right" : {
					"is_visible"  : True,
					"position"    : "block_top_right",
					"title_block" : [{ "locale" : "fr", "text" : "accessibilité", "is_visible" : False}],
					"links"       : [

						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text",
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "accessibilité" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "mentions légales" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},

					]
				},

			},

			"is_default"  : True
		},

	### LOGO
		{ "field"       : "app_logo",
			"content"     : u"apiviz default logo",
			"url"		    	: "https://github.com/co-demos/ApiViz/blob/develop/app/static/logos/app_default/logo_apiviz_15.png?raw=true",
			"app_version" : version,
			"help"        : u"The official default logo for your ApiViz instance",
			"is_default"  : True
		},

	### DEFAULT IMAGES FOR DATASETS SEARCH
		{ "field"       : "app_default_search_images_sets",
			"app_version" : version,
			"help"        : u"The default images sets for the cards for each dataset",

			"images_sets" : [
				{ 
					"dataset_uri" : "sonum_carto",
					"images_set"  : [
						{ "dft_text" : "img_1", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_2", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_3", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_4", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_5", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
					]
				},
				{	
					"dataset_uri" : "sonum_xp",
					"images_set"  : [
						{ "dft_text" : "img_1", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_2", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_3", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_4", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_5", "src_image" : "/", "credits" : "Laurie Balsan", "licence" : "" },
					]
				}
			],

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
			"content"     : u"from API data to a reactive website in seconds",
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

	### GLOBAL CONTENTS / TEXTS
		{ "field"       : "app_welcome",
			"content"     : {
				"en" 	: u"Welcome to ApiViz",
				"fr"	: u"Bienvenue sur ApiViz",
			},
			"app_version" : version,
			"help"        : u"Choose a welcoming phrase for your ApiViz instance",
			"is_default"  : True
		},

		{ "field"       : "app_pitch",
			"content"     : {
				"en" 	: u"from API data to a reactive website in seconds",
				"fr"	: u"transformer les données d'une API en un site réactif en quelques secondes",
			},
			"app_version" : version,
			"help"        : u"Choose a pitch/catchphrase for your ApiViz instance",
			"is_default"  : True
		},

	### GLOBAL STYLES 
		{ "field"       : "app_colors",
			"content"     : { 					### AS HEXA

				### DEFAULTS
				"default_background_app"    : "#fafafa",
				"default_background_navbar" : "#ffffff",

				### SIMILI - BULMA
				"primary" 	  : "#513085",	
				"secondary"   : "#a174ac",	
				"info" 		  	: "#40529d",	
				"warning"   	: "#f3bd80",	
				"error" 	  	: "#d24745",	
				### EXTRA COLORS
				"dark_blue"   : "#40529d",
				"light_pink"  : "#e89db1",
				"light_blue"  : "#a3b1d7",
				"deep_blue"   : "#21295e",
			},
			"app_version" : version,
			"help"        : u"Choose a set of colors (an hexa for example) for your ApiViz instance",
			"is_default"  : True
		},

		{ "field"       : "app_typo_colors",
			"content"     : {
				
				"default_dark"       : "#000000",
				"default_light_dark" : "#3D3A39",
				"default_invert"     : "#ffffff",

				### SIMILI - BULMA
				"primary" 	  : "#513085",	
				"secondary"   : "#a174ac",	
				"info" 		  	: "#40529d",	
				"warning"   	: "#f3bd80",	
				"error" 	  	: "#d24745",	
				### EXTRA COLORS
				"dark_blue"   : "#40529d",
				"light_pink"  : "#e89db1",
				"light_blue"  : "#a3b1d7",
				"deep_blue"   : "#21295e",
			},
			"app_version" : version,
			"help"        : u"Choose a set of colors for your typo for your ApiViz instance",
			"is_default"  : True
		},

		{ "field"       : "app_typo",
			"content"     : {
				"titles" : u"BonvenoCF-Light",
				"textes" : u"NEXA SANS",
			},
			"url"		    	: "",
			"app_version" : version,
			"help"        : u"Choose a typo for your ApiViz instance",
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
	
	### SEO / INDEXING
		{ "field"       : "app_indexing",
			"content"     : u"", 
			"app_version" : version,
			"help"        : u"Choose a token for indexing your ApiViz instance",
			"activated"  	: False,
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

	### SUPPORT 
		{ "field"       : "app_support",
			"content"     : u"your_id_or_token",
			"url"         : "",
			"app_version" : version,
			"help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
			"activated"  	: False,
			"is_default"  : True
		},

]