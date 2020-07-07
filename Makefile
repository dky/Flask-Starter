TAG_NAME=dkyio/flask
HOST_PORT=8000
FLASK_PORT=5000
APP_NAME=mobile-builds

build:
	docker build --build-arg http_proxy=$(PROXY) -t $(TAG_NAME) .
run:
	docker run -d --name $(APP_NAME) -p $(HOST_PORT):$(FLASK_PORT) $(TAG_NAME)
rm:
	docker rm -f $(APP_NAME)
restart:
	# We don't check if the container is running...
	docker rm -f $(APP_NAME)
	docker run -d --name $(APP_NAME) -p $(HOST_PORT):$(FLASK_PORT) $(TAG_NAME)
exec:
	docker exec -it $(APP_NAME) /bin/sh
test:
	curl --noproxy "*" http://localhost:$(HOST_PORT)
local:
	python app/app.py

