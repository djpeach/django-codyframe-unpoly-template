migration:
	python manage.py makemigrations
	python manage.py migrate
cache:
	python manage.py createcachetable
superuser:
	python manage.py createsuperuser
shell:
	python manage.py shell
static:
	python manage.py collectstatic --no-input
server:
	python manage.py runserver 0.0.0.0:8000