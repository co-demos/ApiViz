
<h2 align=center>
	<img src="./backend/static/logos/app_default/logo_apiviz_15.png">
</h2>


-------
## PRESENTATION

Visualize data coming from an API in a CMS-like app. 
If your data is somewhere, ApiViz can transform it into a full website to show it at its best. 


--------

## THE APIVIZ ECOSYSTEM

ApiViz is designed to **agnosticaly display data** and provide an engine to deploy a **datavisualisation website** without (too much) pain, not regarding to the service(s) serving and storing the data. 

Nevertheless to do so an instance of ApiViz must be connected to several external services : one for authentication, one for serving the data, one for storing the static contents (html pages, images...).

The goal of ApiViz is to **work with any external service** fulfilling those roles, but we developed an **eco-system of open source applications** allowing a complete and free way to deploy such a datavisualisation service. 

- [Apiviz](https://github.com/co-demos/ApiViz) as the high-level app for visualisation, a sort of open source CMS for data-visualisation ; 
- [Solidata](https://github.com/entrepreneur-interet-general/solidata_frontend) to "API-fy" your data and manage open data projects ;
- [TokTok](https://github.com/co-demos/toktok) for a dedicated authentication service to manage users, JWT, and roles. 

In the following illustration you can have a general idea of how those several services could work altogether. Check the [`/documentation`](./documentation) folder to have a broader look to [other configurations](./documentation/APIVIZ_CONFIGURATIONS-export.pdf).

<h2 align=center>
	<img src="./documentation/APIVIZ CONFIGURATIONS-export-details.jpg">
</h2>

You can also check those several projects and repository to find some layout for your specific new datavisualisation website : 
- Sonum repo ;
- CIS repo ;
- ... and more to come...


--------

## HOW TO CONFIGURE YOUR APIVIZ INSTANCE

1. register an user (user data will stored and managed in TokTok) ;
1. make this user an `admin` (in TokTok) ;
1. log in (`admin` link in the default footer) ;
1. go to the `back office` ;
1. set up your ApiViz configuration : 
    
    - set up the global variables ; 
    - set up your data endpoints ; 
    - set up your authentication endpoints ; 
    - set up your routes (pages must point out to html contents, f.e. on Github) ; 
    - set up the styles ;
    - set up your navbar ; 
    - set up your footer ;

1. save your configuration ;
1. deploy (if not done already) and enjoy ;

More detailed configuration documentation on its way...

--------

## DEVELOPERS

Please check out our *[guidelines](./GUIDELINES_DEV.md)*

--------

## INSTALLATION WALKTHROUGH 

### _WITH DOCKER (locally or in production)_


1. **locally - in your browser check this url**
    - install [Docker (here for mac OS)](https://docs.docker.com/docker-for-mac/install/) 
    - clone or [download](https://github.com/co-demos/ApiViz/archive/master.zip) the repo
    - [install MongoDB](https://docs.mongodb.com/manual/installation/) locally/on your server** or get the URI of the MongoDB you're using
    - go to your apiviz folder
    - launch docker and run : 
        ```sh
        make up
        ```
    - check the following URL in your browser : 
      ```
      http://localhost:8081
      ```
    - (optional) you can also use those other docker commands : 
      ```sh
       
      ### for local dev 
      # local DB
      make up
      make restart
      make down
      # distant DB - you will need to set up your mongodb URI in "app/config/config_secret_vars_example.py"  
      make up-dist
      make restart-dist
      make down-dist

      ### for testing mode
      # local DB 
      make up-test
      make restart-test
      make down-test
      # distant DB - you will need to set up your mongodb URI in "app/config/config_secret_vars_example.py"  
      make up-test-dist
      make restart-test-dist
      make down-test-dist
      ```

1. **in production** 
    - install [Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) on your server (here for Ubuntu 18) 
      ```sh
      sudo apt-get update
      sudo apt-get remove docker docker-engine docker.io
      sudo apt install docker.io
      sudo systemctl start docker
      sudo systemctl enable docker
      ```
    - set up UFW, GIT, NGINX, ...
    - (optional) [install MongoDB](https://docs.mongodb.com/manual/installation/) (if the ApiViz's DB for config is hosted on your own server)
    - add the github repo
    - create and set a `app/config_app/config_secret_vars_prod.py` file based on `config_secret_vars_example.py` structure
    - lauch docker and run the command : 
      ```sh
      make up-prod
      ```
    - you can also use those other docker commands : 
      ```sh
       
      ### for production 
      # distant DB 
      make up-prod
      make restart-prod
      make down-prod
      # server DB 
      make up-prod-server
      make restart-prod-server
      make down-prod-server

      ### for preprod 
      # distant DB 
      make up-preprod
      make restart-preprod
      make down-preprod
      # server DB 
      make up-preprod-server
      make restart-preprod-server
      make down-preprod-server

      ### for testing 
      # distant DB 
      make up-test-dist
      make restart-test-dist
      make down-test-dist
      # server DB 
      make up-test-server
      make restart-test-server
      make down-test-server

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
- _Language_ : **Python**... because ... uuh ... eeeh ... we like this language too much ? 
- _Backend_  : **[Flask](http://flask.pocoo.org/)**... minimalistic Python framework
- _Frontend_ : **[Bulma](https://bulma.io/)** as CSS framework, **[Vue.js](https://vuejs.org/)** as JS framework, **[Axios](https://github.com/axios/axios)** for API queries (to make queries to [Solidata](https://github.com/entrepreneur-interet-general/solidata_backend) or else), **[Leaflet](https://leafletjs.com)**, **[Vue2Leaflet](https://github.com/KoRiGaN/Vue2Leaflet)**, and [PruneCluster]() for map layout
- _Server_   : **[Ubuntu 18.04]()**, **[NGINX](https://www.nginx.com/)**, **[Gunicorn](http://gunicorn.org/)**, hosted in **[Digital Ocean](http://digitalocean.com/)**, domain name from **[NameCheap](http://namecheap.com/)**


-------

## CREDITS 

#### ApiViz's team thanks :

- the [EIG](https://entrepreneur-interet-general.etalab.gouv.fr/) program by [Etalab](https://www.etalab.gouv.fr/)
- the [SocialConnect](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/socialconnect/) project, aka "Carrefour des Innovations Sociales"
- the [CGET](http://www.cget.gouv.fr/)
- the [MedNum](https://lamednum.coop)
- the [Mission Société Numérique](https://societenumerique.gouv.fr)
- and all those who believed and helped in this project...

#### Contacts - maintainance :

- [Julien Paris](<mailto:codemos.infos@gmail.com>) (aka [JPy](https://github.com/JulienParis) on Github)
- [Guillaume Lancrenon](https://guillim.github.io) (aka [Guillim](https://github.com/guillim) on Github)

#### Design UI-UX
- [Elise Lalique]()


-------

## SCREENSHOTS (development)


...TO DO 


