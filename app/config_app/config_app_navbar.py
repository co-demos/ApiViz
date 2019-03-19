# -*- encoding: utf-8 -*-

from . import version

default_app_navbar = [

  ### MAIN NAVBAR
    { "field"       : "app_navbar",
      "content"     : u"apiviz default navbar",
      "app_version" : version,
      "help"        : u"The nabvbar of your ApiViz instance",
      "ui_options"  : {
        "background_color" : { "value" : None, "default" : "white", },
      }, 
      "links_options" : {
        "extra_buttons" : [ ### for buttons not declared in routes/pages

            # { "is_visible" : True, 
            #   "position"   : "exterior_left",
            #   "link_to"    : "/xp-carto/liste",
            #   "is_external_link" : False,
            #   "link_type"  : "link", ### show btn border
            #   "icon_class" : "", 
            #   "link_text"  : [{"locale" : "fr", "text" : "partage d'expériences" }],
            #   "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }] 
            # },
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/sonum-carto/liste",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "lieux de médiation numérique" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }] 
            },
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/sonum-carto/projet",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "le projet" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }] 
            },
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "https://forum.societenumerique.gouv.fr",
              "is_external_link" : True,
              "link_type"  : "button", ### show btn border
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "Version bêta | Participez" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
        ]
      },
      "is_default"  : True
    },
]