# -*- encoding: utf-8 -*-

from .. import log_app, pformat

print
log_app.info(">>> reading settings.app_settings.py ")

### vars for application in metas
app_metas = {
	
	"version"			: u"v.0.1 alpha",
	"authors"			: u"Julien Paris - http://jpylab.com / Guillaume Lancrenon - https://guillim.github.io",
	"licence"			: u"MIT",
	"refresh_page"	: 1800, # refresh/reload page every n seconds : f.e. 1800 s == every 30 min

}

