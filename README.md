# POLITICO-APP
Politico is an application that enables citizens give their mandate to politicians running for different government offices, while building trust in the process through transparency.

# POLITICO-API-V1
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

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
'''
https://github.com/francis-mwas/POLITICO-API-V1


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

