# -*- encoding: utf-8 -*-


from . 	import FORM_FIELDS_TO_IGNORE, ModelMixin, time, datetime

from .. import log_app, pformat

from ..settings.app_choices import * 



class Partner( ModelMixin ):

	def __init__(self, 	partnerName		= None,
						partnerWebsite	= None, 
						partnerAdress	= None, 
						partnerLogo		= None,

						partnerContacts	= [],
						partnerPhones	= [],
						partnerSocial	= [],
						
						partnerStatus	= "contributor",
						partnerSpiderId	= None,

						):
		"""
		datamodel for a partner in APIVIZ
		- take care of keeping same field names than in forms
		"""

		log_app.debug("creating User")