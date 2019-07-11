.PHONY: makemigrations
makemigrations:
	docker-compose run --rm web python manage.py makemigrations


.PHONY: migrate
migrate:
	docker-compose run --rm web python manage.py migrate


.PHONY: dshell
dshell:
	docker-compose run --rm web python manage.py shell


.PHONY: flake
flake:
	docker-compose run --rm web flake8 .


.PHONY: psql
psql:
	docker-compose run --rm postgres psql --host=postgres --dbname=postgres --username=postgres
