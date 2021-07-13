CovidVaccinationSentiment
==============================

![Logo](https://github.com/Madhour/CovaxAnalytica/blob/main/docs/logo/CovaxAnalytica_darkmode.png?raw=true)

Data and sentiment analysis  on vaccine-acceptance by regions
---


Project Organization
------------


    ├── data               
    │   ├── external       <- exeternal data
    │   ├── interim        <- modified dataset
    │   ├── processed      <- final dataset used for analysis
    │   └── raw            <- original dataset
    │
    ├── docs               <- presentation, documents used for reports etc.
    │
    ├── models             <- Trained Doc2Vec model, TF-IDF Vectors
    │
    ├── notebooks          <- Jupyter notebooks (Creators initials and enumerated)
    │
    ├── reports            
    │   └── figures        <- Interactive HTML figures from the analysis
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    │
    ├── src                
    │   ├── models         <- Scripts to train models
            └── train_model.py

Project structure is an adaption of [Cookiecutter data science template](https://drivendata.github.io/cookiecutter-data-science/).

--------


## Datasets:
- [All COVID-19 Vaccines Tweets](https://www.kaggle.com/gpreda/all-covid19-vaccines-tweets)
- [COVID-19 World Vaccination Progress](https://www.kaggle.com/gpreda/covid-world-vaccination-progress)
- [Coronavirus (COVID-19) Geo-Tagged Tweets Dataset](https://ieee-dataport.org/open-access/coronavirus-covid-19-geo-tagged-tweets-dataset#files)

Unfortunately the Twitter Guidelines do not allow the upload of tweets. Tweet IDs can be provided. To build the dataset, follow the steps [here](https://github.com/DocNow/hydrator) to hydrate the IDs.

## How to analyze vaccine tweets:
1. Hydrate the tweet IDs in ```/data/raw/tweet_ids.csv/``` and store the resulting jsonl file as "vaccine_tweets_hydrated.jsonl" in ```/data/raw/```
2. Run Notebooks 2 - 6 in ```/notebooks/```
 - Note: you may have to install requirements (```pip install requirements.txt```)

## How to analyze overall COVID-19 tweets:
1. Hydrate ```Corona_Combined_Nov2020-June2021.csv``` and store as "Hydrated_Tweets.jsonl" in ```/data/raw```
2. Run Notebook 1 and 7 - 13 in ```/notebooks/```
 - Note: you may have to install requirements (```pip install requirements.txt```)
---
# Report

Read the report [here](/reports/CovaxAnalytica_project_report.pdf)!


