https://docs.docker.com/

https://dev.mysql.com/downloads/installer/

git clone https://github.com/django/django

docker-compose build

docker-compose up

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec db /usr/bin/mysqldump -u root --password=123 casa > backup.sql

http://127.0.0.1:8080/admin
