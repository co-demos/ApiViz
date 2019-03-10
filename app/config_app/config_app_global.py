# -*- encoding: utf-8 -*-

from . import version

default_global_config = [

	### LANGUAGES
		{ "field"       : "app_languages",
			"languages"		: ["fr"],
			"locale"	    : "fr",
			"app_version" : version,
			"help"        : u"The default homepage for your ApiViz instance",
			"is_default"  : True
		},

	### BANNER
		{ "field"       : "app_banner",
			"locale"	    : "fr",
			"app_version" : version,
			"help"        : u"The default banner for your ApiViz instance (between navbar and filter)",
			"template_url"     : "https://github.com/co-demos/carto-sonum/blob/master/pages-html/banner-homepage.html?raw=true",
			"is_dynamic"       : False,
			"dynamic_template" : 'DynamicBanner',
			"is_visible"          : False,
			"is_dismisible"       : True,
			"is_disapearing"      : False,
			"disapearing_timeout" : 5, ## in seconds
			"is_default"     : True
		},

	### FOOTER
		{ "field"       : "app_footer",
			"app_version" : version,
			"help"        : u"The default footer for your ApiViz instance",

			"template_url"      : None,
			"is_dynamic"        : True,
			"dynamic_template"  : 'DynamicFooter',

			"contents_options" : {

				"static_texts_left"  : [
					{ 
						"is_visible"  : False, 
						"title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
						"position"    : "block_top_left", 
					}
				],
				"static_texts_middle" : [
					{ 
						"is_visible"  : False, 
						"title_block" : [{ "locale" : "fr", "text" : "Sites publics", "is_visible" : False}],
						"position"    : "block_top_middle", 
					}
				],
				"static_texts_right" : [
					{ 
						"is_visible"  : False, 
						"title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
						"position"    : "block_top_right", 
					}
				],

			},

			"ui_options" : {

					"card_color" : { "value" : "", "default" : "grey", },
					"text_color" : { "value" : "", "default" : "white", },

					"footer_logos" : [
						{ "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/logos/bloc-web-le-maire-darmanin.png?raw=true", 
						  "has_link"  : False,
							"link_to"   : "/" , 
							"position"  : "block_top_left" 
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

				"block_links_center_left" : {
					"is_visible"  : True,
					"position"    : "block_top_center_left",
					"title_block" : [{ "locale" : "fr", "text" : "L'Agence du numérique", "is_visible" : False}],
					"links"       : [

						{ "is_visible" : True, 
							"link_to"    : "https://www.agencedunumerique.gouv.fr/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "L'Agence du numérique" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://www.francethd.fr/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "Mission France Très Haut Débit" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://www.lafrenchtech.com/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "Mission French Tech" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
					]
				},

				"block_links_center_right" : {
					"is_visible"  : True,
					"position"    : "block_top_center_left",
					"title_block" : [{ "locale" : "fr", "text" : "Société numérique", "is_visible" : False}],
					"links"       : [

						{ "is_visible" : True, 
							"link_to"    : "https://societenumerique.gouv.fr/en-savoir-plus/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "En savoir plus" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://societenumerique.gouv.fr/presse/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "Presse" }],
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
						{ "is_visible" : True, 
							"link_to"    : "https://societenumerique.gouv.fr/mentions-legales/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "mentions légales" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://societenumerique.gouv.fr/accessibilite/",
							"link_type"  : "text",
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "accessibilité" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
					]
				},

				"block_links_right" : {
					"is_visible"  : True,
					"position"    : "block_top_right",
					"title_block" : [{ "locale" : "fr", "text" : "Les sites publics", "is_visible" : False}],
					"links"       : [

						{ "is_visible" : True, 
							"link_to"    : "https://www.gouvernement.fr/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "gouvernement.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://www.service-public.fr/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "service-public.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://www.legifrance.fr/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "legifrance.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://www.elysee.fr",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "elysee.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
						{ "is_visible" : True, 
							"link_to"    : "https://www.data.gouv.fr/",
							"link_type"  : "text", 
							"icon_class" : "", 
							"link_text"  : [{"locale" : "fr", "text" : "data.gouv.fr" }],
							"tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
						},
					]
				},

			},

			"is_default"  : True
		},

	### LOGO
		{ "field"       : "app_logo",
			"content"     : u"apiviz default logo in navbar",
			"url"        	: "https://github.com/co-demos/carto-sonum/blob/master/logos/logo%2Bmarianne_typo%20sombre%404x.png?raw=true",
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
						{ "dft_text" : "img_1", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgA.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_2", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgB.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_3", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgC.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_4", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgD.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_5", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgE.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_6", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgF.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
					]
				},
				{	
					"dataset_uri" : "sonum_xp",
					"images_set"  : [
						{ "dft_text" : "img_1", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgA.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_2", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgB.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_3", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgC.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_4", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgD.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_5", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgE.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
						{ "dft_text" : "img_6", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgF.png?raw=true", "credits" : "Laurie Balsan", "licence" : "" },
					]
				}
			],

			"is_default"  : True
		},

	### METAS
		{ "field"       : "app_title",
			"app_version" : version,
			"help"        : u"Choose a title for your ApiViz instance",
			"content"     : u"ApiViz",
			"is_default"  : True
		},

		{ "field"       : "app_description",
			"app_version" : version,
			"help"        : u"Choose a description for your ApiViz instance",
			"content"     : [{ "locale" : "fr", "text" : ""}],
			"is_default"  : True
		},

		{ "field"       : "app_keywords",
			"app_version" : version,
			"help"        : u"Choose a set of keywords for your ApiViz instance",
			"content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",
			"is_default"  : True
		},

	### GLOBAL CONTENTS / TEXTS
		{ "field"       : "app_welcome",
			"app_version" : version,
			"help"        : u"Choose a welcoming phrase for your ApiViz instance",
			"content"     : [{ "locale" : "fr", "text" : "Bienvenue"}],
			"is_default"  : True
		},

		{ "field"       : "app_pitch",
			"app_version" : version,
			"help"        : u"Choose a pitch/catchphrase for your ApiViz instance",
			"content"     : [{ "locale" : "fr", "text" : ""}],
			"is_default"  : True
		},

	### GLOBAL STYLES 
		{ "field"       : "app_colors",
			"content"     : { 					### AS HEXA

				### DEFAULTS
				"default_background_app"    : "#fafafa",
				"default_background_navbar" : "#ffffff",

				### SIMILI - BULMA
				"primary"     : "#513085",	
				"secondary"   : "#a174ac",	
				"info"        : "#40529d",	
				"warning"     : "#f3bd80",	
				"error"       : "#d24745",	
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
				"primary"     : "#513085",	
				"secondary"   : "#a174ac",	
				"info"        : "#40529d",	
				"warning"     : "#f3bd80",	
				"error"       : "#d24745",	
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
			"url"         : "",
			"app_version" : version,
			"help"        : u"Choose a typo for your ApiViz instance",
			"is_default"  : True
		},

	### REPO GITHUB
		{ "field"       : "app_code",
			"url"         : "https://github.com/co-demos/ApiViz",
			"app_version" : version,
			"help"        : u"Choose the repo for the source code of your ApiViz instance",
			"content"     : [{ "locale" : "fr", "text" : "Code source"}],
			"in_navbar"   : False,
			"in_footer"  	: True,
			"is_default"  : True,
		},
	
	### SEO / INDEXING
		{ "field"       : "app_indexing",
			"app_version" : version,
			"help"        : u"Choose a token for indexing your ApiViz instance",
			"content"     : u"", 
			"activated"  	: False,
			"is_default"  : True
		},

	### ANALYTICS
		{ "field"       : "app_analytics",
			"app_version" : version,
			"help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
			"content"     : u"your_id_or_token",
			"url"         : "",
			"activated"  	: False,
			"is_default"  : True
		},

	### SUPPORT 
		{ "field"       : "app_support",
			"app_version" : version,
			"help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
			"content"     : u"your_id_or_token",
			"url"         : "",
			"activated"  	: False,
			"is_default"  : True
		},

]