# -*- encoding: utf-8 -*-

from .. import log_app, pformat

print
log_app.info(">>> reading settings.app_settings.py ")


### vars for name application / metas
app_metas = {
	
	# "title"				: u"carrefour des innovations sociales", ### dataioio.com | coralcommons.com/io | tadata.io | coraless.io | solidata.io
	# "subtitle"		: u"le moteur de recherche des innovations sociales",
	# "description"	: u"Le Carrefour des innovations sociales regroupe les innovations sociales recensées et actualisées par des partenaires experts. ",
	"version"			: u"v.0.1 alpha",
	"authors"			: u"Julien Paris - http://jpylab.com / Guillaume Lancrenon - https://guillim.github.io",
	"licence"			: u"MIT",

	"refresh_page"	: 1800, # refresh/reload page every n seconds : f.e. 1800 s == every 30 min
	
	# "keywords"		: u"""
	# 	dataviz,data visualisation,data visualization,SIG,
	# 	commons,digital commons,API,
	# 	opensource,open source,open data,opendata,MIT licence,github,
	# 	JS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,
	# 	Etalab,co-demos, codemos,
	# 	""",
	
	"crisp_id"		: {
		u"cis" : "TO DO", 
		},
	
	"mixpanel_id" 	: {   
		u'production'	: "TO DO ",    ### for production metrics  / mixpanel account : carrefour
		u'default'		: "TO DO"      ### for development metrics / mixpanel account : jparis.py
	},
}

