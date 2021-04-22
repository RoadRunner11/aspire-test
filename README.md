# Aspire Backend Test
- After pulling this code repository, create a venv and install the dependencies using the pip install -r requirements.txt command
- Create your .env and set the correct values for the constants
- Run ./manage.py db init, ./manage.py db migrate, ./manage.py db upgrade to set up the sqlite database
- Run ./manage.py run to initiate the server 
- Start testing the endpoints use http://localhost:5000/api as the base url 
    GET /characters
    GET /characters/{{id}}/quotes
    POST /signup
    POST /login
    POST /characters/{{id}}/favourites
    POST /characters/{{id}}/quotes/{{id}}/favourites
    GET /favourites