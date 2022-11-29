# Todo_App
#A Todo App created in Flask Restful

# how to setup code

#INSTALLING REQUIREMENTS
# create a virtual environment and activate it
# install requirements.txt using the command
#  pip install -r requirements.txt
# once the requirements are installed connect to the database

#CONNECTING TO THE DATABASE
#goto the .env file and replace your database credentials with the current ones
#demo
# URL={db_type}://{username}:{password}{host}:{port}/{db_name}

#MIGRATIONS
#once connected to the database, run the command for migrations in console
#command: "python manage.py db init" and then "python manage.py db migrate"
#tables should be created in the db
# actually, I got an error on the second one, and tried this:
(pyhton manage.py db migrate => error)
flask db stamp head
flask db migrate
flask db upgrade
and ... it's good!

#RUN APPLICATION
# to start the application, type command: "run flask"

# User Creation 
POST {{URL}}/user/
body : {'email': 'Abdullahfaiz17@gmail.com', 'password': 12345678,
'username': 'abdullah'}

# Use Basic Auth with email and Password for Todo APIs

POST, PUT, GET, Delete {{URL}}/todo/

Body : 
{
    "note": "This is my first note"
}

# The response is encrypted using Fernet Key and a print statement is added 
# for the key to decrypt the response using the key