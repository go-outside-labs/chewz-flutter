start_service:
	sudo service docker start

run:
	docker-compose up

stop:
	docker-compose down 

logs:
	docker-compose logs -f

dc_clean:
	docker-compose build --no-cache

.PHONY: run install start_service dc_clean logs
