start_service:
	sudo service docker start

install:
	npm install

run:
	docker-compose up

stop:
	docker-compose down 

logs:
	docker-compose logs -f

.PHONY: run install