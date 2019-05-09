# -*- encoding: utf-8 -*-

from . import version

default_app_tabs = [

  ### MAIN TABS

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG SONUM
      { "field"       : "app_tabs_default",
        "tab_uri"     : "tabs-sonum-default",
        "content"     : u"apiviz default navbar",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "ui_options"  : {
          "background_color" : { "value" : None, "default" : "white", },
        }, 
        "tabs_options" : [ 
          { "is_visible" : True, 
            "tab_code"   : "tab-1",
            "is_activated" : True,
            "link_to"    : "/",
            "has_icon"   : False,
            "icon_class" : "", 
            "link_text"  : [{"locale" : "fr", "text" : "le projet" }],
            "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }],
          },
        ],
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG APCIS
      { "field"       : "app_tabs_default",
        "tab_uri"     : "tabs-cis-default",
        "content"     : u"apiviz default navbar",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "ui_options"  : {
          "background_color" : { "value" : None, "default" : "white", },
        }, 
        "tabs_options" : [ 
          { "is_visible" : True, 
            "tab_code"   : "tab-1",
            "is_activated" : True,
            "link_to"    : "/",
            "has_icon"   : False,
            "icon_class" : "", 
            "link_text"  : [{"locale" : "fr", "text" : "le projet" }],
            "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }],
          },
        ],
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

]