# -*- encoding: utf-8 -*-

from . import version

default_data_endpoints_config = [

  ### - - - - - - - - - - - - - - - ###
  ### USER MANAGEMENT
  ### - - - - - - - - - - - - - - - ###

    ### CONFIRM JWT
    { "field"         : "app_data_API_user_auth",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for user authentication (confirm acces)",
      "root_url"      : "http://localhost:4100/api/auth/tokens/confirm_access",
      "args_options"  : [
        { "arg" : "token",     "optional" : False, "in" : ["url","header"], "default" : "", "type" : "str" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint for a JWT check",
      "is_default"    : True
    },

    ### NEW ACCESS JWT
    { "field"         : "app_data_API_user_new_access_token",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for user authentication (new acces token) : needs a valid refresh token as token ",
      "root_url"      : "http://localhost:4100/api/auth/tokens/new_access_token",
      "args_options"  : [
        { "arg" : "token",     "optional" : False, "in" : ["url","header"], "default" : "", "type" : "str" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint for a new access JWT ",
      "is_default"    : True
    },

    ### REGISTER
    { "field"         : "app_data_API_user_register",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for registering a new user",
      "root_url"      : "http://localhost:4100/api/usr/register/",
      "args_options"  : [
      ],
      "app_version"   : version,
      "method"        : "POST",
      "help"          : u"define the endpoint for registering a new user",
      "needs_form"    : True,
      "is_default"    : True
    },

    ### LOGIN
    { "field"         : "app_data_API_user_login",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for login",
      "root_url"      : "http://localhost:4100/api/auth/login/",
      "args_options"  : [
      ],
      "app_version"   : version,
      "method"        : "POST",
      "help"          : u"define the endpoint for login an user",
      "needs_form"    : True,
      "is_default"    : True
    },

    ### USER LIST
    { "field"         : "app_data_API_user_list",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for users list",
      "root_url"      : "http://localhost:4100/api/usr/infos/list",
      "args_options"  : [
        { "arg" : "token",     "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        {  "arg" : "page_n",   "optional" : True,   "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "arg" : "per_page", "optional" : True,   "in" : ["url"],           "default" : 50, "type": "int" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : an user ",
      "is_default"    : True
    },

    ### USER INFOS
    { "field"         : "app_data_API_user_infos",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for user infos",
      "root_url"      : "http://localhost:4100/api/usr/infos/get_one/",
      "args_options"  : [
        { "arg" : "token",     "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "arg" : "doc_id",   "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : an user ",
      "is_default"    : True
    },

    ### USER EDIT
    { "field"         : "app_data_API_user_edit",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for editing an user",
      "root_url"      : "http://localhost:4100/api/auth/edit/",
      "args_options"  : [
        { "arg" : "token",     "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "arg" : "doc_id",   "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
      ],
      "app_version"   : version,
      "method"        : "PUT",
      "help"          : u"define the endpoint to get data for : an user ",
      "needs_form"    : True,
      "is_default"    : True
    },

    ### USER DELETE
    { "field"         : "app_data_API_user_delete",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for deleting an user",
      "root_url"      : "http://localhost:4100/api/auth/edit/",
      "args_options"  : [
        { "arg" : "token",     "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "arg" : "doc_id",   "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
      ],
      "app_version"   : version,
      "method"        : "DELETE",
      "help"          : u"define the endpoint to get data for : an user ",
      "is_default"    : True
    },

    ### USER FORGOT PWD
    { "field"         : "app_data_API_forgot_pwd",
      "data_type"     : "user",
      "content"       : u"apiviz default API endpoint for changing password",
      "root_url"      : "http://localhost:4100/api/auth/password/password_forgotten",
      "args_options"  : [
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : an user ",
      "needs_form"    : True,
      "is_default"    : True
    },

  ### - - - - - - - - - - - - - - - ###
  ### DATA ENDPOINTS
  ### - - - - - - - - - - - - - - - ###

  ####### SONUM / CARTO #######

    ### DATA FILTERS
    { "field"         : "sonum_carto_data_API_filters",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "filters",
      "dataset_uri"   : "sonum-carto",

      "placeholder"   : [
        {"locale" : "fr", "text" : "Tapez le nom d'un lieu" }
      ],
      "items_found"   : [
        {"locale" : "fr", "text" : "lieux trouvés" }
      ],
      "reset"   : [
        {"locale" : "fr", "text" : "Effacer" }
      ],

      "content"       : u"apiviz default API endpoint for navbar filters",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc68328ed724cebd7fbf",
      "args_options"  : [
        {  "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
        {  "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" },
        {  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : filters in search navbar",
      "is_default"    : True
    },

    ### DATA LIST
    { "field"         : "sonum_carto_data_API_list",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "list",
      "dataset_uri"   : "sonum-carto",
      "content"       : u"apiviz default API endpoint for list results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc68328ed724cebd7fbf",
      "args_options"  : [
        {  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
        {  "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "arg" : "results_per_page", "optional" : True, "in" : ["url"],           "default" : 100, "type": "int" },
        {  "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
        {  "arg" : "search_in",        "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a view list",
      "is_default"    : True
    },

    ### DATA DETAIL
    { "field"         : "sonum_carto_data_API_detail",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "detail",
      "dataset_uri"   : "sonum-carto",
      "content"       : u"apiviz default API endpoint for detailled results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc68328ed724cebd7fbf",
      "args_options"  : [
        {  "arg" : "token",     "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "arg" : "item_id",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a detailled data",
      "is_default"    : True
    },

    ### DATA STATS
    { "field"         : "sonum_carto_data_API_stats",
      "is_visible"    : False,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "stat",
      "dataset_uri"    : "sonum-carto",
      "content"       : u"apiviz default API endpoint for stats results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc68328ed724cebd7fbf",
      "args_options"   : [
        {  "arg" : "token",                 "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "arg" : "only_counts_simple",   "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
        {  "arg" : "only_tags_stats",       "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
        {  "arg" : "only_spiders_stats",   "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a stat about the dataset",
      "is_default"    : True
    },

    ### DATA MAP
    { "field"         : "sonum_carto_data_API_map",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "map",
      "dataset_uri"   : "sonum-carto",
      "map_options"   : {
        "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
        "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        "subdomains"       : 'abcd',
        "center"           : [46.2276, 2.2137],
        "currentCenter"    : [46.2276, 2.2137],
        "zoom"             : 6,
        "maxZoom"          : 18,
        "useMarkerCluster" : True,
        "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
        "pinIconSize"      : { "highlighted" : [46, 46] , "normal" : [29, 29]}
      },
      "content"       : u"apiviz default API endpoint for map results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc68328ed724cebd7fbf",
      # "root_url"      : "http://localhost:4000/api/dso/infos/get_one/5c7ebc68328ed724cebd7fbf",
      "args_options"  : [
        {  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },
        {  "arg" : "map_list",         "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "arg" : "as_latlng",        "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "arg" : "only_geocoded",    "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "arg" : "results_per_page", "optional" : True, "in" : ["url"],           "default" : 100,   "type": "int" },
        {  "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "",   "type": "str" },
        {  "arg" : "search_in",        "optional" : True, "in" : ["url"],           "default" : "",   "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : map results",
      "is_default"    : True
    },



  ####### SONUM / XP #######

    ### DATA FILTERS
    { "field"         : "sonum_xp_data_API_filters",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "filters",
      "dataset_uri"   : "sonum-xp",

      "placeholder"   : [
        {"locale" : "fr", "text" : "Tapez le nom d'une expérience" }
      ],
      "items_found"   : [
        {"locale" : "fr", "text" : "expériences trouvées" }
      ],
      "reset"   : [
        {"locale" : "fr", "text" : "Effacer" }
      ],

      "content"       : u"apiviz default API endpoint for navbar filters",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"  : [
        {  "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
        {  "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" },
        {  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : filters in search navbar",
      "is_default"    : True
    },

    ### DATA LIST
    { "field"         : "sonum_xp_data_API_list",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "list",
      "dataset_uri"   : "sonum-xp",
      "content"       : u"apiviz default API endpoint for list results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"  : [
        {  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
        {  "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "arg" : "results_per_page", "optional" : True, "in" : ["url"],           "default" : 100, "type": "int" },
        {  "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
        {  "arg" : "search_in",        "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a view list",
      "is_default"    : True
    },

    ### DATA DETAIL
    { "field"         : "sonum_xp_data_API_detail",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "detail",
      "dataset_uri"   : "sonum-xp",
      "content"       : u"apiviz default API endpoint for detailled results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"  : [
        {  "arg" : "token",     "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "arg" : "item_id",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a detailled data",
      "is_default"    : True
    },

    ### DATA STATS
    { "field"         : "sonum_xp_data_API_stats",
      "is_visible"    : False,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "stat",
      "dataset_uri"    : "sonum-carto",
      "content"       : u"apiviz default API endpoint for stats results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"   : [
        {  "arg" : "token",                 "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "arg" : "only_counts_simple",   "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
        {  "arg" : "only_tags_stats",       "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
        {  "arg" : "only_spiders_stats",   "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a stat about the dataset",
      "is_default"    : True
    },

    ### DATA MAP
    { "field"         : "sonum_xp_data_API_map",
      "is_visible"    : True,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "map",
      "dataset_uri"   : "sonum-xp",
      "map_options"   : {
        "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
        "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        "subdomains"       : 'abcd',
        "center"           : [46.2276, 2.2137],
        "currentCenter"    : [46.2276, 2.2137],
        "zoom"             : 6,
        "maxZoom"          : 18,
        "useMarkerCluster" : True,
        "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
        "pinIconSize"      : { "highlighted" : [46, 46] , "normal" : [29, 29]}
      },
      "content"       : u"apiviz default API endpoint for map results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"  : [
        {  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },
        {  "arg" : "map_list",         "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "arg" : "as_latlng",        "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "arg" : "only_geocoded",    "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "arg" : "results_per_page", "optional" : True, "in" : ["url"],           "default" : 100,   "type": "int" },
        {  "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "",   "type": "str" },
        {  "arg" : "search_in",        "optional" : True, "in" : ["url"],           "default" : "",   "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : map results",
      "is_default"    : True
    },


]
