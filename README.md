# Customer Management App
A webapp to manage customers and their orders.

## How to setup:

This project was setup using python 3.7.5, so it's recommended to install it and use it. All these commands are for ubuntu.

* Install virtual environment [virtualenv] (if already installed, ignore this step).
* Make a folder where you want to setup your work, let say *‘customermanagement’*.
* Change directory to your new folder. ```cd customermanagement```.
* Git clone repo. ```git clone <url>```.
* Make virtual environment in naming it *‘venv’*. ```virtualenv -p python3.7 <nameOfVirtualEnv>``` in your case *‘venv’*.
* Activate your virtual environment, ```source venv/bin/activate```.
* Now install all the dependencies by ```pip install -r requirements.txt```.
* Run the migrate command to complete the steps, ```python manage.py migrate```.
* Run `python manage.py collectstatic` to collect all the static files like images, CSS, JS, etc.
* Now you can run the server. ```python manage.py runserver```