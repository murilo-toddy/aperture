CONTAINER = aperture

up:
	docker-compose up

bg:
	docker-compose up -d

down:
	docker-compose down

psql:
	docker exec -it $(CONTAINER) psql -U postgres

setup_db:
	docker exec -it $(CONTAINER) psql -U postgres -d postgres -f /db-scripts/setup-tables.sql

app:
	python3 src/app/main.py

clear:
	clear

sleep:
	sleep 3

bootstrap: setup_db clear app

all: bg sleep bootstrap