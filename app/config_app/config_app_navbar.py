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

            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/",
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