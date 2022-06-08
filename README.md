# Setup local

## Prequisite

mysql

python3.8

## Setup

Clone the repository

```shell
git clone git@github.com:tungnt247/django-blog-api.**git**
```

Create file `.env` same as file `.env.example`. Fill necessary variales value

Install dependencies

```shell
pip install -r requirements.txt
```

Create database in mysql-server

Run migration

```shell
python manage.py migrate
```

Create superuser

```shell
python manage.py createsuperuser
```

Run server

```shell
python manage.py runserver
```
