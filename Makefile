start_service:
	sudo service docker start

run:
	docker-compose up

stop:
	docker-compose down 

logs:
	docker-compose logs -f

.PHONY: run install
