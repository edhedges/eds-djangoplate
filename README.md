Eddie Hedges' Django Boilerplate
=========

This boilerplate was made so that I can create a development standard for myself when using django. 

I tried to keep it simple while also having the flexibility that will allow me to locally develop and quickly turn around and push the project to production.

In my local development I use django along with pip, virtualenv, virtualenvwrapper, and any other python modules I see necessary.

To make my development even better I will write a .bashrc script that does the following things:

  - Create and activate a virtualenv and a related project 
  - Grab my boilerplate and use it as the project start
  - Remove the README.md file
  - Install the requirements of the project such as django, PIL, etc.
  - Create a new secret key for the project
  - Run syncdb and runserver
  - Last line just opens the project directory in Sublime Text 2

Here is the script:

	mkdjangoproj () {
	mkproject --no-site-packages --prompt=$1: $1 &&
	git init &&
	git pull git@github.com:edhedges/eds-djangoplate.git master &&
	rm README.md &&
	pip install -r requirements.txt &&
	chmod +x manage.py
	./manage.py new_secret &&
	./manage.py syncdb &&
	./manage.py runserver
	sublime ../
	}

I will name this script mkdjangoproj and by typing:
    
    mkdjangoproj project_name

It will create a new django project with my boilerplate named project_name.

This django boilerplate comes with two sample apps which will be included in the INSTALLED_APPS settings. If you would change their directory names make sure to change the names elsewhere like their urls, the project urls, the app views, and the project settings.

I got my inspiration for this boilerplate from [Jordan Orellis Django Skeleton](https://github.com/jordanorelli/Django-Skeleton)

If you aren't familiar with virtualenv/virtualenvwrapper you need to know that if you want to install packages into your virtualenv you need to open a new terminal tab/window and type:
	
	workon myvirtualenv

This will then allow you to type:

	pip install whateverpackagesyouwant

Note: If you use this for development and want to use the .wsgi file I have put in there for when you push to production make sure to edit the file name to not be 'project.wsgi' but replace 'project' with what your projects name is as well as open and edit the necessary name issues used by the wsgi file.