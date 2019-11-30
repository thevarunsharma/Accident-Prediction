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
- following Python-3 libraries have been used: Pandas, pickle, Flask, Jinja

## Usage
- run on terminal as:
```
$ python3 main.py
```
- server running at http://localhost:5000 or http://127.0.0.1:5000

