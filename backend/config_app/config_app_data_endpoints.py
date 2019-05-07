# -*- encoding: utf-8 -*-

from . import version

default_data_endpoints_config = [

  ### - - - - - - - - - - - - - - - ###
  ### USER MANAGEMENT
  ### - - - - - - - - - - - - - - - ###

    ### AUTH ROOT URLS
    { "field"          : "app_data_API_root_auth",
      "data_type"      : "user",
      "endpoint_type"  : "auth_root",
      "content"        : u"apiviz default API endpoint for user authentication (root urls)",
      "auth_activated" : True,
      "root_url"       : {
        ### needs a local instance of toktok if not changed
        "default"         : "http://localhost:4100/api",            # toktok instance on local machine
        "default_docker"  : "http://host.docker.internal:4100/api", # toktok instance on local machine + docker
        ### on server ...
        "server"          : "http://localhost:4100/api",            # toktok instance on server
        "server_docker"   : "http://host.docker.internal:4100/api", # toktok instance on server + docker
        "distant_preprod" : "https://preprod.toktok.co-demos.com/api",
        "distant_prod"    : "https://toktok.co-demos.com/api"
      },
      "args_options"   : [
      ],
      "app_version"    : version,
      "method"         : "GET",
      "help"           : u"define the endpoints for authentication",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"     : True
    },

    ### CONFIRM JWT
    { "field"         : "app_data_API_user_auth",
      "data_type"     : "user",
      "endpoint_type" : "confirm_jwt",
      "content"       : u"apiviz default API endpoint for user authentication (confirm acces)",
      "root_url"      : "/auth/tokens/confirm_access",
      "args_options"  : [
        { "app_arg" : "authToken", "arg" : "token", "optional" : False, "in" : ["url","header"], "default" : "", "type" : "str" },
      ],
      "resp_fields" : {
        "access_token"  : { "path" : "tokens/access_token" },
        "refresh_token" : { "path" : "tokens/refresh_token" },
        "msg"           : { "path" : "msg" },
        "user_role"     : { "path" : "data/auth/role" },
        "user_id"       : { "path" : "data/_id" },
        "user_name"     : { "path" : "data/infos/name" },
        "user_surname"  : { "path" : "data/infos/surname" },
        "user_pseudo"   : { "path" : "data/infos/pseudo"  },
        "user_email"    : { "path" : "data/infos/email" },
      },
      "roles" : { 
        ### defining roles in frontend
        "admin"     : { "resp_role" : "admin",     "help" : "can access all backoffice (lox level access)" },
        "staff"     : { "resp_role" : "staff",     "help" : "can access backoffice (high level access)" },
        "registred" : { "resp_role" : "registred", "help" : "registred user" },
        "guest"     : { "resp_role" : "guest",     "help" : "logged but not registred" },
        "anonymous" : { "resp_role" : "anonymous", "help" : "logged as anonymous" },
      },
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint for a JWT check",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### NEW ACCESS JWT
    { "field"         : "app_data_API_user_new_access_token",
      "data_type"     : "user",
      "endpoint_type" : "new_access_token",
      "content"       : u"apiviz default API endpoint for user authentication (new acces token) : needs a valid refresh token as token ",
      "root_url"      : "/auth/tokens/new_access_token",
      "args_options"  : [
        { "app_arg" : "authToken", "arg" : "token", "optional" : False, "in" : ["url","header"], "default" : "", "type" : "str" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint for a new access JWT ",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### REGISTER
    { "field"         : "app_data_API_user_register",
      "data_type"     : "user",
      "endpoint_type" : "register",
      "content"       : u"apiviz default API endpoint for registering a new user",
      "root_url"      : "/usr/register",
      "args_options"  : [
      ],
      "app_version"   : version,
      "method"        : "POST",
      "help"          : u"define the endpoint for registering a new user",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "needs_form"    : True,
      "is_default"    : True
    },

    ### LOGIN
    { "field"         : "app_data_API_user_login",
      "data_type"     : "user",
      "endpoint_type" : "login",
      "content"       : u"apiviz default API endpoint for login",
      "root_url"      : "/auth/login",
      "args_options"  : [
      ],
      "app_version"   : version,
      "method"        : "POST",
      "help"          : u"define the endpoint for login an user",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "needs_form"    : True,
      "is_default"    : True
    },

    ### USER LIST
    { "field"         : "app_data_API_user_list",
      "data_type"     : "user",
      "endpoint_type" : "user_modif",
      "content"       : u"apiviz default API endpoint for users list",
      "root_url"      : "/usr/infos/list",
      "args_options"  : [
        { "app_arg" : "authToken",    "arg" : "token",     "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "app_arg" : "pageUser",     "arg" : "page_n",   "optional" : True,   "in" : ["url"],           "default" : 1,   "type": "int" },
        { "app_arg" : "perPageUser",  "arg" : "per_page", "optional" : True,   "in" : ["url"],           "default" : 50, "type": "int" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : an user ",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### USER INFOS
    { "field"         : "app_data_API_user_infos",
      "data_type"     : "user",
      "endpoint_type" : "user_modif",
      "content"       : u"apiviz default API endpoint for user infos",
      "root_url"      : "/usr/infos/get_one",
      "args_options"  : [
        { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "app_arg" : "userID",    "arg" : "doc_id", "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : an user ",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### USER EDIT
    { "field"         : "app_data_API_user_edit",
      "data_type"     : "user",
      "endpoint_type" : "user_modif",
      "content"       : u"apiviz default API endpoint for editing an user",
      "root_url"      : "/auth/edit/",
      "args_options"  : [
        { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "app_arg" : "userID",    "arg" : "doc_id", "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
      ],
      "app_version"   : version,
      "method"        : "PUT",
      "help"          : u"define the endpoint to get data for : an user ",
      "needs_form"    : True,
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### USER DELETE
    { "field"         : "app_data_API_user_delete",
      "data_type"     : "user",
      "endpoint_type" : "user_modif",
      "content"       : u"apiviz default API endpoint for deleting an user",
      "root_url"      : "/auth/edit/",
      "args_options"  : [
        { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        { "app_arg" : "userID",    "arg" : "doc_id", "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
      ],
      "app_version"   : version,
      "method"        : "DELETE",
      "help"          : u"define the endpoint to get data for : an user ",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### USER FORGOT PWD
    { "field"         : "app_data_API_forgot_pwd",
      "data_type"     : "user",
      "endpoint_type" : "user_modif",
      "content"       : u"apiviz default API endpoint for changing password",
      "root_url"      : "/auth/password/password_forgotten",
      "args_options"  : [
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : an user ",
      "needs_form"    : True,
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
      "args_options"  : [
        {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
        {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" },
        {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
      ],

      "filter_options" : [
        { "name"		: u"coding services__",
          "id"      : "filter_1",
          "dataType" : "text",
          "fullname": u"Modalités d'accompagnement",		
          "choices"	: [
            {"name" : u"ACC", "fullname" : u"accompagnement"},
            {"name" : u"FOR", "fullname" : u"formation"},
            {"name" : u"ACL", "fullname" : u"accès libre"},
            # {"name" : u"non", "fullname" : u"aucun"},
            {"name" : u"NR",  "fullname" : u"non renseigné"},
          ]
        },
        { "name"		: u"coding jours__",
          "id"      : "filter_2",
          "dataType" : "text",
          "fullname": u"Jours d'ouverture",		
          "choices"	: [
            {"name" : u"lu", "fullname" : u"lundi"},
            {"name" : u"ma", "fullname" : u"mardi"},
            {"name" : u"me", "fullname" : u"mercredi"},
            {"name" : u"je", "fullname" : u"jeudi"},
            {"name" : u"ve", "fullname" : u"vendredi"},
            {"name" : u"sa", "fullname" : u"samedi"},
            {"name" : u"di", "fullname" : u"dimanche"},
          ]
        },
        {	"name"		: u"source__",
          "id"      : "filter_3",
          "dataType" : "text",
          "fullname" 	: u"Source",		
          "choices"	: [
            {"name" : u"APTIC",            "fullname" : u"APTIC"},
            {"name" : u"Gironde",          "fullname" : u"Gironde"},
            {"name" : u"Hauts de France",  "fullname" : u"Hauts de France"},
            {"name" : u"Loire-Atlantique", "fullname" : u"Loire-Atlantique"},
            {"name" : u"MSAP",             "fullname" : u"MSAP"},
            {"name" : u"NetPublic",        "fullname" : u"NetPublic"},
          ], 
        },

      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : filters in search navbar",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
      "args_options"  : [
        {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
        {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 100, "type": "int" },
        {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
        {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
        {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : 0 , "type": "int" },

      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a view list",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
      "args_options"  : [
        {  "app_arg" : "dataToken",  "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a detailled data",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
      "args_options"   : [
        {  "app_arg" : "dataToken",        "arg" : "token",                "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "app_arg" : "onlyCountsSimple", "arg" : "only_counts_simple",   "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a stat about the dataset",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
        "minZoom"          : 3,
        "useMarkerCluster" : True,
        "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
        "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]}
      },
      "content"       : u"apiviz default API endpoint for map results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
      # "root_url"      : "http://localhost:4000/api/dso/infos/get_one/5c89636d328ed70609be03ab",
      "args_options"  : [
        {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },

        {  "app_arg" : "forMap",     "arg" : "map_list",         "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        # {  "app_arg" : "asLatLng", "arg" : "as_latlng",        "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "app_arg" : "onlyGeocoded", "arg" : "only_geocoded",  "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },

        # {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],          "default" : 1,    "type": "int" },
        # {  "app_arg" : "perPage",    "arg" : "per_page", "optional" : True, "in" : ["url"],          "default" : 100,  "type": "int" },
        {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
        {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
        {  "app_arg" : "itemId",     "arg" : "item_id",          "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },

      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : map results",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
        {"locale" : "fr", "text" : "Tapez le nom d'une initiative" }
      ],
      "items_found"   : [
        {"locale" : "fr", "text" : "initiatives trouvées" }
      ],
      "reset"   : [
        {"locale" : "fr", "text" : "Effacer" }
      ],

      "content"       : u"apiviz default API endpoint for navbar filters",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"  : [
        {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
        {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" },
        {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
      ],

      "filter_options" : [

        { "name"		: u"type structure__",
          "id"      : "filter_1",
          "dataType" : "text",
          "fullname": u"Type de structure",		
          "choices"	: [
            {"name" : u"structure publique (CCAS, CIAS, bibliothèque, etc...)", "fullname" : u"structure publique"},
            {"name" : u"collectivité territoriale/EPCI",                        "fullname" : u"collectivité territoriale/EPCI"},

          ]
        },
        { "name"		: u"thématique__",
          "id"      : "filter_2",
          "dataType" : "text",
          "fullname": u"Thématique",		
          "choices"	: [
            {"name" : u"INCNUM", "fullname" : u"inclusion numérique"},
            {"name" : u"DEMPAR", "fullname" : u"démocratie participative"},
            {"name" : u"FORNUM", "fullname" : u"formation aux métiers du numérique"},
            {"name" : u"POLOUV", "fullname" : u"politique d'ouverture des données"},
            {"name" : u"MEDNUM", "fullname" : u"médiation numérique"},
            {"name" : u"FORAGP", "fullname" : u"formation d'agents publics"},
            {"name" : u"TERINT", "fullname" : u"territoire intelligent"},
            {"name" : u"CULNUM", "fullname" : u"culture numérique"},
            {"name" : u"TIELIE", "fullname" : u"tiers lieux"},
            {"name" : u"COMMUN", "fullname" : u"communs numériques"},
            {"name" : u"DATLIT", "fullname" : u"data literacy"},
            {"name" : u"AUTRES", "fullname" : u"autre"},
          ]
        },


      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : filters in search navbar",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
        {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
        {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
        {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 100, "type": "int" },
        {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
        {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
        {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : 0 , "type": "int" },
      ],
      "app_version"   : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a view list",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
        {  "app_arg" : "dataToken",  "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a detailled data",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },

    ### DATA STATS
    { "field"         : "sonum_xp_data_API_stats",
      "is_visible"    : False,
      "is_disabled"   : False,
      "data_type"     : "data",
      "endpoint_type" : "stat",
      "dataset_uri"    : "sonum-xp",
      "content"       : u"apiviz default API endpoint for stats results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"   : [
        {  "app_arg" : "dataToken",        "arg" : "token",              "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
        {  "app_arg" : "onlyCountsSimple", "arg" : "only_counts_simple", "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : a stat about the dataset",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
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
        "minZoom"          : 5,
        "useMarkerCluster" : True,
        "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
        "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]}
      },
      "content"       : u"apiviz default API endpoint for map results",
      "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
      "args_options"  : [
        {  "app_arg" : "dataToken",     "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },
        {  "app_arg" : "forMap",        "arg" : "map_list",         "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "app_arg" : "asLatLng",      "arg" : "as_latlng",        "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "app_arg" : "onlyGeocoded",  "arg" : "only_geocoded",    "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
        {  "app_arg" : "page",          "arg" : "page_n",           "optional" : True, "in" : ["url"],          "default" : 1,   "type": "int" },
        {  "app_arg" : "perPage",       "arg" : "per_page",         "optional" : True, "in" : ["url"],          "default" : 100,   "type": "int" },
        {  "app_arg" : "itemId",        "arg" : "item_id",          "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },

        {  "app_arg" : "query",         "arg" : "search_for",       "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
        {  "app_arg" : "filters",       "arg" : "search_filters",   "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
      ],
      "app_version"    : version,
      "method"        : "GET",
      "help"          : u"define the endpoint to get data for : map results",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"    : True
    },


]
