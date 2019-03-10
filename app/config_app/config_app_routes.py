# -*- encoding: utf-8 -*-

from . import version

### ROUTES / PAGES 

default_routes_config = [

  ### - - - - - - - - - - - - - - - - - ###
  ### PAGES : HOME --> NEED AT LEAST ONE ROUTE AS 'is_global_app_homepage = True' / TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### - - - - - - - - - - - - - - - - - ###

  { "field"             : "app_home_fr",
    "is_global_app_homepage" : True,
    "route_title"       : u"Home",
    "route_description" : u"apiviz default home page",
    "banner" : {
      "activated"  : False,
      "banner_uri" : "default"
    },
    "in_main_navbar"    : False,
    "in_footer"         : False,
    "link_in_logo"      : True,
    "urls"              : ["/"],
    "template_url"      : "/static/spa.html",
    "help"              : u"you can specify a remote template (f.e. a github url)",
    "languages"         : ["fr"],
      "app_version"       : version,
    "comment"           : u"Main home route in french",
    "is_dynamic"        : False,
    "dynamic_template"  : None,
    "has_navbar"        : True,
    "has_footer"        : True,
      "is_default"        : True
  },

  ### - - - - - - - - - - - - - - - - - ###
  ### PAGES : DATASETS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### - - - - - - - - - - - - - - - - - ###

  ### DATASETS CARTO SONUM
    ## PAGE - map
    { "field"             : "sonum_carto_carte",
      "is_global_app_homepage" : False,
      "route_title"       : u"Rechercher",
      "route_description" : u"Page de recherche d'Apiviz",
      "banner" : {
        "activated"  : True,
        "banner_uri" : "banner_sonum_carto"
      },
      "is_dataset_homepage" : True,
      "in_main_navbar"    : True,
      "in_footer"         : False,
      "urls"              : ["/carto-sonum/carte"],
      "template_url"      : "/static/spa.html",
      "help"             : u"you can specify a remote template (f.e. a github url)",
      "languages"         : ["fr"],
        "app_version"        : version,
      "comment"           : u"Main search route in french",
      "is_dynamic"        : True,
      "dataset_uri"        : "sonum_carto",
      "dynamic_template"  : 'DynamicMap',
      "endpoint_type"     : "map",

      "contents_options"  : {

        "title"         : [{ "field" : "title",        "default" : "title",     "position" : "block_top_1",    "is_visible" : True, "trim" : 50, "locale" : "fr" }],
        "address"       : [{ "field" : "adresse",      "default" : "address",   "position" : "block_top_2",    "is_visible" : True, "trim" : 20, "locale" : "fr" }],
        "abstract"      : [{ "field" : "présentation", "default" : "abstract",  "position" : "block_middle_1", "is_visible" : True, "trim" : 50, "locale" : "fr" }],
        "tags_1"        : [{ "field" : "étiquettes",   "default" : "tags",      "position" : "block_bottom_1", "is_visible" : True, "trim" : 50, "locale" : "fr"  }],
      },

      "ui_options"        : {

        "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
        "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        "card_color"    : { "value" : "", "default" : "white", },
        "text_color"    : { "value" : "", "default" : "black", },

        "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
        "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
        "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
      },

      "links_options"  : {

        "block_data_links" : {
         "is_visible"  : False,
         "position"    : "block_bottom_1",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_data_infos" : {
         "is_visible"  : False,
         "position"    : "block_bottom_2",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_share" : {
         "is_visible"  : False,
         "position"    : "block_bottom_3",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

      },

      "has_navbar"        : True,
      "has_footer"        : True,
      "deactivate_btn"    : False,
      "is_visible"        : True,
        "is_default"      : True
    },
    ## PAGE - list
    { "field"             : "sonum_carto_liste",
      "is_global_app_homepage" : False,
      "route_title"       : u"Rechercher",
      "route_description" : u"Page de recherche d'Apiviz",
      "banner" : {
        "activated"  : False,
        "banner_uri" : "banner_sonum_carto"
      },
      "is_dataset_homepage" : False,
      "in_main_navbar"    : False,
      "in_footer"         : False,
      "urls"              : ["/carto-sonum/liste"],
      "template_url"      : "/static/spa.html",
      "help"             : u"you can specify a remote template (f.e. a github url)",
      "languages"         : ["fr"],
        "app_version"        : version,
      "comment"           : u"Main search route in french",
      "is_dynamic"        : True,
      "dataset_uri"        : "sonum_carto",
      "dynamic_template"  : 'DynamicList',
      "endpoint_type"     : "list",

      "contents_options"  : {

        "title"         : [{ "field" : "title",        "default" : "title",    "position" : "block_top_1",    "is_visible" : True, "trim" : 50, "locale" : "fr" }],
        "address"       : [{ "field" : "adresse",      "default" : "address",  "position" : "block_top_2",    "is_visible" : True, "trim" : 20, "locale" : "fr" }],
        "abstract"      : [{ "field" : "présentation", "default" : "abstract", "position" : "block_middle_1", "is_visible" : True, "trim" : 50, "locale" : "fr"}],
        "tags_1"        : [{ "field" : "étiquettes",   "default" : "tags",     "position" : "block_bottom_1", "is_visible" : True, "trim" : 50, "locale" : "fr"  }],
      },

      "ui_options"        : {

        "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
        "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        "card_color"    : { "value" : "", "default" : "white", },
        "text_color"    : { "value" : "", "default" : "black", },

        "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
        "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
        "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
      },

      "links_options"  : {

        "block_data_links" : {
         "is_visible"  : False,
         "position"    : "block_bottom_1",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_data_infos" : {
         "is_visible"  : False,
         "position"    : "block_bottom_2",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_share" : {
         "is_visible"  : False,
         "position"    : "block_bottom_3",
         "title_block" : [{ "locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : False}],
         "links"       : []
        },

      },

      "has_navbar"        : True,
      "has_footer"        : True,
      "deactivate_btn"    : False,
      "is_visible"        : True,
        "is_default"        : True
    },
    ## PAGE - detail
    { "field"             : "sonum_carto_detail",
      "is_global_app_homepage" : False,
      "route_title"        : u"Rechercher",
      "route_description"  : u"Page de recherche d'Apiviz",
      "banner" : {
        "activated"  : False,
        "banner_uri" : "banner_sonum_carto"
      },
      "is_dataset_homepage" : False,
      "in_main_navbar"    : False,
      "in_footer"         : False,
      "urls"              : ["/carto-sonum/detail"],
      "template_url"      : "/static/spa.html",
      "help"              : u"you can specify a remote template (f.e. a github url)",
      "languages"         : ["fr"],
        "app_version"        : version,
      "comment"           : u"Main search route in french",
      "is_dynamic"        : True,
      "dataset_uri"        : "sonum_carto",
      "dynamic_template"  : 'DynamicDetail',
      "endpoint_type"     : "detail",
      
      "contents_options"  : {
        
        "title"          : [{ "field" : "title",             "default" : "title",    "position" : "block_left_top_1",     "is_visible" : True,  "trim" : 0, "locale" : "fr" }],
        "address"        : [{ "field" : "adresse",           "default" : "address",  "position" : "block_left_top_2",     "is_visible" : True,  "trim" : 0, "locale" : "fr" }],
        "abstract"       : [{ "field" : "présentation",      "default" : "abstract", "position" : "block_left_middle_1",  "is_visible" : True,  "trim" : 0, "locale" : "fr" }],
        "full_text"      : [{ "field" : "détails structure", "default" : "abstract", "position" : "block_left_middle_1",  "is_visible" : False, "trim" : 0, "locale" : "fr" }],
        "tags_1"         : [{ "field" : "étiquettes",        "default" : "tags",     "position" : "block_right_bottom_1", "is_visible" : True,  "trim" : 0, "locale" : "fr" }],

        # optional text contents
        "other_contents"  : [
         { "field"       : "services",        
           "is_visible"  : True, 
           "position"    : "block_right_bottom_1", 
           "title_block" : [{ "locale" : "fr", "text" : "Services proposés", "is_visible" : False }],
         },
         { "field"       : "infos_pratiques", 
           "is_visible"  : True, 
           "position"    : "block_right_bottom_1", 
           "title_block" : [{ "locale" : "fr", "text" : "Informations pratiques", "is_visible" : False }],
         },
        ],

      },

      "ui_options"        : {

        "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
        "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
        "card_color"     : { "value" : "", "default" : "white", },
        "text_color"     : { "value" : "", "default" : "black", },
        
        "link_to_detail"   : { "is_visible" : False, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
        "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
        "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },

      },

      "links_options"  : {

        "block_data_links" : {
         "is_visible"  : True,
         "position"    : "block_left_middle_2",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : [
           { "field" : "website", 
             "is_visible" : True, 
             "link_type"  : "text", 
             "icon_class" : "", 
             "link_text"  : [{"locale" : "fr", "text" : "website" }],
             "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
           },
           { "field" : "contact", 
             "is_visible" : True, 
             "link_type"  : "text", 
             "icon_class" : "", 
             "link_text"  : [{"locale" : "fr", "text" : "contact" }],
             "tooltip"    : [{"locale" : "fr", "text" : "contacter la structure" }] 
           },
         ]
        },

        "block_share" : {
         "is_visible"  : True,
         "position"    : "block_left_bottom_2",
         "title_block" : [{ "locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : True}],
         "links"       : [
           {
             "is_visible" : True, 
             "link_type"  : "icon", 
             "icon_class" : "fas fa-link", 
             "link_text"  : [{"locale" : "fr", "text" : "lien" }],
             "tooltip"    : [{"locale" : "fr", "text" : "partager cette page (copier le lien)" }] 
           },
          {
             "is_visible" : True, 
             "link_type"  : "icon", 
             "icon_class" : "fab fa-facebook-f", 
             "link_text"  : [{"locale" : "fr", "text" : "facebook" }],
             "tooltip"    : [{"locale" : "fr", "text" : "partager sur facebook" }] 
           },
           {
             "is_visible" : True, 
             "link_type"  : "icon", 
             "icon_class" : "fab fa-twitter", 
             "link_text"  : [{"locale" : "fr", "text" : "twitter" }],
             "tooltip"    : [{"locale" : "fr", "text" : "partager sur twitter" }] 
           },
         ]
        },

      },

      "has_navbar"        : True,
      "has_footer"        : True,
      "deactivate_btn"    : False,
      "is_visible"        : True,
        "is_default"        : True
    },

  ### DATASETS XP SONUM
    ## PAGE - map
    { "field"             : "sonum_xp_carte",
      "is_global_app_homepage" : False,
      "route_title"        : u"Rechercher",
      "route_description"  : u"Page de recherche d'Apiviz",
      "banner" : {
        "activated"  : False,
        "banner_uri" : "banner_sonum_xp"
      },
      "is_dataset_homepage" : False,
      "in_main_navbar"    : True,
      "in_footer"         : False,
      "urls"              : ["/xp-sonum/carte"],
      "template_url"      : "/static/spa.html",
      "help"             : u"you can specify a remote template (f.e. a github url)",
      "languages"         : ["fr"],
        "app_version"        : version,
      "comment"           : u"Main search route in french",
      "is_dynamic"        : True,
      "dataset_uri"        : "sonum_xp",
      "dynamic_template"  : 'DynamicMap',
      "endpoint_type"     : "map",

      "contents_options"  : {

        "title"         : [{ "field" : "title",        "default" : "title",     "position" : "block_top_1",    "is_visible" : True, "trim" : 50, "locale" : "fr" }],
        "address"       : [{ "field" : "adresse",      "default" : "address",   "position" : "block_top_2",    "is_visible" : True, "trim" : 20, "locale" : "fr" }],
        "abstract"      : [{ "field" : "présentation", "default" : "abstract",  "position" : "block_middle_1", "is_visible" : True, "trim" : 50, "locale" : "fr" }],
        "tags_1"        : [{ "field" : "étiquettes",   "default" : "tags",      "position" : "block_bottom_1", "is_visible" : True, "trim" : 50, "locale" : "fr"  }],
      },

      "ui_options"        : {

        "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
        "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        "card_color"    : { "value" : "", "default" : "white", },
        "text_color"    : { "value" : "", "default" : "black", },

        "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
        "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
        "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
      },

      "links_options"  : {

        "block_data_links" : {
         "is_visible"  : False,
         "position"    : "block_bottom_1",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_data_infos" : {
         "is_visible"  : False,
         "position"    : "block_bottom_2",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_share" : {
         "is_visible"  : False,
         "position"    : "block_bottom_3",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

      },

      "has_navbar"        : True,
      "has_footer"        : True,
      "deactivate_btn"    : False,
      "is_visible"        : True,
        "is_default"        : True
    },
    ## PAGE - list
    { "field"             : "sonum_xp_liste",
      "is_global_app_homepage" : False,
      "route_title"        : u"Rechercher",
      "route_description"  : u"Page de recherche d'Apiviz",
      "banner" : {
        "activated"  : True,
        "banner_uri" : "banner_sonum_xp"
      },
      "is_dataset_homepage" : True,
      "in_main_navbar"    : False,
      "in_footer"         : False,
      "urls"              : ["/xp-sonum/liste"],
      "template_url"      : "/static/spa.html",
      "help"             : u"you can specify a remote template (f.e. a github url)",
      "languages"         : ["fr"],
        "app_version"        : version,
      "comment"           : u"Main search route in french",
      "is_dynamic"        : True,
      "dataset_uri"        : "sonum_xp",
      "dynamic_template"  : 'DynamicList',
      "endpoint_type"     : "list",


      "contents_options"  : {

        "title"         : [{ "field" : "title",        "default" : "title",    "position" : "block_top_1",    "is_visible" : True, "trim" : 50, "locale" : "fr" }],
        "address"       : [{ "field" : "adresse",      "default" : "address",  "position" : "block_top_2",    "is_visible" : True, "trim" : 20, "locale" : "fr" }],
        "abstract"      : [{ "field" : "présentation", "default" : "abstract", "position" : "block_middle_1", "is_visible" : True, "trim" : 50, "locale" : "fr"}],
        "tags_1"        : [{ "field" : "étiquettes",   "default" : "tags",     "position" : "block_bottom_1", "is_visible" : True, "trim" : 50, "locale" : "fr"  }],
      },

      "ui_options"        : {

        "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
        "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        "card_color"    : { "value" : "", "default" : "white", },
        "text_color"    : { "value" : "", "default" : "black", },

        "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
        "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
        "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
      },

      "links_options"  : {

        "block_data_links" : {
         "is_visible"  : False,
         "position"    : "block_bottom_1",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_data_infos" : {
         "is_visible"  : False,
         "position"    : "block_bottom_2",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : []
        },

        "block_share" : {
         "is_visible"  : False,
         "position"    : "block_bottom_3",
         "title_block" : [{ "locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : False}],
         "links"       : []
        },

      },


      "has_navbar"        : True,
      "has_footer"        : True,
      "deactivate_btn"    : False,
      "is_visible"        : True,
        "is_default"        : True
    },
    ## PAGE - detail
    { "field"             : "sonum_xp_detail",
      "is_global_app_homepage" : False,
      "route_title"       : u"Rechercher",
      "route_description" : u"Page de recherche d'Apiviz",
      "is_dataset_homepage" : False,
      "banner" : {
        "activated"  : False,
        "banner_uri" : "banner_sonum_xp"
      },
      "in_main_navbar"    : False,
      "in_footer"         : False,
      "urls"              : ["/xp-sonum/detail"],
      "template_url"      : "/static/spa.html",
      "help"              : u"you can specify a remote template (f.e. a github url)",
      "languages"         : ["fr"],
        "app_version"        : version,
      "comment"           : u"Main search route in french",
      "is_dynamic"        : True,
      "dataset_uri"        : "sonum_xp",
      "dynamic_template"  : 'DynamicDetail',
      "endpoint_type"     : "detail",

      "contents_options"  : {
        
        "title"          : [{ "field" : "title",             "default" : "title",    "position" : "block_left_top_1",     "is_visible" : True,  "trim" : 0, "locale" : "fr" }],
        "address"        : [{ "field" : "adresse",           "default" : "address",  "position" : "block_left_top_2",     "is_visible" : True,  "trim" : 0, "locale" : "fr" }],
        "abstract"       : [{ "field" : "présentation",      "default" : "abstract", "position" : "block_left_middle_1",  "is_visible" : True,  "trim" : 0, "locale" : "fr" }],
        "full_text"      : [{ "field" : "détails structure", "default" : "abstract", "position" : "block_left_middle_1",  "is_visible" : False, "trim" : 0, "locale" : "fr" }],
        "tags_1"         : [{ "field" : "étiquettes",        "default" : "tags",     "position" : "block_right_bottom_1", "is_visible" : True,  "trim" : 0, "locale" : "fr" }],

        # optional text contents
        "other_contents"  : [
         { "field"       : "services",        
           "is_visible"  : True, 
           "position"    : "block_right_bottom_1", 
           "title_block" : [{ "locale" : "fr", "text" : "Services proposés", "is_visible" : False }],
         },
         { "field"       : "infos_pratiques", 
           "is_visible"  : True, 
           "position"    : "block_right_bottom_1", 
           "title_block" : [{ "locale" : "fr", "text" : "Informations pratiques", "is_visible" : False }],
         },
        ],

      },

      "ui_options"        : {

        "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
        "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
        "card_color"     : { "value" : "", "default" : "white", },
        "text_color"     : { "value" : "", "default" : "black", },
        
        "link_to_detail"   : { "is_visible" : False, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
        "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
        "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },

      },

      "links_options"  : {

        "block_data_links" : {
         "is_visible"  : True,
         "position"    : "block_left_middle_2",
         "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
         "links"       : [
           { "field" : "website", 
             "is_visible" : True, 
             "link_type"  : "text", 
             "icon_class" : "", 
             "link_text"  : [{"locale" : "fr", "text" : "website" }],
             "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
           },
           { "field" : "contact", 
             "is_visible" : True, 
             "link_type"  : "text", 
             "icon_class" : "", 
             "link_text"  : [{"locale" : "fr", "text" : "contact" }],
             "tooltip"    : [{"locale" : "fr", "text" : "contacter la structure" }] 
           },
         ]
        },

        "block_share" : {
         "is_visible"  : True,
         "position"    : "block_left_bottom_2",
         "title_block" : [{ "locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : True}],
         "links"       : [
            {
              "is_visible" : True, 
              "link_type"  : "icon", 
              "icon_class" : "fas fa-link", 
              "link_text"  : [{"locale" : "fr", "text" : "lien" }],
              "tooltip"    : [{"locale" : "fr", "text" : "partager cette page (copier le lien)" }] 
            },
            {
              "is_visible" : True, 
              "link_type"  : "icon", 
              "icon_class" : "fab fa-facebook-f", 
              "link_text"  : [{"locale" : "fr", "text" : "facebook" }],
              "tooltip"    : [{"locale" : "fr", "text" : "partager sur facebook" }] 
            },
            {
              "is_visible" : True, 
              "link_type"  : "icon", 
              "icon_class" : "fab fa-twitter", 
              "link_text"  : [{"locale" : "fr", "text" : "twitter" }],
              "tooltip"    : [{"locale" : "fr", "text" : "partager sur twitter" }] 
            },
          ]
        },

      },

      "has_navbar"        : True,
      "has_footer"        : True,
      "deactivate_btn"    : False,
      "is_visible"        : True,
        "is_default"        : True
    },


  ### - - - - - - - - - - - - - - - - - ###
  ### CUSTOM ROUTES-PAGES --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### - - - - - - - - - - - - - - - - - ###

  ### PAGE : QUI SOMMES-NOUS
  { "field"             : "app_who_fr",
    "is_global_app_homepage" : False,
    "route_title"        : u"Home",
    "route_description"  : u"Qui sommes-nous",
    "banner" : {
      "activated"  : False,
      "banner_uri" : "default"
    },
    "is_dataset_homepage" : False,
    "in_main_navbar"    : True,
    "in_footer"         : False,
    "link_in_logo"      : False,
    "urls"              : ["/qui-sommes-nous"],
    "template_url"      : "https://github.com/co-demos/carto-sonum/blob/master/pages-html/qui-sommes-nous.html?raw=true",
    "help"             : u"you can specify a remote template (f.e. a github url)",
    "languages"         : ["fr"],
      "app_version"        : version,
    "comment"           : u"A custom page for your ApiViz app",
    "is_dynamic"        : True,
    "dynamic_template"  : 'DynamicStatic',
    "has_navbar"        : True,
    "has_footer"        : True,
      "is_default"        : True
  },

  ### PAGES : TOOLS
  { "field"             : "app_outils",
    "is_global_app_homepage" : False,
    "route_title"        : u"Outils",
    "route_description"  : u"Nos outils",
    "banner" : {
      "activated"  : False,
      "banner_uri" : "default"
    },
    "is_dataset_homepage" : False,
    "in_main_navbar"    : False,
    "in_footer"         : True,
    "urls"              : ["/nos-outils"],
    "template_url"      : "/static/les-outils.html",
    "help"             : u"you can specify a remote template (f.e. a github url)",
    "languages"         : ["fr"],
      "app_version"        : version,
    "comment"           : u"Main tools route in french",
    "is_dynamic"        : False,
    "dynamic_template"  : None,
    "has_navbar"        : True,
    "has_footer"        : True,
      "is_default"        : True
  },

  ### ...
]