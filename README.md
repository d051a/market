# Installation / Установка
- Open the command line, navigate to the django app folder and execute:
- virtualenv *virtualenvname*
- Clone this repository to virtualenv folder
- Linux: source *virtualenvname*/bin/activate, Windows: call *virtualenvname*/Scripts/activate.bat
- pip install -r requirements.txt
- move to cloned repository folder
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
# runserver / запуск серевера
admin
P@ssw0rd
- Open http://127.0.0.1:8000/ in web browser.