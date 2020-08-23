# Django simple ToDo project

## Running process for Linux (Debian/Ubuntu)

### Install virtualenv and activate it
1. sudo apt install virtualenv python3-pip
2. virtualenv -p python3 .venv
3. source .venv/bin/activate

### Virtual Environment Requirements

* asgiref==3.2.10
* Django==3.1
* django-crispy-forms==1.9.2
* pkg-resources==0.0.0
* pytz==2020.1
* sqlparse==0.3.1


### clone this repository
1. git clone https://github.com/z4yed/django3-ToDo
2. cd django3-ToDo

### Run manage.py file

1. python3 manage.py runserver
2. Then Visit [localhost:8000](http://127.0.0.1:8000/)

### Optionally You can create superuser to view administration site.

1. python3 manage.py createsuperuser
2. visit [Admin Panel](http://127.0.0.1:8000/)


## Enjoy DJANGO
