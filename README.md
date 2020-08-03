# LibraryRestAPI
This is the git repository for the library API project!
##  Development Environment Setup

### Cloning Project
1. (Optional) You can install [GitHub Desktop](https://desktop.github.com/) and clone from its interface to avoid ssh configuration.


2. To clone, go to your desired directory and run:
```
git clone https://github.com/castilhos90124/LibraryRestAPI.git
```
### VirtualEnv Setup

1. To install your virtual environment, run these commands:
```
pipx install virtualenv
virtualenv --help
```
2. To create your virtual environment, go to your project's directory and run:
```
virtualenv <virtualenv-name>
```

3. To activate your virtual environment, run: 
```
.\<name-to-virtualenv>\Scripts\activate
```

4. After this, you should see your virtual env name in powershell.
```
(<virtualenv-name>) PS C:\Users\...
```

5. To install Django in our virtual env, run:
```
python -m pip install Django
```

6. To install Django REST Framework, run:
```
pip install djangorestframework
pip install markdown
pip install django-filter
```

7. To create the database file, go to manage location folder and run:
```
python .\manage.py migrate
```
8. Finally, to create a superuser, run:
```
python manage.py createsuperuser
```
### Starting Server
1. To start your local server, run:
```
python .\manage.py runserver
```

2. To access it, go to http://127.0.0.1:8000/.


