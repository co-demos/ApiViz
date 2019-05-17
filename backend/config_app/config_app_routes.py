# -*- encoding: utf-8 -*-

from . import version

### ROUTES / PAGES

default_routes_config = [


  ### - - - - - - - - - - - - - - - - - - -  ### 
  ### CONFIG SONUM 
  ### - - - - - - - - - - - - - - - - - - -  ### 

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : HOME --> NEED AT LEAST ONE ROUTE AS 'is_global_app_homepage = True' / TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_home_fr",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : True,
          "banner_uri" : "banner-sonum-carto"
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_left",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : ["/"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/test-apiviz.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main home route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : DATASETS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### DATASETS CARTO SONUM

        ### PAGE PROJECT
        { "field"             : "sonum_carto_project",
          "is_global_app_homepage" : True,
          "route_title"       : u"Home",
          "route_description" : u"apiviz default home page",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-carto"
          },
          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "link_in_logo"      : True,
          "urls"              : ["/sonum-carto/projet"],
          "template_url"      : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/sonum-carto-projet.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"       : version,
          "comment"           : u"Main project route in french",
          "is_dynamic"        : True,
          "dynamic_template"  : "DynamicStatic",
          "has_navbar"        : True,
          "has_footer"        : True,

          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },

        ## PAGE - map
        { "field"             : "sonum_carto_carte",
          "is_global_app_homepage" : False,
          "route_title"       : u"Rechercher",
          "route_description" : u"Page de recherche d'Apiviz",
          "route_activated"   : True,
          "banner" : {
            "activated"  : True,
            "banner_uri" : "banner-sonum-carto"
          },
          "is_dataset_homepage" : True,

          "in_main_navbar"    : True,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : False,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-carto/carte"],
          "template_url"      : "/static/spa.html",
          "help"             : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"        : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"        : "sonum-carto",
          "dynamic_template"  : 'DynamicMap',
          "endpoint_type"     : "map",

          "contents_fields"  : [

            { "field" : "sd_id",
              "is_visible" : True,
              "position" : "block_id",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "is_visible" : True,
              "position" : "block_address",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "ville structure",
              "is_visible" : True,
              "position" : "block_city",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "intitulé structure",
              "is_visible" : True,
              "position" : "block_title",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "",
              "is_visible" : True,
              "position" : "block_image",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "description structure",
              "is_visible" : True,
              "position" : "block_abstract",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "source",
              "is_visible" : True,
              "position" : "block_src",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "",
              "is_visible" : True,
              "position" : "block_tags",
              "trim" : 50,
              "locale" : "fr"
            },
            
          ],

          "lat_long_fields" : {
            "latitude" : "lat",
            "longitude" : "lon"
          },

          "images_fields"        : {
            "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },

          "ui_options"        : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
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

          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },
        ## PAGE - list
        { "field"             : "sonum_carto_liste",
          "is_global_app_homepage" : False,
          "route_title"       : u"Rechercher",
          "route_description" : u"Page de recherche d'Apiviz",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-carto"
          },
          "is_dataset_homepage" : False,

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-carto/liste"],
          "template_url"      : "/static/spa.html",
          "help"             : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"        : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"        : "sonum-carto",
          "dynamic_template"  : 'DynamicList',
          "endpoint_type"     : "list",

          "contents_fields"  : [

            { "field" : "sd_id",
              "is_visible" : True,
              "position" : "block_id",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "is_visible" : True,
              "position" : "block_address",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "ville structure",
              "is_visible" : True,
              "position" : "block_city",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "intitulé structure",
              "is_visible" : True,
              "position" : "block_title",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "",
              "is_visible" : True,
              "position" : "block_image",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "description structure",
              "is_visible" : True,
              "position" : "block_abstract",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "source",
              "is_visible" : True,
              "position" : "block_src",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "",
              "is_visible" : True,
              "position" : "block_tags",
              "trim" : 50,
              "locale" : "fr"
            },

          ],

          "images_fields"        : {
            "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },
          "ui_options" : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
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
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },
        ## PAGE - detail
        { "field"             : "sonum_carto_detail",
          "is_global_app_homepage" : False,
          "route_title"        : u"Rechercher",
          "route_description"  : u"Page de recherche d'Apiviz",
          "route_activated"    : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-carto"
          },
          "is_dataset_homepage" : False,

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-carto/detail"],
          "template_url"      : "/static/spa.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"        : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"        : "sonum-carto",
          "dynamic_template"  : 'DynamicDetail',
          "endpoint_type"     : "detail",

          "contents_fields"  : [

            { "field" : "intitulé structure",
              "is_visible" : True,
              "position" : "block_title",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "is_visible" : True,
              "position" : "block_address",
              "trim" : 0,
              "locale" : "fr"
            },
          { "field" : "code postal structure",
              "is_visible" : True,
              "position" : "block_cp",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "description structure",
              "is_visible" : True,
              "position" : "block_abstract",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "source",
              "is_visible" : False,
              "position" : "block_src",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "services",
              "is_visible" : True,
              "position" : "block_tags",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "website structure",
              "is_visible" : True,
              "position" : "block_wesite",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "contact",
              "is_visible" : True,
              "position" : "block_contact",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "téléphone",
              "is_visible" : True,
              "position" : "block_tel",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "horaires structure",
              "is_visible" : True,
              "position" : "block_open_infos",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "services",
              "is_visible" : True,
              "position" : "block_services",
              "title_block" : [{ "locale" : "fr", "text" : "Services proposés", "is_visible" : False }],
            },
            { "field" : "infos pratiques",
              "is_visible" : True,
              "position" : "block_infos_pract",
              "title_block" : [{ "locale" : "fr", "text" : "Informations pratiques", "is_visible" : False }],
            },

          ],

          "images_fields"     : {
            "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
            "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
          },

          "ui_options"        : {
            "card_color"     : { "value" : None, "default" : "white", },
            "text_color"     : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : False, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
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
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },

      ### DATASETS XP SONUM
        ## PAGE - map
        { "field"             : "sonum_xp_carte",
          "is_global_app_homepage" : False,
          "route_title"        : u"Rechercher",
          "route_description"  : u"Page de recherche d'Apiviz",
          "route_activated"    : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },
          "is_dataset_homepage" : False,

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher une expérience" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-xp/carte"],
          "template_url"      : "/static/spa.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"        : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-xp",
          "dynamic_template"  : 'DynamicMap',
          "endpoint_type"     : "map",

          "contents_fields"  : [

            { "field" : "sd_id",
              "is_visible" : True,
              "position" : "block_id",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "titre initiative",
              "is_visible" : True,
              "position" : "block_title",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "is_visible" : True,
              "position" : "block_address",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "city",
              "is_visible" : True,
              "position" : "block_city",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "présentation initiative",
              "is_visible" : True,
              "position" : "block_abstract",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "type structure",
              "is_visible" : True,
              "position" : "block_tags",
              "trim" : 50,
              "locale" : "fr"
            },
          ],

          "images_fields"        : {
            "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },

          "ui_options"        : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
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
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },
        ## PAGE - list
        { "field"             : "sonum_xp_liste",
          "is_global_app_homepage" : False,
          "route_title"        : u"Rechercher",
          "route_description"  : u"Page de recherche d'Apiviz",
          "route_activated"    : True,
          "banner" : {
            "activated"  : True,
            "banner_uri" : "banner-sonum-xp"
          },
          "is_dataset_homepage" : True,

          "in_main_navbar"    : True,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : False,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher une expérience" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-xp/liste"],
          "template_url"      : "/static/spa.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"        : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-xp",
          "dynamic_template"  : 'DynamicList',
          "endpoint_type"     : "list",


          "contents_fields"  : [

            { "field" : "sd_id",
              "is_visible" : True,
              "position" : "block_id",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "titre initiative",
              "is_visible" : True,
              "position" : "block_title",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "is_visible" : True,
              "position" : "block_address",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "city",
              "is_visible" : True,
              "position" : "block_city",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "présentation initiative",
              "is_visible" : True,
              "position" : "block_abstract",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "type structure",
              "is_visible" : True,
              "position" : "block_tags",
              "trim" : 50,
              "locale" : "fr"
            },
          ],

          "images_fields"        : {
            "card_img_main" : { "field" : "illustration initiative", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },
          "ui_options" : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
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
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },
        ## PAGE - detail
        { "field"               : "sonum_xp_detail",
          "is_global_app_homepage" : False,
          "route_title"         : u"Rechercher",
          "route_description"   : u"Page de recherche d'Apiviz",
          "route_activated"     : True,
          "is_dataset_homepage" : False,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher une expérience" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-xp/detail"],
          "template_url"      : "/static/spa.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"        : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-xp",
          "dynamic_template"  : 'DynamicDetail',
          "endpoint_type"     : "detail",

          "contents_fields"  : [

            { "field" : "titre initiative",
              "is_visible" : True,
              "position" : "block_title",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "public visé",
              "is_visible" : True,
              "position" : "block_main_tags",
              "custom_title" : "Publics visés :",
              "is_tag_like" : True,
              "tags_separator" : "-",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "échelle action initiative",
              "is_visible" : True,
              "position" : "block_scale_tags",
              "custom_title" : "Echelle :",
              "is_tag_like" : True,
              "tags_separator" : "-",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "nom structure porteuse",
              "is_visible" : True,
              "position" : "block_scale_2",
              "custom_title" : "Structure :",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "is_visible" : True,
              "position" : "block_scale_address",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "city",
              "is_visible" : True,
              "position" : "block_city",
              "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "présentation structure",
              "is_visible" : True,
              "position" : "block_pre_abstract",
              "custom_title" : "Présentation de la structure",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "présentation initiative",
              "is_visible" : True,
              "position" : "block_abstract",
              "custom_title" : "Présentation de l'initiative",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "type structure",
              "is_visible" : True,
              "position" : "block_tags",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "date action initiative - début",
              "is_visible" : True,
              "position" : "block_period",
              "trim" : 50,
              "locale" : "fr"
            },
            { "field" : "contact - nom",
              "is_visible" : True,
              "position" : "block_contact_surname",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "contact - prénom",
              "is_visible" : True,
              "position" : "block_contact_name",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "contact - titre",
              "is_visible" : True,
              "position" : "block_contact_title",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "contact - email",
              "is_visible" : True,
              "position" : "block_contact_email",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "contact - téléphone",
              "is_visible" : True,
              "position" : "block_contact_tel",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "lien document présentation",
              "is_visible" : True,
              "position" : "block_file_1",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "website - initiative",
              "is_visible" : True,
              "position" : "block_wesite",
              "trim" : 0,
              "locale" : "fr"
            },
            { "field" : "retour d'expérience",
              "is_visible" : True,
              "position" : "block_right_bottom_1",
              "trim" : 0,
              "custom_title" : "Retour d'expérience",
              "locale" : "fr"
            },
            { "field" : "partenaires initiative",
              "is_visible" : True,
              "position" : "block_post_abstract_1",
              "trim" : 0,
              "custom_title" : "Partenaires de l'initiative",
              "locale" : "fr"
            },
            { "field" : "moyens humains initiative",
              "is_visible" : True,
              "position" : "block_post_abstract_2",
              "trim" : 0,
              "custom_title" : "Moyens",
              "locale" : "fr"
            },
            { "field" : "mesure d'impact",
              "is_visible" : True,
              "position" : "block_right_bottom_2",
              "trim" : 0,
              "custom_title" : "Mesure d'impact",
              "locale" : "fr"
            },
          ],

          "images_fields"     : {
            "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
            "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
          },
          "ui_options"        : {
            "card_color"     : { "value" : None, "default" : "white", },
            "text_color"     : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : False, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
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
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },

        ### PAGE HOME XP
        { "field"             : "sonum_xp_home",
          "is_global_app_homepage" : True,
          "route_title"       : u"Accueil XP",
          "route_description" : u"XP sonum default home page",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },
          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "link_in_logo"      : True,
          "urls"              : ["/sonum-xp/accueil"],
          "template_url"      : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/accueil-clean.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"       : version,
          "comment"           : u"Main project route in french",
          "is_dynamic"        : True,
          "dynamic_template"  : "DynamicStatic",
          "has_navbar"        : True,
          "has_footer"        : True,
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
          "is_default"        : True
        },
        ### PAGE STRATEGIE
        { "field"             : "sonum_xp_strategie",
          "is_global_app_homepage" : True,
          "route_title"       : u"Stratégie XP",
          "route_description" : u"apiviz default home page",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },
          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "link_in_logo"      : True,
          "urls"              : ["/sonum-xp/strategie"],
          "template_url"      : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/strategie-clean.html",
          # "template_url"      : "https://raw.githubusercontent.com/CBalsier/test-content/master/pages-html/le-collectif.html",
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
            "app_version"       : version,
          "comment"           : u"Main project route in french",
          "is_dynamic"        : True,
          "dynamic_template"  : "DynamicStatic",
          "has_navbar"        : True,
          "has_footer"        : True,
          "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/qui-sommes-nous"],
        "template_url"      : "https://github.com/co-demos/carto-sonum/blob/master/pages-html/qui-sommes-nous.html?raw=true",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"A custom page for your ApiViz app",
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicStatic',
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },

      ### PAGES : TOOLS
      { "field"              : "app_outils",
        "is_global_app_homepage" : False,
        "route_title"        : u"Outils",
        "route_description"  : u"Nos outils",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : True,
        "urls"              : ["/nos-outils"],
        "template_url"      : "/static/les-outils.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main tools route in french",
        "is_dynamic"        : False,
        "dynamic_template"  : None,
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },

      ### PAGE TOOLS - FR
      { "field"             : "app_tools",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/apiviz/outils"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/structure/master/pages-html/tools-fr.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },
      ### ...

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-LOGIN 
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_login",
        "is_global_app_homepage" : False,
        "route_title"       : u"Login",
        "route_description" : u"apiviz default login page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/login"],
        "template_url"      : "",
        "help"              : u"default login page for Apiviz",
        "languages"         : ["fr"],
          "app_version"       : version,
        "comment"           : u"Main login route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Login",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },

      { "field"             : "app_register",
        "is_global_app_homepage" : False,
        "route_title"       : u"Register",
        "route_description" : u"apiviz default register page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/register"],
        "template_url"      : "",
        "help"              : u"default register page for Apiviz",
        "languages"         : ["fr"],
          "app_version"       : version,
        "comment"           : u"Main register route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Register",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },

      { "field"             : "app_logout",
        "is_global_app_homepage" : False,
        "route_title"       : u"logout",
        "route_description" : u"apiviz default logout page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/logout"],
        "template_url"      : "",
        "help"              : u"default logout page for Apiviz",
        "languages"         : ["fr"],
          "app_version"       : version,
        "comment"           : u"Main logout route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Logout",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },

      { "field"             : "app_backoffice",
        "is_global_app_homepage" : False,
        "route_title"       : u"backoffice",
        "route_description" : u"apiviz default backoffice page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/backoffice"],
        "template_url"      : "",
        "help"              : u"default backoffice page for Apiviz",
        "languages"         : ["fr"],
          "app_version"       : version,
        "comment"           : u"Main backoffice route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "BackOffice",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"        : True
      },





  ### - - - - - - - - - - - - - - - - - - -  ### 
  ### CONFIG CIS 
  ### - - - - - - - - - - - - - - - - - - -  ###

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : HOME --> NEED AT LEAST ONE ROUTE AS 'is_global_app_homepage = True' / TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_home_fr",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "tabs" : {
          "activated" : False,
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_left",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : ["/"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/home.html",
        "has_ext_script"    : True,
        "ext_script_url"    : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/home.js",
        "has_carousel"      : True,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main home route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "dataset_uri"       : "cis",
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : DATASETS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE - map
      { "field"             : "cis_carte",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche d'Apiviz",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto" # TODO
        },
        "is_dataset_homepage" : True,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "only_in_navbar_for_this_dataset" : False,
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "urls"              : ["/recherche/carte"],
        "template_url"      : "/static/spa.html",
        "help"             : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"        : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"        : "cis",
        "dynamic_template"  : 'DynamicMap',
        "endpoint_type"     : "map",

        "contents_fields"  : [

          { "field" : "sd_id",
            "is_visible" : True,
            "position" : "block_id",
            "trim" : 50,
            "locale" : "fr"
          },
          # { "field" : "adresse structure", # SONUM
          { "field" : "adresse du projet", # CIS
            "is_visible" : True,
            "position" : "block_address",
            "trim" : 20,
            "locale" : "fr"
          },
          { "field" : "ville structure",
            "is_visible" : True,
            "position" : "block_city",
            "trim" : 20,
            "locale" : "fr"
          },
          # { "field" : "intitulé structure", # SONUM
          { "field" : "titre du projet", # CIS
            "is_visible" : True,
            "position" : "block_title",
            "trim" : 20,
            "locale" : "fr"
          },
          { "field" : "",
            "is_visible" : True,
            "position" : "block_image",
            "trim" : 20,
            "locale" : "fr"
          },
          { "field" : "résumé du projet",
            "is_visible" : True,
            "position" : "block_abstract",
            "trim" : 50,
            "locale" : "fr"
          },
          { "field" : "link_src", # spider/sourceur
            "is_visible" : True,
            "position" : "block_src",
            "trim" : 50,
            "locale" : "fr"
          },
          { "field" : "",
            "is_visible" : True,
            "position" : "block_tags",
            "trim" : 50,
            "locale" : "fr"
          },

        ],

        "lat_long_fields" : {
          "latitude" : "lat",
          "longitude" : "lon"
        },

        "images_fields"        : {
          "card_img_main" : { "field" : "image(s) du projet", "default" : "img_card",  "is_visible" : True  },
          "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        },

        "ui_options"        : {
          "card_color"    : { "value" : None, "default" : "white", },
          "text_color"    : { "value" : None, "default" : "black", },
          "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
          "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
          "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
        },

        "links_options"  : {

          "block_contents_links" : {
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
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"      : True
      },

      ### PAGE - list
      { "field"             : "cis_liste",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche d'Apiviz",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "only_in_navbar_for_this_dataset" : True,
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "urls"              : ["/recherche", "/recherche/liste"],
        "template_url"      : "/static/spa.html",
        "help"             : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"        : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"        : "cis",
        "dynamic_template"  : 'DynamicList',
        "endpoint_type"     : "list",

        "contents_fields"  : [

          { "field" : "sd_id",
            "is_visible" : True,
            "position" : "block_id",
            "trim" : 50,
            "locale" : "fr"
          },
          { "field" : "adresse du projet",
            "is_visible" : True,
            "position" : "block_address",
            "trim" : 20,
            "locale" : "fr"
          },
          { "field" : "ville structure",
            "is_visible" : True,
            "position" : "block_city",
            "trim" : 20,
            "locale" : "fr"
          },
          # { "field" : "intitulé structure", #SONUM
          { "field" : "titre du projet",#CIS
            "is_visible" : True,
            "position" : "block_title",
            "trim" : 20,
            "locale" : "fr"
          },
          { "field" : "",
            "is_visible" : True,
            "position" : "block_image",
            "trim" : 20,
            "locale" : "fr"
          },
          { "field" : "résumé du projet",
            "is_visible" : True,
            "position" : "block_abstract",
            "trim" : 50,
            "locale" : "fr"
          },
          { "field" : "link_src",
            "is_visible" : True,
            "position" : "block_src",
            "trim" : 50,
            "locale" : "fr"
          },
          { "field" : "",
            "is_visible" : True,
            "position" : "block_tags",
            "trim" : 50,
            "locale" : "fr"
          },

        ],

        "images_fields"        : {
          "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
          "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        },
        "ui_options" : {
          "card_color"    : { "value" : None, "default" : "white", },
          "text_color"    : { "value" : None, "default" : "black", },
          "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
          "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
          "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
        },

        "links_options"  : {

          "block_contents_links" : {
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
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE - detail
      { "field"             : "cis_detail",
        "is_global_app_homepage" : False,
        "route_title"        : u"Rechercher",
        "route_description"  : u"Page de recherche d'Apiviz",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "only_in_navbar_for_this_dataset" : True,
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "urls"              : ["/project", "/cis/detail"],
        "template_url"      : "/static/spa.html",
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"       : "cis",
        "dynamic_template"  : 'DynamicDetail',
        "endpoint_type"     : "detail",

        "contents_fields"  : [

          # { "field" : "intitulé structure", #SONUM
          { "field" : "titre du projet",#CIS
            "is_visible" : True,
            "position" : "block_title",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field" : "adresse du projet",
            "is_visible" : True,
            "position" : "block_address",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field" : "code postal structure",
            "is_visible" : True,
            "position" : "block_cp",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field" : "résumé du projet",
            "is_visible" : True,
            "position" : "block_abstract",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field" : "link_src",
            "is_visible" : False,
            "position" : "block_src",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field" : "services",
            "is_visible" : True,
            "position" : "block_tags",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field" : "link_data",
            "is_visible" : True,
            "position" : "block_wesite",
            "trim" : 0,
            "locale" : "fr"
          },
          { "field"       : "tags",
            "is_visible"  : True,
            "position"    : "block_right_bottom_1",
            "title_block" : [{ "locale" : "fr", "text" : "Tags", "is_visible" : True }],
          },

        ],

        "images_fields"     : {
          "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
          "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
        },

        "ui_options"        : {
          "card_color"     : { "value" : None, "default" : "white", },
          "text_color"     : { "value" : None, "default" : "black", },
          "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "fr", "text" : "voir le document" }] },
          "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir prochain document" }] },
          "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "fr", "text" : "voir le document précédent" }] },
        },

        "links_options"  : {

          "block_contents_links" : {
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
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-PAGES --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE - PROJECT
      { "field"             : "cis_project",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : ["/le-projet"],
        "dataset_uri"       : "project-cis",
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/le-projet.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : True,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main project route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_tabs"          : True,
        "tabs_uri"          : "project-cis-tabs",
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE : QUI SOMMES-NOUS CIS
      { "field"             : "app_who_fr",
        "is_global_app_homepage" : False,
        "route_title"        : u"Home",
        "route_description"  : u"Qui sommes-nous",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/qui-sommes-nous"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/le-collectif.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"A custom page for your ApiViz app",
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicStatic',
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE : QUI-SOMMES-NOUS/QUI-FAIT-QUOI
      { "field"             : "cis_partners",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "has_ext_script"    : True,
        "ext_script_url"    : "https:cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/who-are-we.js",
        "urls"              : ["/qui-sommes-nous/qui-fait-quoi"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/qui-fait-quoi.html",
        "has_ext_script"    : True,
        "ext_script_url"    : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/who-are-we.js",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE : JOIN US/NOUS REJOINDRE CIS
      { "field"             : "app_join_us",
        "is_global_app_homepage" : False,
        "route_title"        : u"Home",
        "route_description"  : u"Nous rejoindre",
        "route_activated"    : False, # this page is currently waiting for a redesign + new policy of "who can join?" + template not updated
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/nous-rejoindre"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/nous-rejoindre.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"A custom page for your ApiViz app",
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicStatic',
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGES : TOOLS (GENERIC)
      { "field"              : "app_outils",
        "is_global_app_homepage" : False,
        "route_title"        : u"Outils",
        "route_description"  : u"Nos outils",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : True,
        "urls"              : ["/nos-outils"],
        "template_url"      : "/static/les-outils.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"        : version,
        "comment"           : u"Main tools route in french",
        "is_dynamic"        : False,
        "dynamic_template"  : None,
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE TOOLS - FR - APIVIZ
      { "field"             : "app_tools",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/apiviz/outils"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/structure/master/pages-html/tools-fr.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE : PROJECT/TOOLS (CIS)
      { "field"             : "cis_tools",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-projet/outils"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/les-outils.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      ### PAGE : PROJECT/PARLENT-DE-NOUS (CIS)
      { "field"             : "cis_review",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-projet/parlent-de-nous"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/parlent-de-nous.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },


      ### PAGE : PROJECT/RECOMPENSES
      { "field"             : "cis_rewards",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-projet/recompenses"],
        "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/recompenses.html",
        "has_ext_script"    : False,
        "ext_script_url"    : "",
        "has_carousel"      : False,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-LOGIN 
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_login",
        "is_global_app_homepage" : False,
        "route_title"       : u"Login",
        "route_description" : u"apiviz default login page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/login"],
        "template_url"      : "",
        "help"              : u"default login page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main login route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Login",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      { "field"             : "app_register",
        "is_global_app_homepage" : False,
        "route_title"       : u"Register",
        "route_description" : u"apiviz default register page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/register"],
        "template_url"      : "",
        "help"              : u"default register page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main register route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Register",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      { "field"             : "app_logout",
        "is_global_app_homepage" : False,
        "route_title"       : u"logout",
        "route_description" : u"apiviz default logout page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/logout"],
        "template_url"      : "",
        "help"              : u"default logout page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main logout route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Logout",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },

      { "field"             : "app_backoffice",
        "is_global_app_homepage" : False,
        "route_title"       : u"backoffice",
        "route_description" : u"apiviz default backoffice page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/backoffice"],
        "template_url"      : "",
        "help"              : u"default backoffice page for Apiviz",
        "languages"         : ["fr"],
          "app_version"       : version,
        "comment"           : u"Main backoffice route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "BackOffice",
        "has_navbar"        : True,
        "has_footer"        : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"        : True
      },




]
