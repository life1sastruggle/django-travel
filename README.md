# django-travel
The back-end of the travel web developed by Django, MySQL, Django REST framework.
>###Back-end 
>git clone https://github.com/life1sastruggle/django-travel.git  
>###Front-end
>git clone https://github.com/life1sastruggle/vue-travel.git  

## Run in local environment

+ Create superuser for admin
```
py manage.py createsuperuser
```
+ Execute commands in terminal for migrations
```
py manage.py makemigrations
py manage.py migrate
```
+ Install dependencies in requirements.txt
```
pip install -r requirements.txt
# You can use 'pip freeze > requirements.txt' to generate requirements.txt
```
+ Modify the database account and password in settings.py 
+ Run server
```
py manage.py runserver
```
