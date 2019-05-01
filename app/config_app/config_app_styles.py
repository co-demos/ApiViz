# -*- encoding: utf-8 -*-

from . import version

default_app_styles_config = [

  ### GLOBAL STYLES
    { "field"       : "app_colors",

      ### COLOR INPUTS AS HEXA
      "content"     : {

        ### DEFAULTS
        "default_background_app"    : "#fafafa",
        "default_background_navbar" : "#ffffff",

        ### SIMILI - BULMA
        "primary"     : "#513085",
        "secondary"   : "#a174ac",
        "info"        : "#40529d",
        "warning"     : "#f3bd80",
        "error"       : "#d24745",
        ### EXTRA COLORS
        "dark_blue"   : "#40529d",
        "light_pink"  : "#e89db1",
        "light_blue"  : "#a3b1d7",
        "deep_blue"   : "#21295e",
      },
      "app_version" : version,
      "help"        : u"Choose a set of colors (an hexa for example) for your ApiViz instance",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"  : True
    },

    { "field"       : "app_typo_colors",
      "content"     : {

        "default_dark"       : "#000000",
        "default_light_dark" : "#3D3A39",
        "default_invert"     : "#ffffff",

        ### SIMILI - BULMA
        "primary"     : "#513085",
        "secondary"   : "#a174ac",
        "info"        : "#40529d",
        "warning"     : "#f3bd80",
        "error"       : "#d24745",
        ### EXTRA COLORS
        "dark_blue"   : "#40529d",
        "light_pink"  : "#e89db1",
        "light_blue"  : "#a3b1d7",
        "deep_blue"   : "#21295e",
      },
      "app_version" : version,
      "help"        : u"Choose a set of colors for your typo for your ApiViz instance",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"  : True
    },

    { "field"       : "app_typo",
      "content"     : {
        "titles" : u"BonvenoCF-Light",
        "textes" : u"NEXA SANS",
      },
      "url"         : "",
      "app_version" : version,
      "help"        : u"Choose a typo for your ApiViz instance",
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"  : True
    },

  ### BANNERS SET
    { "field"       : "app_banners",
      "locale"      : "fr",
      "app_version" : version,
      "help"        : u"The dataset banners for your ApiViz instance (between navbar and filter)",
      "banners_set" : [
        {
          "banner_uri"       : "apiviz_default",
          "dataset_uri"      : None,
          "template_url"     : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/banner-sonum-dft.html",
          "is_dynamic"       : False,
          "dynamic_template" : 'DynamicBanner',
          "is_visible"          : False,
          "is_dismisible"       : True,
          "is_disapearing"      : False,
          "disapearing_timeout" : 5, ## in seconds
        },
        {
          "banner_uri"       : "banner-sonum-carto",
          "dataset_uri"      : "sonum-carto",
          "template_url"     : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/banner-sonum-dft.html",
          "is_dynamic"       : False,
          "dynamic_template" : 'DynamicBanner',
          "is_visible"          : False,
          "is_dismisible"       : True,
          "is_disapearing"      : False,
          "disapearing_timeout" : 5, ## in seconds
        },
        {
          "banner_uri"       : "banner-sonum-xp",
          "dataset_uri"      : "sonum-xp",
          "template_url"     : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/banner-sonum-xp.html",
          "is_dynamic"       : False,
          "dynamic_template" : 'DynamicBanner',
          "is_visible"          : False,
          "is_dismisible"       : True,
          "is_disapearing"      : False,
          "disapearing_timeout" : 5, ## in seconds
        },
      ],
      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"     : True
    },

  ### DEFAULT IMAGES FOR DATASETS SEARCH
    { "field"       : "app_search_default_images_sets",
      "app_version" : version,
      "help"        : u"The default images sets for the cards for each dataset",

      "images_sets" : [
        {
          "dataset_uri" : "sonum-carto",
          "images_set"  : [
            { "dft_text" : "img_1", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgA.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_2", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgB.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_3", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgC.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_4", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgD.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_5", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgE.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_6", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgF.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
          ]
        },
        {
          "dataset_uri" : "sonum-xp",
          "images_set"  : [
            { "dft_text" : "img_1", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgA.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_2", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgB.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_3", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgC.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_4", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgD.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_5", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgE.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
            { "dft_text" : "img_6", "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/imgF.png?raw=true", "credits" : "Laurie Chapotte", "licence" : "" },
          ]
        }
      ],

      "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
      "is_default"  : True
    },

]
