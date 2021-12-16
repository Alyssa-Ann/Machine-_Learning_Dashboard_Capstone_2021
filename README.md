# Google Play App Analysis 

## Topic Selection
Google Play  is Android's official store for app purchases including games, music, educational tools, communications, and travel. A publicly accessible dataset with information on current app sales has been used to make predictions and analyze what attributes of an app can drive user installs. In order to make our predictions more comprehensive, we have also included user ratings and the designation of "Editor's Choice".  We are conducting this analysis so it can give developers insight to help make future successful apps. In this model, success is defined by a proprietary algorithm composed of data taken from ratings and installs.

## Research Questions
1. How does one define an app as successful?
2. Do  certain categories of apps see more installs or higher ratings?
3. If a developer were to create a new app, what features should this app have to make it successful? 

## Data Source
The initial dataset was sourced from Kaggle. See https://www.kaggle.com/gauthamp10/google-playstore-apps for the original csv file. This data source has been cleaned of any superfluous columns. 

## Communication Protocols
The team will be communicating primarily over Slack and Google Docs. The files and databases will be shared on Github. 

## Technology
1. Jupyter Notebook
2. Pandas 
3. Numpy
4. Sklearn
5. Plotly
6. Matplotlib
7. Flask

## Databases
This analysis will be composed of two databases. The first database will be our proprietary algorithm and include the rating, rating count, maximum installs, and a new column called success. The success column will be true or 0 if the app is above the median rating and maximum installs as well as above 250 rating count. 

The second database will include features of an app. Category, price, size, release date, content rating, ads supported, in-app-purchases, and editor's choice are all features that will be analyzed in order to determine what drives success in apps. 

## Machine Learning Model 
This analysis lends itself to a supervised machine learning model. To run the machine learning model, a random sampling of about 20000 apps will be used to analyze our data.
