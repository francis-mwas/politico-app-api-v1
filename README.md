# POLITICO-APP
Politico is an application that enables citizens give their mandate to politicians running for different government offices, while building trust in the process through transparency.

[![Build Status](https://travis-ci.com/francis-mwas/politico-app-api-v1.svg?branch=develop)](https://travis-ci.com/francis-mwas/politico-app-api-v1)
[![Coverage Status](https://coveralls.io/repos/github/francis-mwas/politico-app-api-v1/badge.svg?branch=develop)](https://coveralls.io/github/francis-mwas/politico-app-api-v1?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/784dc521fe654185a9c783847599e41a)](https://www.codacy.com/app/francis-mwas/politico-app-api-v1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=francis-mwas/politico-app-api-v1&amp;utm_campaign=Badge_Grade)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)

#Politico app challenge
Politico is an application that enables citizens give their mandate to politicians running for different government offices, while building trust in the process through transparency.

## How politico app works
- An admin creates a political party
- An admin creates political offices
- Politicians show their interest to run for a particular government office
- Normal users creates an account
- Normal users with an account can login
- Normal users who are qualified to vote, can search for government offices and vote their prffered candidate to represent them.
- Normal users can be able to view their votes and the candidate they have voted for
- Polician user can file a petition against a concluded political office election

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and setup

Clone this repository 
```
https://github.com/francis-mwas/politico-app-api-v1
```

### Create and activate virtual environment

    virtualenv env --python=python3.6

    source env/bin/activate

### Install all the required dependancies

    pip install -r requirements.txt

### Running Politico application
    ```zsh
    $ export FLASK_APP = run.py

    $ export MODE = development

    $ flask run

    ```

    ## Politico App Available Endpoints 

| Method | Endpoint                        | Description                           | Roles           |
| ------ | ------------------------------- | ------------------------------------- | ----------------|
| POST   | /api/v1/admin/parties           | create party                          | Admin           |  
| GET    |/api/v1/admin/parties            | view all parties                      | Admin           |
| DELETE |/api/V1/admin/parties/<{id}>     | delete a specific party               | Admin           |
| PATCH  |/api/V1/admin/parties/<{id}>     | edit specific party                   | Admin           |
| GET    | /api/V1/admin/parties/<{id}>    | get a specific party                  | Admin           |
| POST   |/api/V1/admin/offices            | create office                         | Admin           |
| GET    | /api/V1/admin/ofice/<{id}>      | get a specific office                 | Admin           |
| GET    | /api/V1/admin/offices           | fetch all offices                     |Admin            |
| PATCH  | /api/V1/admin/offices/<{id}>    | update a specific office              | Admin           |
| POST   | /api/V1/auth/signup             | create an account                     |Admin/Users      |       |POST    |/api/V1/auth/signin              | signin                                | Admin/Users     |
|DELETE  |/api/V1/admin/offices/<{id}>     | delete a specific office              | Admin           |



### Testing

    Pytest

    - Testing with coverage

    - pytest --cov=app

### Author

Francis Mwangi