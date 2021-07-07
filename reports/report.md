CovidVaccinationSentiment
==============================

![Logo](https://github.com/Madhour/CovaxAnalytica/blob/main/docs/logo/CovaxAnalytica_darkmode.png?raw=true)

---
# Motivation
COVAX is a worldwide initiative aiming at a fair distribution of COVID-19 vaccines, especially in developing countries. It is directed by the global alliance for Vaccines and Immunisation (GAVI) and the world health organisation (WHO).
> "With a fast-moving pandemic, no one is safe, unless everyone is safe."

Under this slogan, the initiative is striving to distribute WHO approved Vaccines, namely: Oxford-AstraZeneca, Pfizer-BioNTech, Moderna, Sinopharm, Sinovac and Johnson & Johnson. 
However, when it comes to vaccines, there are vastly polarising opinions, ranging from absolute vaccine-acceptance all the way to FUD and conspiracy theories.

Identifying triggers of negative sentiment and vaccine-hesitancy might be the first step towards a united society, pulling together against COVID-19. CovaxAnalytica, a student project by Madhour and Bach, aims to analyze the overall sentiment towards each vaccine, which allows for an in-depth analysis of opinions and their causes.

---
# Part 1: Overall Covid-19

## 1.1 Placement of Tweets

![tweets worldwide](/docs/img/tweets_worldwide.png)

## 1.2 Average Sentiment and Tweet Amount

<p align="center">
  ![overall development](/docs/img/sentiment.gif)
</p>

![sentiment overall](/docs/img/sentiment_overall.png)
![sentiment per month](/docs/img/sentiment_per_month.png)
![amount of tweets](/docs/img/amount_tweets.png)

## 1.3 Focussing on detailed Countries

![sentiment india](/docs/img/sentiment_india.png)
![sentiment germany](/docs/img/sentiment_germany.png)
![sentiment us](/docs/img/sentiment_us.png)
![sentiment uk](/docs/img/sentiment_uk.png)

## 1.4 Correlation between Sentiment and vaccination status

![sentiment vaccination](/docs/img/vaccine_sentiment.png)

# Part 2: Vaccines

As of July 2021, more than 3 billion vaccine doses have been administered. 24% of the world population has received at least one dose, the goal however is 70% receiving 2 doses. That means the fight against the virus is far from over and is getting stalled by major setbacks. Fake news, news about side-effects and new variants all lead to an increase in vaccine-hesitancy or an overall negative sentiment. Thus it is of utmost importance to identify causes for the negative sentiment so that these problematic areas can be resolved.

## 2.1 Vaccine Sentiment:
The basis of our vaccine sentiment analysis is a tweet dataset, containing more than 100.000 vaccine-related tweets. Out of the whole dataset, we extracted all tweets about WHO-approved vaccines, as well as russian SputnikV and BharatBiotechs Covaxin. For the sentiment prediction, we opted for the NLTK library in python. The predictions range from -1 for very negative to 1 for very positive.
We smoothed the sentiment through a savitzky-golay filter to be able to identify peaks better. The date of the peaks was then used to identify notable trends that could have potentially lead to that sentiment. The trends were obtained through PyTrends, an unofficial api for the Google Trends service.

The overall mean sentiment of each vaccine is neutral with a positive tendency. Out of all analyzed vaccines, SputnikV has the lowest and Johnson & Johnson the highest sentiment. But because the tweet volume of these two tweets wasn't particularily high, we are cautious to draw any conclusions. 

![vaccine sentiment](/docs/img/vaccine_sentiment.png)

PfizerBiontech, the first approved COVID-19 vaccine, was the most tweeted about in the beginning of the year. However it got quickly overrun by Moderna and Covaxin. The tweet volume is of importance because the more a vaccine is talked about the less the risk of a few opionion leaders influencing the absolute sentiment.

![Tweet amount](/docs/img/tweet_amount.gif)

Most positive tweets tend to talk about a successful vaccination experience or are longing for positive things like traveling again. Negative tweets tend to be about conspiracy theories or bad vaccine experiences (side-effects, deaths, etc.). Neutral tweets are mostly articles about cases and available doses.


### PfizerBioNTech
As with all Vaccines predominantly used in the U.S., there is an observable dip in Vaccination on valentines day and memorial day. Other than that, it seems like more people get vaccinated on weekends than during the week. 

![pfizer sentiment](/docs/img/pfizerbiontech_sentiment.png)

The first negative peak in sentiment seems to be influenced by news about pfizer biontech causing 23 deaths in norway. The news had a strong impact overseas and caused an increase in vaccine-hesitancy, as observable in the following tweet:
- "U MAY die if u become covid positive. But #PfizerBioNTech shot will DEFINITELY kill you. Stuck between devil and sea." (Index No. 29798 in geo_vaccine_tweets_with_sentiment.csv)

![world sentiment](/docs/img/world_sentiment.png)

---
### Sinovac/Sinopharm
Sinovac and Sinopharm have a notable peak in positive sentiment in the beginning of june. This was most likely a reaction to the fact that the vaccine got approved by the WHO. 

![sinovacsinopharm sentiment](/docs/img/sino_sentiment.png)

---
### AstraZeneca
When the news broke that AstraZeneca causes thrombosis, germany stopped vaccination briefly. These two events caused a notable shift in sentiment during march 2021. What is also notable is that after the initial negative sentiment, the opinions shifted from largely negative to suddenly positive. This might be the work of targeted awareness raising that this is a rare condition. 

![astrazeneca sentiment](/docs/img/astrazeneca_sentiment.png)

---
### Johnson & Johnson
On 12. April, Johnson & Johnson (JandJ) experienced a sudden shift from very positive sentiment to neutral with negative tendency. That is roughly the time during which the news broke that johnson and johnson causes blood clots. Trending search terms were "johnson and johnson vaccine blood clot symptoms" which hints that people who are vaccinated feel afraid. JandJ was largely used in the U.S. which during that time was vaccinating its population at full speed. 

![JandJ sentiment](/docs/img/jandj_sentiment.png)

A more in depth look reveals that over the course of 4 days the amount of positive tweets fell and neutral/negative tweets gained traction.

![JandJ sentiment broken down](/docs/img/jandj_sentiment_broken_down.png)

---
## 2.2 Text Analysis:

As of june/july 2021, the delta variant of the COVID-19 virus is posing serious threats to progress made in the fight against the virus. The discourse about the delta variant shows that Covaxin, an indian vaccine, is the most mentioned. This doesn't come as a surprise as the delta variant appeared first in India, which means that this region is likely the most affected.

![deltavariant](/docs/img/deltavariant.png)

Apart from this, we conducted several iterations of word and document vectorization. Our aim was to cluster tweets depending on their content but because tweets are short in text, no clear cluster could be identified. To achieve this, further data engineering and hyperparameter tuning is needed. 
What we found out with our attempt however, still remains relevant: a Word2Vec model trained on the whole corpus of 100.000+ tweets yields the following:
- the most similar word to common conspiracy theory terms like "plandemic" is: great reset, bill gates, genocide, drfauci, merck. 

This can be used to identify further sources of false news and conspiracies. 

# 3. Conclusion:

The results appear promising, however we can't make definite conclusions as there are a few limiting factors:
1. The language barrier can't be neglected. Some countries weren't considered as only english tweets were analyzed. 
2. Some contries have their own social media platforms and don't partake in the discourse on twitter.
3. The largest demographic group of twitter users are betwen ages 18 and 29, that means that other age groups aren't represented in the discourse.

Fact checkers are widely needed and remain necessary to reduce misinformation. The way social media is designed is that people stay in their own "bubble" and only consume tweets/news that validate their views and thoughts. This confirmation bias is dangerous as it can lead to extremist views. A mixed and civil discourse would be the most beneficial to unite society as a whole.
