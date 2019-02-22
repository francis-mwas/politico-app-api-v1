# POLITICO-APP
[![Maintainability](https://api.codeclimate.com/v1/badges/f2f881c783706e56e049/maintainability)](https://codeclimate.com/github/francis-mwas/politico-app-api-v1/maintainability)
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

https://github.com/francis-mwas/politico-app-api-v1

Heroku link

https://politico-app-api-v1.herokuapp.com/

API documentation link

https://politicoapiv2.docs.apiary.io/


### Create and activate virtual environment

    in the root directory,open your terminal and create virtual environment by entering the commands below

    virtualenv env --python=python3.6

    source env/bin/activate

### Install all the required dependancies

    pip install -r requirements.txt

### Running Politico application
    
    $ export FLASK_APP=run.py

    $ export MODE=development

    $ python manage.py

    $ flask run

    

## Politico App Available Endpoints 
<table>
    <tr>
        <td>Method</td>
        <td>Endpoint</td>
        <td>Description</td>
        <td>Roles</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/api/v2/admin/parties </td>
        <td>create party </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>GET</td>
        <td>/api/v2/admin/parties </td>
        <td>Fetch all parties </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>DELETE</td>
        <td>/api/v2/admin/parties/<{id}> </td>
        <td>delete a specific party </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>PATCH</td>
        <td>/api/v2/admin/parties/<{id}></td>
        <td>edit a specific party </td>
        <td>Admin</td>
    </tr>
     <tr>
     <td>GET</td>
        <td>/api/v2/admin/parties/<{id}> </td>
        <td>get a specific party </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>POST</td>
        <td>/api/v2/admin/offices </td>
        <td>create office </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>GET</td>
        <td>/api/v2/admin/offices/<{id}>  </td>
        <td> get a specific office </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>GET</td>
        <td>/api/v2/admin/offices  </td>
        <td>fetch all offices </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>PATCH</td>
        <td>/api/v2/admin/offices/<{id}> </td>
        <td> update a specific office </td>
        <td>Admin</td>
    </tr>
    <tr>
     <td>POST</td>
        <td>/api/V2/auth/signup </td>
        <td> create an account </td>
        <td>Admin /Users</td>
    </tr>
     <tr>
     <td>POST</td>
        <td>/api/v2/auth/signin  </td>
        <td>signin</td>
        <td>Admin /Users</td>
    </tr>
    <tr>
     <td>POST</td>
        <td>/api/v2/users/votes  </td>
        <td>Vote for a candidate</td>
        <td>Admin /Users</td>
    </tr>
    <tr>
    <tr>
     <td>GET</td>
        <td>/api/v2/users/candidates  </td>
        <td>View candidates</td>
        <td>Admin /Users</td>
    </tr>
    <td>GET</td>
        <td>/api/v2/users/offices/1 </td>
        <td>View office results</td>
        <td>Admin /Users</td>
    </tr>
    <tr>
    <td>GET</td>
        <td>/api/v2/admin/users </td>
        <td>View all users</td>
        <td>Admin</td>
    </tr>
     <tr>
    <td>GET</td>
        <td>/api/v2/admin/office/1/register </td>
        <td>Register candidates</td>
        <td>Admin</td>
    </tr>
    <tr>
    <td>GET</td>
        <td>/api/v2/users/office/1/3/result</td>
        <td>View office results for specific office and specific candidate</td>
        <td>Admin /Users</td>
    </tr>
     <td>DELETE</td>
        <td>/api/v2/admin/offices/<{id}> </td>
        <td>delete a specific office</td>
        <td>Admin</td>
    </tr>
</table>

### Testing

    Pytest

    - Testing with coverage

    - pytest --cov=app

### Author

Francis Mwangi
