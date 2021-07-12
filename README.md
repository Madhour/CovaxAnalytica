CovidVaccinationSentiment
==============================

![Logo](https://github.com/Madhour/CovaxAnalytica/blob/main/docs/logo/CovaxAnalytica_darkmode.png?raw=true)

Data and sentiment analysis  on vaccine-acceptance by regions
---
Unfortunately the Twitter Guidelines do not allow us to upload or provide hydrated Twitter Data. Therefore there is a Dataset provided including the Tweet ID´s in the Repository in the Data Folder. These ID´s need to be hydrated using the Hydrator Tool ![Hydrator](https://github.com/DocNow/hydrator).

```
pip3 install -r requirements.txt
```

---
# Report

Read the report [here](/reports/report.md)!

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
