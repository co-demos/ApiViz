

from . 	import FORM_FIELDS_TO_IGNORE, ModelMixin, time, datetime

from .. import log_app, pformat


class PreRegister(ModelMixin):

	def __init__(self,	follow_up_feedback = "- suivi du feedback - "
				):
		"""
		datamodel for a Preregister data in APIVIZ
		- take care of keeping same field names than in forms
		"""

		log_app.info("creating a PreRegister class object")		

		self.follow_up_feedback	= follow_up_feedback
