# -*- encoding: utf-8 -*-

"""
main config file --> to keep secret 
stores main secret keys and app passwords
"""

""" APP SECRET KEY """
SECRET_KEY					= "app_very_secret_key"
WTF_CSRF_SECRET_KEY = "a_super_wtf_secret_key"
WTF_CSRF_ADMIN_KEY	= "a_mega_super_key_for_admin_views" 

""" SHARED JWT SECRET KEY : this key must be shared with openscraper and solidata """
JWT_SECRET_KEY		= "a_key_shared_solidata"

""" HOST / PORT / DOMAIN / SERVER """
SERVER_NAME_TEST		= "True" 


# """ PORT SOCKETIO """
# PORT_EVENTLET		= "4000"


""" MONGODB """
MONGO_URI					= 'mongodb://localhost:27017/apiviz'

""" MAILING """
VALIDITY_CONFIRM	= "7"
VALIDITY_CHGPWD		= "1"

MAIL_DEFAULT_SENDER = "EMAIL_HERE@gmail.com" 
MAIL_PASSWORD       = "EMAIL_PWD" 
MAIL_SERVER         = "smtp.googlemail.com"
MAIL_USERNAME       = "EMAIL_HERE@gmail.com"


""" RECAPTCHA """ ## from https://www.google.com/recaptcha/admin#site/338490121?setup and yourDevEmail@gmail.com account
RECAPTCHA_SECRET_KEY = "6LcJ8ywUAAAgaqcvqzaeAAFm7HLkyIF2Kn6PhUqtG8VOOOCfj"
RECAPTCHA_SITE_KEY   = "6LcJ8ywUAAAAafzgreaqsANYugpgfbEZEWVRyTy7RiwdjUa07"


""" CONFIG GOOGLE ANALYTICS / ... """
""" 
	INDEXING  : https://www.google.com/webmasters/verification/verification?hl=en&siteUrl=http://solidata.cleverapps.io/&continue=https://www.google.com/webmasters/tools/dashboard?hl%3Den%26authuser%3D3%26siteUrl%3Dhttp://solidata.cleverapps.io/%26sig%3DALjLGbMSPbWTn48JKVqv7WClemAPnPysHg&theme=wmt&authuser=3&priorities=vfile,vmeta,vdns,vanalytics,vtagmanager&tid=alternate 
	ANALYTICS : https://analytics.google.com/analytics/web/?authuser=3#management/Settings/a105171735w157018175p158556390/%3Fm.page%3DTrackingDataCollection/
"""