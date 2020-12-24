# Image Detection
This project prepared detects images from the camera and check weather image matches with the criminal database or missing database. Once all these get computerized to work efficiency of the police officer will get increases. “Image Detection System” has been designed to automate the process of matching image. System can make the daily activities efficient and providing the fast response to store and retrieve information to the police officer by the android or web application.

Requirement:-
Python 3.8
Django
Pillow
Face-recognition


Create Project:
1. Install django
pip install django
2. Install environment
pip install pipenv
3. Create Project
django-admin startproject Image_Detection
4. Create environment
pipenv install
5. Run environment
pipenv shell
6. Install django in environment
pipenv install django
7. Install psycopg2-binary
pip install psycopg2-binary
8. Make migration
python manage.py makemigrations
9. Migrate
python manage.py migrate
10. Create superuser
python manage.py createsuperuser
11. Create app
python manage.py startapp user

python manage.py startapp criminal
python manage.py startapp missing
python manage.py startapp feedback
python manage.py startapp news
12. Install pillow
pip install pillow
13. Install face recognition
pip install face-recognition
