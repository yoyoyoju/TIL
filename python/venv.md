# Virtual Environment

How to use virtual environment.

#### list pythons

    $ which -a python python3

#### create virtual env

    $ python3 -m venv /path/to/new/virtual/environment

for example,
`$ python3 -m venv ./venv` to create in `./venv`.
Or you can specify the python version by using the full path:
`$ /usr/bin/python3 -m venv ./venv`


#### activate and deactivate

    $ source ./venv/bin/activate
    $ deactivate


#### gitignore file

Here is an example of `.gitignore` file:

    # Virtualenv
    # source from:
    # http://iamzed.com/2009/05/07/a-primer-on-virtualenv/
    .Python
    [Bb]in
    [Ii]nclude
    [Ll]ib
    [Ll]ib64
    [Ll]ocal
    [Ss]cripts
    pyvenv.cfg
    .venv
    pip-selfcheck.json




