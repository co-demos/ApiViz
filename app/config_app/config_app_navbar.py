# -*- encoding: utf-8 -*-

from . import version

default_app_navbar = [

  ### MAIN NAVBAR
    { "field"       : "app_navbar",
      "content"     : u"apiviz default navbar",
      "app_version" : version,
      "help"        : u"The nabvbar of your ApiViz instance",
      "logo_to" : "/sonum-carto/liste",
      "ui_options"  : {
        "background_color" : { "value" : None, "default" : "white", },
      }, 
      "links_options" : {
        "extra_buttons" : [ ### for buttons not declared in routes/pages

          # NAVBAR ITEM - LINK WITH DROPDOWNS
          { "is_visible" : True, 
            "position"   : "exterior_right",
            "link_to"    : "/sonum-xp/liste",
            "is_external_link" : False,
            "link_type"  : "link", ### show as link
            "icon_class" : "", 
            "link_text"  : [{"locale" : "fr", "text" : "partage d'expériences" }],
            "tooltip"    : [{"locale" : "fr", "text" : "voir la liste" }],
            "has_dropdown" : True,
            "dropdowns"  : [
              { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/liste", "link_text" : [{"locale" : "fr", "text" : "Documentation des initiatives inspirantes"}] },
              { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/carte", "link_text" : [{"locale" : "fr", "text" : "Cartographie des initiatives"}] },
              { "is_divider" : True,  "is_external_link" : False },
              { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/stratégie", "link_text" : [{"locale" : "fr", "text" : "Elaborer une stratégie locale d'inclusion numérique"}] },
              { "is_divider" : True,  "is_external_link" : False },
              { "is_divider" : False, "is_external_link" : True, "link_to" : "https://societenumerique.gouv.fr/territoires/", "link_text" : [{"locale" : "fr", "text" : "Bénéficier des outils à ma disposition"}] },
              { "is_divider" : False, "is_external_link" : True, "link_to" : "https://societenumerique.gouv.fr/hubs/", "link_text" : [{"locale" : "fr", "text" : "Mobiliser les interlocuteurs"}] },
            ]
          },

          # NAVBAR ITEM - LINK WITH DROPDOWNS
          { "is_visible" : True, 
            "position"   : "exterior_right",
            "link_to"    : "/sonum-carto/liste",
            "is_external_link" : False,
            "link_type"  : "link", ### show as link
            "icon_class" : "", 
            "link_text"  : [{"locale" : "fr", "text" : "lieux de médiation numérique" }],
            "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }],
            "has_dropdown" : True,
            "dropdowns"  : [
              { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/carte", "link_text" : [{"locale" : "fr", "text" : "Cartographie des lieux de médiation numérique"}] },
              { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/liste", "link_text" : [{"locale" : "fr", "text" : "Liste des lieux de médiation numérique"}] },
              { "is_divider" : True,  "is_external_link" : False },
              { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/projet", "link_text" : [{"locale" : "fr", "text" : "Le projet de cartographie"}] },
            ]
          },

          # NAVBAR ITEM - SIMPLE LINK-LIKE
          # { "is_visible" : True, 
          #   "position"   : "exterior_right",
          #   "link_to"    : "/sonum-carto/projet",
          #   "is_external_link" : False,
          #   "link_type"  : "link", ### show as link
          #   "icon_class" : "", 
          #   "link_text"  : [{"locale" : "fr", "text" : "le projet" }],
          #   "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }],
          #   "has_dropdown" : False,
          #   "dropdowns"  : [],
          # },

          # NAVBAR ITEM - BUTTON-LIKE
          { "is_visible" : True, 
            "position"   : "exterior_right",
            "link_to"    : "https://forum.societenumerique.gouv.fr/category/10/cartographie-des-services-de-médiation-et-d-inclusion-numérique",
            "is_external_link" : True,
            "link_type"  : "button", ### show btn border
            "icon_class" : "", 
            "link_text"  : [{"locale" : "fr", "text" : "Version bêta | Participez" }],
            "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }],
            "has_dropdown" : False,
            "dropdowns"  : [],
          },
        ]
      },
      "is_default"  : True
    },
]