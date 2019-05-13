# -*- encoding: utf-8 -*-

from . import version

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG SONUM
      { "field"       : "app_navbar",
        "content"     : u"apiviz default navbar",
        "app_version" : version,
        "help"        : u"The nabvbar of your ApiViz instance",
        "logo_to"     : "/sonum-carto/carte",
        "ui_options"  : {
          "background_color" : { "value" : None, "default" : "white", },
        }, 
        "links_options" : {

          "extra_buttons" : [ ### for buttons not declared in routes/pages

            # NAVBAR ITEM - LINK WITH DROPDOWNS
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/sonum-xp/accueil",
              "is_external_link" : False,
              "link_type"  : "link", ### show as link
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "territoires" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir la liste" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/accueil",   "link_text" : [{"locale" : "fr", "text" : "Accueil"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/strategie", "link_text" : [{"locale" : "fr", "text" : "Elaborer une stratégie locale d'inclusion numérique"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/liste", "link_text" : [{"locale" : "fr", "text" : "Documentation des initiatives inspirantes"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/carte", "link_text" : [{"locale" : "fr", "text" : "Cartographie des initiatives"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://societenumerique.gouv.fr/territoires/", "link_text" : [{"locale" : "fr", "text" : "Bénéficier des outils à ma disposition"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://societenumerique.gouv.fr/hubs/", "link_text" : [{"locale" : "fr", "text" : "Mobiliser les interlocuteurs"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://framaforms.org/documentation-dinitiatives-et-politiques-publiques-numeriques-innovantes-1540547339", "link_text" : [{"locale" : "fr", "text" : "Formulaire de documentation"}] },
              ]
            },

            # NAVBAR ITEM - LINK WITH DROPDOWNS
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/sonum-carto/carte",
              "is_external_link" : False,
              "link_type"  : "link", ### show as link
              "icon_class" : "", 
              "link_text"  : [{"locale" : "fr", "text" : "lieux de médiation numérique" }],
              "tooltip"    : [{"locale" : "fr", "text" : "voir la carte" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/projet", "link_text" : [{"locale" : "fr", "text" : "Le projet de cartographie"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/carte", "link_text" : [{"locale" : "fr", "text" : "Cartographie des lieux de médiation numérique"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/liste", "link_text" : [{"locale" : "fr", "text" : "Liste des lieux de médiation numérique"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://forum.societenumerique.gouv.fr/category/10/cartographie-des-services-de-m%C3%A9diation-et-d-inclusion-num%C3%A9rique", "link_text" : [{"locale" : "fr", "text" : "Participez à la cartographie"}] },
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
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG APCIS
      { "field"       : "app_navbar",
        "content"     : u"CIS navbar",
        "app_version" : version,
        "help"        : u"The nabvbar of your ApiViz instance",
        "logo_to"     : "/",
        "ui_options"  : {
          "background_color" : { "value" : None, "default" : "white", },
        },
        "links_options" : {
          "extra_buttons" : [ ### for buttons not declared in routes/pages

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/recherche",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "fr", "text" : "Moteur de recherche" }],
              "tooltip"    : [{"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/recherche",   "link_text" :
                    [{"locale" : "fr", "text" : "Liste"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/recherche/carte",   "link_text" :
                    [{"locale" : "fr", "text" : "Carte"}] },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/le-projet",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "fr", "text" : "Projet" }],
              "tooltip"    : [{"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet",   "link_text" :
                    [{"locale" : "fr", "text" : "À propos"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/outils",   "link_text" :
                    [{"locale" : "fr", "text" : "Les outils techniques"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/parlent-de-nous",   "link_text" :
                    [{"locale" : "fr", "text" : "Ils parlent de nous"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/recompenses",   "link_text" :
                    [{"locale" : "fr", "text" : "Récompenses"}] },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/qui-sommes-nous",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "fr", "text" : "Qui sommes-nous ?" }],
              "tooltip"    : [{"locale" : "fr", "text" : "Plus d’informations sur l’initiative" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/qui-sommes-nous",   "link_text" :
                    [{"locale" : "fr", "text" : "Le collectif"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/qui-sommes-nous/qui-fait-quoi",   "link_text" :
                    [{"locale" : "fr", "text" : "Qui fait quoi ?"}] },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "fr", "text" : "FR" }],
              "tooltip"    : [{"locale" : "fr", "text" : "En français" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/accueil",   "link_text" : [{"locale" : "fr", "text" : "Accueil"}] },
                { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "fr", "text" : "EN" }],
              "tooltip"    : [{"locale" : "fr", "text" : "En anglais" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/accueil",   "link_text" : [{"locale" : "fr", "text" : "Accueil"}] },
                { "is_divider" : True,  "is_external_link" : False },
              ]
            },
          ]
        },
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

]