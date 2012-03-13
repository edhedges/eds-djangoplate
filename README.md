Eddie Hedges' Django Boilerplate
=========

This is my personalized django project boilerplate. I made it to make starting a new project quick and efficient.

I would like to site my sources and inspiration for the project below: 
    
* [kstateome](https://github.com/kstateome)
* [gpennington](https://github.com/gpennington)
* [dstegelman](https://github.com/dstegelman)
* [jonfaustman](https://github.com/jonfaustman)
* [jordanorelli](https://github.com/jordanorelli)

Without the above sources my boilerplate would not have been possible.

I use virtualenv with virtualenvwrapper for local development and have written a short bash script that starts a project for me to develop locally in one simple command: `mkdjangoproj myproject`.

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
	}

The boilerplate comes with a sample app that can be renamed, modified, or deleted it is basically only there for reference.

So once I run the mkproject function from my bash it does a number of things:

	- Creates a virtualenv and project with the same name to be pythonic!
	- Initializes the project as an empty git repo and pulls the boilerplate from github.
	- Removes the README.md file.
	- Installs django, south, and fabric.
	- Makes manage.py executable and creates a new secret key, runs syncdb, and starts the local dev server.


Here is a list of the bare minimum files that NEED edited before deployment besides normal development: 
	
	- settings.py
	- project.py
	- httpd-vhosts.conf
	- fabfile.py
	- httpd.conf

For deployment, redeployment, and more see fabfile.py and read code.