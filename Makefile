#Database
migrations:
	./manage.py makemigrations

db-up:
	./manage.py migrate

#Setup
pip:
	pip install pip --upgrade

setup: pip
	pip install -r requirements/base.txt

setup-dev: pip
	pip install -r requirements/local.txt

setup-production: pip
	pip install -r requirements/production.txt

#Start server locally
start:
	./manage.py runserver

# Test
test:
	pytest --cov=.

# Start celery
celery-run:
	celery -A project worker -l info --without-gossip --without-mingle --without-heartbeat
