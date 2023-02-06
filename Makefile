
install:
	poetry install

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 test_project

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

requir:
	poetry export --without-hashes --format=requirements.txt > requirements.txt



compille_mess:
	poetry run django-admin compilemessages