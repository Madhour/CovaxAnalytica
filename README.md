CovidVaccinationSentiment
==============================

![Logo](https://github.com/Madhour/CovaxAnalytica/blob/main/docs/logo/CovaxAnalytica_darkmode.png?raw=true)

Data and sentiment analysis  on vaccine-acceptance by regions
---

## Datasets:
- [All COVID-19 Vaccines Tweets](https://www.kaggle.com/gpreda/all-covid19-vaccines-tweets)
- [COVID-19 World Vaccination Progress](https://www.kaggle.com/gpreda/covid-world-vaccination-progress)


Unfortunately the Twitter Guidelines do not allow the upload of tweets. Tweet IDs can be provided. To build the dataset, follow the steps [here](https://github.com/DocNow/hydrator) to hydrate the IDs.

```
pip3 install -r requirements.txt
```

---
# Report

Read the report [here](/reports/CovaxAnalytica_project_report.pdf)!

<!-- 

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

-->
