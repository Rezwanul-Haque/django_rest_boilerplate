# This is a project boilerplate for Django to deploy a secure Django project on any web hosting site.

# Please install virtualenv on your local computer
```pip install virtualenv```

### This is what I like do when creating a virtual environment (you can change whatever you like)
(I always like to called the virtual environment as venv)
# Creating virtual environment

```virtualenv venv```

```cd venv```

```
## For Windows
scripts\activate

## For Linux
source bin\activate
```

```cd ..```

## Installing requirements

```cd src```

```pip install -r requirements-dev.txt```

### And for production environment

```pip install -r requirements-prod.txt```

Then I create the django project.

```django-admin startproject project_name```

## But anyone who use this boilerplate will already create a project called mysite which is inside the src folder

# Custom management command (core)
A management custom command added to rename project name and all the related places where changes must be done to run the project.
## For changing the project name run the following command.
```python manage.py rename project_name```

so current folder structure would be like this...

django-project-boilerplate(project folder)

.
+-- .git
+-- src
|   +-- core
|   +-- mysite
|   +-- templates
|   +-- .env
|   +-- manage.py
|   +-- requirements.dev.txt
|   +-- requirements.prod.txt
+-- venv
|   +-- Scripts
+-- README.md
+-- LICENSE

For security purpose this boilerplate uses python-decouple to secure all sensitive variables like SECRECT_KEY, Production level database username, password etc to a secure file called .env

## A example of the .env file given as .env.example

### For local development you can rename the .env.example file to .env to run the project on local computer.

The boilerplate can be improved so please let me know how to improve...

# Core app
Django suggest if any custom command has to create for a project it should be on the core > management > command folder.
Like I created the rename command

# Lets talk about the settings of the project
>src > mysite > settings
There are three file
1. base.py
2. developement.py
3. production.py

base.py file has contain things that both needed for both development and production settings.

# Development settings
Development settings included Django debug tools and which is helpful for debugging a Django project.

# Production settings
Production settings I configured Database to use PostgreSQL so to secure the database sensitive information like DB_NAME, DB_USER, DB_PASSWORD etc I use the python-decouple module.

By default python-decouple check for .env file for sensitive information of the project.

### This .env file should not be push on the public repository. You can create variable on the hosting site so just created their will auto fetch value by python-decouple module.

Checkout the .env.example file to create a .env file

# Note .env.example file contain the Django project SECRET_KEY and it's just a 50 character long random number so you can change it when you use this boilerplate.

# Final instruction
If anyone want to change the project to use the production settings just change one place only.

# Edit manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')
to
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')
