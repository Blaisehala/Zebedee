# A X E L

## Author
Blaise Hala

### Description
AXEL is a clone of Instagram

* Sign in to the application to start using.
* Upload my pictures to the application.
* 6See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

### Features
* authentication system
* search functionality
* Image details
* profile


#### View Live Site here

View the complete site here

Technologies Used
- Python 3.8
- Django MVC framework
- HTML and Bootstrap
- Postgressql
- Heroku



## Prerequisite
The Instaclan project requires a prerequisite understanding of the following:

* Django Framework
* Python3.8
* Postgres
* Python virtualenv
* Setup and installation
* Clone the Repo
* Activate virtual environment


## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

### Create the Database
- psql
- CREATE DATABASE nameofdatabase;
.env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DB_NAME = 'instaclan'
USER_NAME = '<Username>'
DB_PASSWORD = '<password>'
DEBUG = True
Run initial Migration
python3.8 manage.py makemigrations gallery
python3.8 manage.py migrate
Run the app
python3.8 manage.py runserver
Open terminal on localhost:8000


##### Known bugs
No known bugs so far. If found drop me an email.

Contributors
- Blaise Hala 
Contact Information
blaiseha@gmail.com | 