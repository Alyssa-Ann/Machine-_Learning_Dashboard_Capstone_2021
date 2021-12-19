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

The model was built with Jupyter Notebook with Pandas for data cleaning and wrangling, Matplotlib for model visualization with Jupyter Notebook, and SciKit Learn for Machine Learning. The csv file was pushed through a MongoDB database and an S3 AWS database to determine which would be more functional for this project. An app will be created in the future that will be run through flask.   

## Data Exploration
This analysis will be composed of two dataframes. The first dataframe will be our proprietary algorithm and include the rating, rating count, maximum installs, and a new column called success. The success column will be true or 1 if the app is above the median rating and maximum installs as well as above 250 rating count. The second dataframe will include features of an app. Category, price, size, release date, content rating, ads supported, and in-app-purchases are all features that will be analyzed in order to determine what drives success in apps. the original Kaggle file and newly cleaned csv file are robust, leading to data storage through MongoDB and S3 AWS. Both databases have been run through the machine learning model to showcase successful intgration.  

## Machine Learning Model 
This analysis lends itself to a supervised machine learning model. To run the machine learning model, a random sampling of about 20000 apps will be used to analyze our data. For this first segment a DecisionTreeClassifier and a RandomForestClassifier were run, but both got similar results of about 79% for the current question of whether an app was successful or not.  

