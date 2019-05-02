export APP=apiviz
export DC_PREFIX= $(shell pwd)/docker-compose
export APP_PATH := $(shell pwd)
export BACKEND=${APP_PATH}
export FRONTEND=${APP_PATH}

#other variable definition
DC    := 'docker-compose'

frontend: network
	${DC} -f ${DC_PREFIX}-frontend.yml up --build -d

frontend-stop:
	${DC} -f ${DC_PREFIX}-frontend.yml down

network-stop:
	docker network rm ${APP}

network:
	@docker network create ${APP} 2> /dev/null; true

backend-gunicorn:
	${DC} -f ${DC_PREFIX}-backend-gunicorn.yml up --build -d

backend-gunicorn-stop:
	${DC} -f ${DC_PREFIX}-backend-gunicorn.yml down

up: network frontend backend-gunicorn

down: backend-gunicorn-stop frontend-stop network-stop

restart: down up
