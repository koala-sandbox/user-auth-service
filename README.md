# Flask App

## Requirements

Python 3.10.0

Project is ready to work with either "pipenv" (Pipfile) or "pip" (requirements.txt) - choose whatever suites you best. 

Please note, Github Actions flows rely on requirements.txt so in case you go with "pipenv" please make sure to run the command below after every `Pipfile` change.

```
pipenv run pip freeze > requirements.txt
```

## Install and Run

```
pipenv install
pipenv run python run.py
```

Application will be available at:

	http://localhost:5000

## Unit tests

Run:

```
pipenv run python -m unittest tests/test_example.py
```

## App Configuration
All configuration is in: `configuration.py`
