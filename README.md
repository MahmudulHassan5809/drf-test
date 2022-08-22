# Project Description

## Project Clone

 1. git clone <https://github.com/MahmudulHassan5809/drf-test>
 2. git checkout develop

## Project Run Using Virtual Env

    1. create virtual env using this command-> python3 -m venv ./venv
    2. activate virtual env
     1.venv\Scripts\activate (windows)
     2.source venv/bin/activate (Linux)
    3. Install all the requirements using this commands -> pip install -r requirements.txt
    4. Create a .env file copy all the ENV variable from .env.example and replace by your values.
       For testing purpose i am not putting .env file in gitignore.
    5. cd src
    6. export $(xargs <../.env)
    7. Run python manage.py runserver 0.0.0.0:8000
    8. project will run in http://0.0.0.0:8000
    9. To test run python manage.py test

## Project Run Using Docker

    1. install Docker and docker compose
    2. check .env file set with all the necessary variables (For testing purpose i am not putting .env file in gitignore.)
    3. run docker-compose up --build --remove-orphans
    4. project will run in http://0.0.0.0:8000
    5. in separate terminal run docker-compose exec app bash (add user to docker group or run as sudo)
    6. in the docker shell run cd src && ./manage.py test

## Api Documentation (swagger)

    http://0.0.0.0:8000/swagger/

## Decode Api

    POST REQUEST
    ENDPOINT  : http://0.0.0.0:8000/api/v1.0/decode/public/decode/
    PAYLOAD   :
    {
            "request_id": "A32W4ER2341",
            "account_name": "TXIuIEFCQw==",
            "amount": "aSN2QHZYeExjRE0h"
    }

    Response  :
    {
        "success": true,
        "message": "Status OK",
        "data": {
            "request_id": "A32W4ER2341",
            "account_name": "Mr. ABC",
            "amount": 1681
        }
    }
