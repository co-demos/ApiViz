
<h2 align=center>
	<img src="./app/static/logos/app_default/logo_apiviz_15.png">
</h2>


-------
## PRESENTATION

Visualize data coming from an API in a CMS-like app

--------

## DEVELOPERS

Please check out our *[guidelines](./GUIDELINES_DEV.md)*

--------

## INSTALLATION WALKTHROUGH 

### _WITH DOCKER (locally or in production)_


1. **locally - in your browser check this url**
    - install [Docker](https://docs.docker.com/docker-for-mac/install/) (here for mac OS) 
    - clone or [download](https://github.com/co-demos/ApiViz/archive/master.zip) the repo
    - [install MongoDB](https://docs.mongodb.com/manual/installation/) locally/on your server** or get the URI of the MongoDB you're using
    - go to your apiviz folder
    - launch docker and run : 
        ```sh
        docker up
        ```
    - check the following URL in your browser : 
      ```
      http://localhost:8100
      ```
    - you can also use those other docker commands : 
      ```sh
       
      ### for local dev 
      # local DB
      docker up
      docker restart
      docker down
      # distant DB - you need to set up "app/config/config_secret_vars_example.py" 
      docker up-dist
      docker restart-dist
      docker down-dist

      ### for testing
      # local DB 
      docker up-test
      docker restart-test
      docker down-test
      # distant DB - you need to set up "app/config/config_secret_vars_example.py"  
      docker up-test-dist
      docker restart-test-dist
      docker down-test-dist
      ```

1. **in production** 
    - install [Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) on your server (here for Ubuntu 18) 
    - set up UFW, GIT, NGINX, 
    - (optional) [install MongoDB](https://docs.mongodb.com/manual/installation/) (if the ApiViz's DB for config is hosted on your own server)
    - add the github repo
    - create and set a `app/config_app/config_secret_vars_prod.py` file based on `config_secret_vars_example.py` structure
    - lauch docker and run the command : 
      ```sh
      docker up-prod
      ```
    - you can also use those other docker commands : 
      ```sh
       
      ### for production 
      # distant DB 
      docker up-prod
      docker restart-prod
      docker down-prod
      # server DB 
      docker up-prod-server
      docker restart-prod-server
      docker down-prod-server

      ### for preprod 
      # distant DB 
      docker up-preprod
      docker restart-preprod
      docker down-preprod
      # server DB 
      docker up-preprod-server
      docker restart-preprod-server
      docker down-preprod-server


      ### for testing 
      # distant DB 
      docker up-test-dist
      docker restart-test-dist
      docker down-test-dist
      # server DB 
      docker up-test-server
      docker restart-test-server
      docker down-test-server

      ```

### _WITHOUT DOCKER - LOCALLY_

1. **clone or [download](https://github.com/co-demos/ApiViz/archive/master.zip) the repo**
1. **[install MongoDB](https://docs.mongodb.com/manual/installation/) locally** or get the URI of the MongoDB you're using
1. **go to your apiviz folder**
1. **use Python 2**
1. **install python pip and virtualenv**
	```sh 
	sudo apt install python-pip
	sudo apt install virtualenv
	```


1. **install a [virtual environment](https://pypi.python.org/pypi/virtualenv)**
	```sh
	virtualenv venv
	source venv/bin/activate
	````
		
1. **install the libraries**

	```sh
	sudo pip install -r requirements.txt
	```

1. if any problem occur here try to reinstall pip with 

    ```sh
      curl https://bootstrap.pypa.io/get-pip.py | python
    ```


1. **optional** : _update the `app/config_app/config_secret_vars_example.py` file with your mongoDB URI (if you're not using default mongoDB connection_
	>

1. **Go to your app folder and run :**

	```sh
	python run_apiviz.py
	````
1. **optional** : you can also use some variables in the command line : 
	```sh
	# get the list of available CLI options
	python run_apiviz.py --help

	# for example : run with a custom port number in testing mode
	pythom run_apiviz.py --port=8200 --mode=preprod
	```

1. **Install Node.js and npm**
	>

1. **Build the front-end**
	
	```sh
	cd app/frontend
	npm install

	# build the bundle.js
	npm run build

	# you can also build and watch the bundle.js
	npm run watch
	```

1. **optional** : _if you encounter problems while building try this_
	
	```sh
	rm -rf app/frontend/node_modules
	npm install 
	npm run build
	```

1. **check in your browser** at `localhost:8100`


### _WITHOUT DOCKER - IN PRODUCTION_

1. **get a server** - check digital ocean, OVH, ...
1. optionnal : get a domain name : check OVH, namecheap, godaddy.... + setup DNS
1. **follow (most of) these [instructions](https://github.com/entrepreneur-interet-general/tutos-2018/wiki/Admin-Sys)**
1. **create a `app/config_app/config_secret_vars_prod.py` file** based on `config_secret_vars_example.py` structure
1. **go to app folder and create a virtual env** (for instance called "venv")
1. **set up the [gunicorn service](./unit/working_service_config.service) and [NGINX](./nginx/working_nginx_config)** accordingly 

1. ... pray for all that to work as expected, and keep calm... 

1. **update code and (re-)deploy**

    ```sh
    cd /<your_app_folder>/<username>/app_apiviz
    git pull origin master
    cd app/frontend

    # build the frontend
    npm install
    npm run build

    # rerun app
    sudo systemctl restart apiviz
    ```




------

## TECHNICAL POINTS

#### Tech stack
- _Language_ : **Python**... because ... uuh ... eeeh ... I like this language too much ? 
- _Backend_  : **[Flask](http://flask.pocoo.org/)**... minimalistic Python framework
- _Frontend_ : **[Bulma](https://bulma.io/)** as CSS framework, **[Vue.js](https://vuejs.org/)** as JS framework, **[Axios](https://github.com/axios/axios)** for API queries (to make queries to [Solidata](https://github.com/entrepreneur-interet-general/solidata_backend) or else), **[Leaflet](https://leafletjs.com)** and **[Vue2Leaflet](https://github.com/KoRiGaN/Vue2Leaflet)** for map layout
- _Server_   : **[Ubuntu 18.04]()**, **[NGINX](https://www.nginx.com/)**, **[Gunicorn](http://gunicorn.org/)**, hosted in **[Digital Ocean](http://digitalocean.com/)**, domain name from **[NameCheap](http://namecheap.com/)**


-------

## CREDITS 

#### ApiViz's team thanks :

- the [EIG](https://entrepreneur-interet-general.etalab.gouv.fr/) program by [Etalab](https://www.etalab.gouv.fr/)
- the [SocialConnect](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/socialconnect/) project, aka "Carrefour des Innovations Sociales"
- the [CGET](http://www.cget.gouv.fr/)
- the [MedNum](https://lamednum.coop)
- the [Mission Société Numérique](https://societenumerique.gouv.fr)

#### Contacts - maintainance :

- [Julien Paris](<mailto:codemos.infos@gmail.com>) (aka [JPy](https://github.com/JulienParis) on Github)
- [Guillaume Lancrenon](https://guillim.github.io) (aka [Guillim](https://github.com/guillim) on Github)


-------

## SCREENSHOTS (development)


...TO DO 


