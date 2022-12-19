# Project: Cars API Authentication & Production Server

## Author: ASAD HIJAWI

##Links and Resources

[Pull Request](https://github.com/asadhijj/drf-auth/pull/1)

##Setup

    Clone the Repo
    Run the server
    http://127.0.0.1:8000/api/v1/cars/ To see the cars API

## .env requirements (where applicable)

## How to initialize/run your application (where applicable)

    To run the server
    python manage.py runserver

## How to use your library (where applicable)

## Tests

Testing Using Postman:

    Send a get request to http://127.0.0.1:8000/api/v1/cars/ to see the data
    Try sending a post request to http://127.0.0.1:8000/api/v1/cars/ without authentication will fail.
    Send a post request to http://127.0.0.1:8000/api/v1/cars/ using the basic authentication with the following:

    {"type": "Toyata", "car_model: "prius2017", "car_fuel":gasoline, "purchaser": 1}
    Username : asad
    Password asadh001
    The data will be added to the API

    To test the tokens send a post request to http://127.0.0.1:8000/api/token/ with the following body: {"username":"asad", "password":"asadh001"}

    The response will contain an access token and a refresh token

    We can use the access token as bearer authentication to post more data to the API.

    The access token will be working for 5 minutes

    To get a new access token after the first one expired, we send a post request to http://127.0.0.1:8000/api/token/refresh/ containing the refresh token in the body.

    The response will be a new access token
