# Social Media app

This is a simple REST API based social network in Django
where Users can sign up and create text posts, as well as view, like, and unlike other Users’ posts.

## Features

- on signup, validate email formatting and only allow signups with valid emails
- once signed up, enrich the User with geolocation data of the IP that the
signup originated from
- based on geolocation of the IP, check if the signup date coincides with a
holiday in the User’s country, and save that info

## Runnning app

This app has a Makefile where frequntly run commands have been written. Below are the commands which can be run on terminal to execute some actions.

- make run: This command starts the app on port 8005 (I set this port as default). You can open the make file and select set a port of your choice.

- make superuser: This command allows you create a superuser from the terminal using `valid email address` and password

- migration: I created this command to help me quickly makemigrations and auto generates migration files containing changes that need to be applied to the database

- migrate: This command makes the actual modifications to your database, based on the migration files

- test: This command analyzes an application program interface (API) to verify it fulfills its expected functionality, security, performance and reliability

## Other Features

- APIDOCs is used for API documentation and schema generation. visit `localhost:8005/api/schema/` and `localhost:8005/api/docs/` go generate schema and docs
- Circle-ci is used to configured to run the continous integration pipelines
- black is used for code formatting
- flake8 is used for code linting and to identify and flag possible syntax errors, possible bugs, and stylistic errors
- `https://www.abstractapi.com/` is used for email validation, user's geoinfo and holidays extraction

PS: The `API_KEYS` use in this project is not in this repository. `https://www.abstractapi.com/` offers free api for email validation, geodata extraction and holidays.
