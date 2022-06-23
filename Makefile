run:
	python manage.py runserver 8005

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

test:
	python3 manage.py test


