.DEFAULT_GOAL := default_target
# Default
default_target: clean code-convention test
# Code style
code-convention:
	flake8
	pycodestyle
# Remove useless files
clean:
	rm -fr .coverage
	rm -fr .pytest_cache/

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
	PYTHON_PATH=. pytest --cov=.

# Start celery
celery-run:
	celery -A project worker -l info --without-gossip --without-mingle --without-heartbeat