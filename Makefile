start_service:
	sudo service start

install:
	npm install

run:
	docker-compose up

stop:
	docker-compose down 

.PHONY: run install