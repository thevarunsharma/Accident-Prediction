# Accident-Prediction
Accident prediction using Naive Bayes

## Components of the project
- *main.py* : main python script to start the flask application (server)
- *naive_bayes.py* : python script including import classes which contain implementation of Naive-Bayesian Model
- *accident-datasets/* : directory containing raw, sorted datasets obtained from data.gov.in
- *cleaning.ipynb* : jupyter-notebook containing code and workflow done for cleaning and organising the datasets
- *cleaned/* : directory containing pickled files containing useful information obtained from datasets
- *test.ipynb* : jupyter-notebook containing code workflow for implementing and testing Naive-Bayesian Model
- *templates/* : directory containing Jinja templates to be rendered by flask

## Requirements
- Find in `requirements.txt`

## Usage
- navigate to the current directory first
- run on terminal as:
```
$ gunicorn Accident_Prediction:app
```
- server running at http://localhost:8000 or http://127.0.0.1:8000

