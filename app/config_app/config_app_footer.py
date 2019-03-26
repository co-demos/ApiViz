# -*- encoding: utf-8 -*-

from . import version

default_app_footer = [

  ### FOOTER
    { "field"       : "app_footer",
      "app_version" : version,
      "help"        : u"The default footer for your ApiViz instance",

      "template_url"      : None,
      "is_dynamic"        : True,
      "dynamic_template"  : 'DynamicFooter',
      "has_credits_footer": True,
      "credits_footer_url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/footer-mednum.html",
      "active_columns"    : ['block_left', 'block_center_left', 'block_center_right','block_right'],

      "contents_fields" : {

        "block_left"  : [
          { 
            "is_visible"  : False, 
            "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
            "position"    : "block_top_left", 
          }
        ],
        "block_center_left" : [
          { 
            "is_visible"  : False, 
            "title_block" : [{ "locale" : "fr", "text" : "Sites publics", "is_visible" : False}],
            "position"    : "block_top_middle", 
          }
        ],
        "block_center_right" : [
          { 
            "is_visible"  : False, 
            "title_block" : [{ "locale" : "fr", "text" : "Sites publics", "is_visible" : False}],
            "position"    : "block_top_middle", 
          }
        ],
        "block_right" : [
          { 
            "is_visible"  : False, 
            "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
            "position"    : "block_top_right", 
          }
        ],

      },

      "ui_options" : {

          "card_color" : { "value" : None, "default" : "grey", },
          "text_color" : { "value" : None, "default" : "white", },

          "footer_logos" : [
            { "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/logos/bloc-web-le-maire-darmanin.png?raw=true", 
              "has_link"  : False,
              "link_to"   : "/" , 
              "position"  : "block_top_left" 
            }
          ],

      },

      "links_options" : {

        "block_left" : {
          "is_visible"  : False,
          "position"    : "block_top_left",
          "title_block" : [{ "locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : []
        },

        "block_center_left" : {
          "is_visible"  : True,
          "position"    : "block_top_center_left",
          "title_block" : [{ "locale" : "fr", "text" : "L'Agence du numérique", "is_visible" : False}],
          "links"       : [

            { "is_visible" : True, 
              "link_to"    : "https://www.agencedunumerique.gouv.fr/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "L'Agence du numérique" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://www.francethd.fr/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "Mission France Très Haut Débit" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://www.lafrenchtech.com/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "Mission French Tech" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
          ]
        },

        "block_center_right" : {
          "is_visible"  : True,
          "position"    : "block_top_center_left",
          "title_block" : [{ "locale" : "fr", "text" : "Société numérique", "is_visible" : False}],
          "links"       : [

            { "is_visible" : True, 
              "link_to"    : "https://societenumerique.gouv.fr/en-savoir-plus/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "En savoir plus" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://societenumerique.gouv.fr/presse/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "Presse" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "kit d'intervention rapide" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "plateforme des territoires" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://societenumerique.gouv.fr/mentions-legales/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "mentions légales" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://societenumerique.gouv.fr/accessibilite/",
              "is_external_link" : True,
              "link_type"  : "text",
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "accessibilité" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            # { "is_visible" : True, 
            #   "link_to"    : "/login",
            #   "is_external_link" : False,
            #   "link_type"  : "text",
            #   "icon_class" : "", 
            #   "link_text"  : [{"locale" : "fr", "text" : "admin" }],
            #   "tooltip"    : [{"locale" : "fr", "text" : "se connecter au back-office" }] 
            # },
            # { "is_visible" : False, 
            #   "link_to"    : "/register",
            #   "is_external_link" : False,
            #   "link_type"  : "text",
            #   "icon_class" : "", 
            #   "link_text"  : [{"locale" : "fr", "text" : "register" }],
            #   "tooltip"    : [{"locale" : "fr", "text" : "se créer un compte" }] 
            # },
            { "is_visible" : True, 
              "link_to"    : "https://github.com/co-demos/ApiViz",
              "is_external_link" : True,
              "link_type"  : "text",
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "code source" }],
              "tooltip"    : [{"locale" : "fr", "text" : "accéder au code source" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "/apiviz/outils",
              "is_external_link" : False,
              "link_type"  : "text",
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "outils open source" }],
              "tooltip"    : [{"locale" : "fr", "text" : "accéder au code source" }] 
            },
          ]
        },

        "block_right" : {
          "is_visible"  : True,
          "position"    : "block_top_right",
          "title_block" : [{ "locale" : "fr", "text" : "Les sites publics", "is_visible" : False}],
          "links"       : [

            { "is_visible" : True, 
              "link_to"    : "https://www.gouvernement.fr/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "gouvernement.fr" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://www.service-public.fr/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "service-public.fr" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://www.legifrance.fr/",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "legifrance.fr" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://www.elysee.fr",
              "is_external_link" : True,
              "link_type"  : "text", 
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "elysee.fr" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir le site" }] 
            },
            { "is_visible" : True, 
              "link_to"    : "https://www.data.gouv.fr/",
              "is_external_link" : True,
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

]