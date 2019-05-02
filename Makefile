export APP=apiviz

export D_FOLDER=docker-files
export DC_FOLDER=dockercomposes
export DF_FOLDER=dockerfiles

#other variable definition
# DC    := docker-compose
# DF    := Dockerfile.

export DC=docker-compose
export DF=Dockerfile.

export DC_PREFIX= $(shell pwd)/${DC}
export DC_PREFIX_FOLDER= $(shell pwd)/${D_FOLDER}/${DC_FOLDER}/${DC}

export DC_FOLDER_SUBPATH= ${D_FOLDER}/${DC_FOLDER}
export DF_FOLDER_SUBPATH= ${D_FOLDER}/${DF_FOLDER}

export APP_PATH := $(shell pwd)

export BACKEND=${APP_PATH}
export FRONTEND=${APP_PATH}



### ============ ###
### network
### ============ ###

network-stop:
	docker network rm ${APP}
network:
	@docker network create ${APP} 2> /dev/null; true


### ============ ###
### frontend
### ============ ###

frontend: 
	${DC} -f ${DC_PREFIX_FOLDER}-frontend.yml up --build -d
frontend-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-frontend.yml down



### ============ ###
### backend
### ============ ###

# ------------------
# default - local DB 
backend-gunicorn-default-local:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-default-local.yml up --build -d
backend-gunicorn-default-local-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-default-local.yml down

# default - distant DB 
backend-gunicorn-default-dist:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-default-dist.yml up --build -d
backend-gunicorn-default-dist-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-default-dist.yml down

# ------------------
# test - local DB 
backend-gunicorn-test-local:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-test-local.yml up --build -d
backend-gunicorn-test-local-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-test-local.yml down

# test - distant DB 
backend-gunicorn-test-dist:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-test-dist.yml up --build -d
backend-gunicorn-test-dist-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-test-dist.yml down

# test - server DB 
backend-gunicorn-test-server:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-test-server.yml up --build -d
backend-gunicorn-test-server-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-test-server.yml down

# ------------------
# # preprod - server DB 
backend-gunicorn-preprod-server:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-preprod-server.yml up --build -d
backend-gunicorn-preprod-server-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-preprod-server.yml down

# # preprod - distant DB 
backend-gunicorn-preprod-dist:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-preprod-dist.yml up --build -d
backend-gunicorn-preprod-dist-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-preprod-dist.yml down

# ------------------
# # production - server DB 
backend-gunicorn-prod-server:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-prod-server.yml up --build -d
backend-gunicorn-prod-server-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-prod-server.yml down

# # production - distant DB 
backend-gunicorn-prod-dist:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-prod-dist.yml up --build -d
backend-gunicorn-prod-dist-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-prod-dist.yml down



### ============================= ###
### main make / docker commands
### ============================= ###

# --------------------
# default - local DB
up: network frontend backend-gunicorn-default-local
down: backend-gunicorn-default-local-stop frontend-stop network-stop
restart: down up

# default - distant DB
up-dist: network frontend backend-gunicorn-default-dist
down-dist: backend-gunicorn-default-dist-stop frontend-stop network-stop
restart-dist: down-dist up-dist

# --------------------
# testing - local DB
up-test-local: network frontend backend-gunicorn-test-local
down-test-local: backend-gunicorn-test-local-stop frontend-stop network-stop
restart-test-local: down-test-local up-test-local

# testing - server DB
up-test-server: network frontend backend-gunicorn-test-server
down-test-server: backend-gunicorn-test-server-stop frontend-stop network-stop
restart-test-server: down-test-server up-test-server

# testing - distant DB
up-test-dist: network frontend backend-gunicorn-test-dist
down-test-dist: backend-gunicorn-test-dist-stop frontend-stop network-stop
restart-test-dist: down-test-dist up-test-dist

# --------------------
# preprod - server DB
up-preprod-server: network frontend backend-gunicorn-preprod-server
down-preprod-server: backend-gunicorn-preprod-server-stop frontend-stop network-stop
restart-preprod-server: down-preprod-server up-preprod-server

# preprod - distant DB
up-preprod-dist: network frontend backend-gunicorn-preprod-dist
down-preprod-dist: backend-gunicorn-preprod-dist-stop frontend-stop network-stop
restart-preprod-dist: down-preprod-dist up-preprod-dist

# --------------------
# prod - server DB
up-prod-server: network frontend backend-gunicorn-prod-server
down-prod-server: backend-gunicorn-prod-server-stop frontend-stop network-stop
restart-prod-server: down-prod-server up-prod-server

# prod - distant DB
up-prod-dist: network frontend backend-gunicorn-prod-dist
down-prod-dist: backend-gunicorn-prod-dist-stop frontend-stop network-stop
restart-prod-dist: down-prod-dist up-prod-dist