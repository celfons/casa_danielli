https://docs.docker.com/

https://dev.mysql.com/downloads/installer/

git clone https://github.com/django/django

docker-compose up

docker-compose run web python /code/manage.py createsuperuser

docker-compose run web python /code/manage.py migrate

docker-compose up -d --build

http://127.0.0.1:8080/admin
