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

Covid 19 had a massive impact on the whole planet. In numbers there occur nearly 4 Millions deaths, 126 Million lost Jobs and a GDP Development of -3.5 percent in 2020. Families lost their father, their mother or their children. Many employees can not find a way to feed their family anymore. And like the people are, the world wide economy is at it´s weakest part of the decade. The Dataset includes over 110000 Tweets which has been parsed with a high number of keywords, which were enhanced continuously during the process. The Dataset gives Information about the period from 1st of November 2020 till 12th of June 2021. Also important to mention is that the dataset included the Sentiment of the tweets, which gives an indicator about the mood of every single tweet from -1 for very negative to 1 for very positive.

## 1.1 Placement of Tweets

![tweets worldwide](/docs/img/tweets_worldwide.png)

We can see the overall coverage of tweets in the dataset worldwide. We can observe that the Dataset mostly includes tweets from the United States. 44824 Tweets of a the total 110000 were parsed there. After that the United Kingdom includes 21110 Tweets with a focus on the south part of England. But also Wales, Scottland and Ireland were included. Furthermore Canada provides 15610 Tweets, India 7687 and Australia 1867. Germany is the top 10 Country for amount of tweets with between 800 and 900 Tweets. What also can be observed is that some countries like Russia and China for example are not featured that much in the Dataset because of the language barrier and the fact that they provide their own social networks apart from Twitter and so on.

## 1.2 Average Sentiment and Tweet Amount

We can see that the Dataset covers nearly the whole world. Overall we see a very neutral Sentiment. We need to mention here that the dataset covers a period over 7 months, where many positive and negative Covid-19 news occured in the media. Nevertheless we encounter a slightly negative Sentiment in parts of Africa. This can be classified as less meaningful because the dataset does not include many Tweets from Ghana, which means that just one to five tweets have to represent the whole country over a period of 7 month which is not possible. If you compare the amount of tweets with the population of the country a negative sentiment can not be taken as a result. Also more positive Sentiments. For example Kazakhstan and Mongolia have a slightly positive Sentiment with 0.38 in Kazakhstan and 0.5 in Mongolia. The Dataset features 3 Tweets from Kazakhstan and 4 Tweets from Mongolia.
![overall development](/docs/img/sentiment.gif)
![sentiment overall](/docs/img/sentiment_overall.png)
We see that the average amount of tweets per day is 500. Also we occur a always neutral to positive sentiment around 0.1. Most people tweeted in January of 2021 because of new years resolutions and hopes that Covid-19 will not also ruin the coming year.
![sentiment per month](/docs/img/sentiment_per_month.png)
![amount of tweets](/docs/img/amount_tweets.png)

## 1.3 Focussing on detailed Countries

In India we can find a very unstatic Sentiment from November 2020 to March 2021 which can be justified with the low amount of tweets in that period of time. In March we can see a data growth attributable to the attachment of new parsing parameters which also cover more indian tweets. In April India celebrated the biggest festival of the world. It is called Kumbh Mela, the festival of hinduism, and had 10 Million attendants, a 1800% increase of Covid Cases in the week that followed the festival and more than 168000 new cases just on 12th of April. Which resulted in an increase of Tweets and a slightly more negative Sentiment.
![sentiment india](/docs/img/sentiment_india.png)

In the United States we can see a peak on 7th of May, which can be drawn back to the national tourism day, where many vaccinations were offered in the usa to enable tourism again on a date in the sooner future. According to that the Sentiment was very positive on that specific day. 
![sentiment us](/docs/img/sentiment_us.png)

The United Kingdom offers two peaks. The first peak can be seen on 5th of November with a slightly more neutral sentiment and a high amount of tweets. On this day Prime Minister Boris Johnson announced the second Lockdown in England. The second peak on the 31st of December around new years features a high sentiment  with nearly 0.3 overall and a slightly higher amount of tweets. People around the United Kingdom praised the end of the pandemic in the following year and thanked all helping hands including medical and transport sector.
![sentiment uk](/docs/img/sentiment_uk.png)
![sentiment germany](/docs/img/sentiment_germany.png)

## 1.4 Correlation between Sentiment and vaccination status

In the Correlation Graph we can not define a correlation between the overall Sentiment andthe Amount of Vaccinations worldwide. Due to the fact, that the Sentiment of Tweets can be influenced by the amount of Vaccinations, like in the United States on 7th of May, the Sentiment is influenced by way more information than the Vaccination Status.
![sentiment vaccination](/docs/img/vaccine_sentiment.png)

## 1.5 Used Technologies

For the Sentiment Scatter Plot we used the Savgol Filter to smooth the curve in the plot to make it more visible. For that in realtion to the Plot the length of the filter window and the order of the polynomial were customized to insure the best visibility.
For the Visualization of the data we used Plotly because it features many build in heatmaps, animated plots, zoom features and it is adjustable in the Output of the Code.
Furthermore we used Jupyter Notebooks as development environment, such as Hydrator to hydrate the Dataset of ID´s to full text and geolocation.

## 1.6 Reflection on Findings

On one side the findings of this Dataset are very interesting and decisive but on the other side many people worldwide could not participate in this dataset due to language barriers and the fact, that you need a internet connection and a device to join the Twitter Community. Furthermore do countries like China and Russia have their own social networks. If we could start over the project with a little bit more time we would search for a way of including cyrillic and asian font and also other social networks which are used in the affected countries. 

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
