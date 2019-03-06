
<!-- <h1 align=center> APIVIZ </h1>

--------- -->

<h2 align=center>
	<img src="./app/static/logos/app_default/logo_apiviz_15.png">
</h2>


-------
## PRESENTATION

Visualize data coming from an API in a CMS-like app

--------

## DEVELOPPERS

Please check out our *[guidelines](./GUIDELINES_DEV.md)*

--------

## INSTALLATION WALKTHROUGH 

### _LOCALLY_

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

1. **optional** : _if you encounter problems installing the requirements try to install the 'cryptography' library following those steps :_

	```sh
	# install crypto
	pip install cryptography --global-option=build_ext --global-option="-L/usr/local/opt/openssl/lib" --global-option="-I/usr/local/opt/openssl/include"
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
	pythom run_apiviz.py --port=8200 --mode=testing
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


### _PRODUCTION_

1. **get a server** - check digital ocean, OVH, ...
1. optionnal : get a domain name : check OVH, namecheap, godaddy.... + setup DNS
1. **follow (most of) these [instructions](https://github.com/entrepreneur-interet-general/tutos-2018/wiki/Admin-Sys)**
1. **create a `app/config_app/config_secret_vars_prod.py` file** based on `config_secret_vars_example.py` structure
1. **go to app folder and create a virtual env** (for instance called "venv")
1. **set up the [gunicorn service](./unit/working_service_config.service) and [NGINX](./nginx/working_nginx_config)** accordingly 
1. ... pray for all that to work as expected, and keep calm... 


### _PRODUCTION_ : update code and deploy


```sh
cd /<your_app_folder>/<username>/app_apiviz
git pull origin master
cd app/frontend

# build the frontend
npm ci
npm run build

# rerun app
sudo systemctl restart apiviz
```


#### Creating the first admin account

Go to `/register`, create an account, then:
```sh
# Connect to MongoDB
mongo
# => mongo shell prompts

# Use cis-front database
use apiviz

# list users
db.users.find()

# get the id of the user you want to move to admin
# abcdef

# Modify user
db.users.updateOne({_id: ObjectId('abcdef')}, {$set: {userAuthLevel: 'admin'}})
```

Then, you can login with your admin user which can change settings of other users 



------

## TECHNICAL POINTS

#### Tech stack
- _Language_ : **Python**... because ... uuh ... eeeh ... I like this language too much ? 
- _Backend_  : **[Flask](http://flask.pocoo.org/)**... minimalistic Python framework
- _Frontend_ : **[Bulma](https://bulma.io/)** as CSS framework, **[Vue.js](https://vuejs.org/)** as JS framework, **[Ajax]()** for API queries (to make queries to [Openscraper](https://github.com/entrepreneur-interet-general/OpenScraper) )
- _Server_   : **[Ubuntu 16.04]()**, **[NGINX](https://www.nginx.com/)**, **[Gunicorn](http://gunicorn.org/)**, hosted in **[Digital Ocean](http://digitalocean.com/)**, domain name from **[OVH](http://ovh.com/)**


-------

## CREDITS 

#### ApiViz's team thanks :

- the [SocialConnect](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/socialconnect/) project, aka "Carrefour des Innovations Sociales"
- the [EIG](https://entrepreneur-interet-general.etalab.gouv.fr/) program by [Etalab](https://www.etalab.gouv.fr/)
- the [CGET](http://www.cget.gouv.fr/)

#### Contacts - maintainance :

- [Julien Paris](<mailto:codemos.infos@gmail.com>) (aka [JPy](https://github.com/JulienParis) on Github)
- [Guillaume Lancrenon](<mailto:codemos.infos@gmail.com>) (aka [Guillim](https://github.com/guillim) on Github)


-------

## SCREENSHOTS (development)



<h4 align=center><br>login</h4>

![alt text](./screenshots/cis-front-login.png "home")

-------

<h4 align=center><br>register</h4>

![alt text](./screenshots/cis-front-register.png "register")


