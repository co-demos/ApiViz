# -*- encoding: utf-8 -*-

import os
import click 

### set environment variable 
# os.environ['FLASK_CONFIGURATION'] = "default" # "testing" / "production"
### change environment var to "production" for debugging
# os.environ['FLASK_CONFIGURATION'] = "production"


# from app import app

debug = True




@click.command()
@click.option('--mode', 	  default="default", 		nargs=1,	help="The <mode> you need to run the app : default | testing | preprod | production" )
@click.option('--docker', 	default="docker_off", nargs=1,	help="Are you running the app with <docker> : docker_off | docker_on" )
@click.option('--mongodb', 	default="local", 	  	nargs=1,	help="The <mongodb> you need to run the app : local | distant | server" )
@click.option('--host', 	  default="localhost", 	nargs=1,	help="The <host> name you want the app to run on : <IP_NUMBER> " )
@click.option('--port',   	default="8100", 			nargs=1,	help="The <port> number you want the app to run on : <PORT_NUMBER>")
@click.option('--https', 	  default="false", 			nargs=1,	help="The <https> mode you want the app to run on : true | false")
def app_runner(mode, docker, mongodb, host, port, https) :
  """
  app_runner

  """

  print "= "*50
  print "= = = RERUN FLASK APP FROM APP RUNNER = = ="
  print "= "*50


  ### WARNING : CLIck will treat every input as string as defaults values are string too
  print "\n=== CUSTOM CONFIG FROM CLI ===\n"
  print "=== mode 	 : ", mode
  print "=== docker  : ", docker
  print "=== mongodb : ", mongodb
  print "=== host    : ", host
  print "=== port  	 : ", port
  print "=== https 	 : ", https

  if https == "true" : 
    http_mode = "https"
  else : 
    http_mode = "http"

  ### apply / overwrites host configuration
  if mode != "default" : 
    print "=== mode : ", mode
    os.environ["FLASK_CONFIGURATION"] = str(mode)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default') ### 'default' for local dev
    print "=== config_name : ", config_name

  ### SET UP ENV VARS FROM CLI 
  os.environ["DOMAIN_ROOT"]	 = host
  os.environ["DOCKER_MODE"]  = docker
  os.environ["MONGODB_MODE"] = mongodb
  os.environ["DOMAIN_PORT"]	 = port
  os.environ["SERVER_NAME"]	 = host + ":" + port
  os.environ["DOMAIN_NAME"]	 = http_mode + "://" + host + ":" + port

  ### create app by importing app.__init__
  from app import app

  ### simple flask runner
  app.run( debug=debug, host=host, port=port, threaded=True )



if __name__ == '__main__':
  """ 
  runner for the CIS front Flask app 
  - gets most of its variables at start from environment variables
  - 

  in command line just type : 
  "python run_apiviz.py"

  """

  app_runner()
