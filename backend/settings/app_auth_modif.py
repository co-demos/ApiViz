# -*- encoding: utf-8 -*-

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES ONLY FOR ADMIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###


""" 
available roles

"admin"     : { "help" : "can access all backoffice (lox level access)" },
"staff"     : { "help" : "can access backoffice (high level access)" },
"registred" : { "help" : "registred user" },
"guest"     : { "help" : "logged but not registred" },
"anonymous" : 
"""

COLLECTIONS_AUTH_MODIFICATIONS	= {
  "global"    : {
    'POST'    : ['admin'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
  "footer"    : {
    'POST'    : ['admin', 'staff'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
  "navbar"    : {
    'POST'    : ['admin', 'staff'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
  "endpoints" : {
    'POST'    : ['admin'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
  "styles"    : {
    'POST'    : ['admin', 'staff'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
  "routes"    : {
    'POST'    : ['admin', 'staff'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
  "socials"   : {
    'POST'    : ['admin', 'staff'], 
    'DELETE'  : ['admin'], 
    'GET'     : ['all']
  },
}

