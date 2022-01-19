
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

## Dashboard
The dashboard has been conceptualized as a flask app that can be used by future app developers. They will be able to input data about their potential app that falls into the category of our features. The flask app will then run whether or not the potential Google Play app will be successful or not according to the set arbitrary parameters.
=======

# Final Presentation Outline

## Google Slides Outline

A breakdown of the presentation components and overall skeleton of the presentation was created using Google Slides. 

https://docs.google.com/presentation/d/1CzfQGNICr494rHfeoBJDLGvN3tXc-nueh5KBQIHy9Y0/edit?usp=sharing

## Visualizations

Tableau was used to create visualization, and will be used to create interactive dashboards displaying data used to support findings of this project. Dashboards were created to display data on different features and results including installs, ratings, categories, and successful apps features.

https://public.tableau.com/views/Google_App_Store_Final/SuccessfulApps?:language=en-US&:display_count=n&:origin=viz_share_link

## Dashboard Conceptualization

A storyboard was created using Google Slides to outline the basic features of our dashboard and the elements it will contain.

https://docs.google.com/presentation/d/1EhOnHk-wfv1HrGhrd_nG5N0M-_3SBkQa_MmpDVsHwQg/edit?usp=sharing
=======
# Machine-_Learning_Dashboard_Capstone_2021
## Rutgers Data Bootcamp Final Project

## Data Preprocessing

1. Imported data from MongoDB Online database
2. Set the index to be the 'App Name'.
3. Dropped the unnamed column, and _id column.
4. Explored the data to find the median of both the 'Rating' column and Maximum Installs column.
5. Created a 'Good_App' column based on groups classification of a good app. (Above median Rating, above 250 rating count, above median Maximum Installs).
6. Used pd.to_datetime to changed the Released date column.
7. Extracted the month number from the updated Released date column.
8. Encoded the 'Category' column for use.
9. Dropped the 'Released' column and 'Size (Mb)' column.

## Feature Selection

### Included:
- Price
- Ad Supported
- In App Purchases
- Month_Num (Released Month)
- Encoded Category Columns


### Not Included:
- Good_App column not included as this is the result we are looking to predict/test for.
- Rating
- Rating Count
- Maximum Installs

- Rating, Rating Count, and Maximum Installs were not included in the features because they were used to create
the Good_App column and any machine learning selected would find this relationship and would result in a perfect match
for the data no matter what.

## Training and Testings Sets

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

- X values for the data training were all the Features that were selected to be included above.

- y values were simply the values from the Good_App column.

## Model Choice

- Ran through 4 different machine learning models before settling on DecisionTreeClassifier. Also performed RandomForestClassifier,
Random UnderSampling, and Boosting. However, none of these models performed significantly better than the DecisionTree Classifier to merit
switching to them. The final accuracy score of the DecisionTreeClassifier being 0.7993422068496958.

![Confusion Matrix](https://github.com/Alyssa-Ann/Machine_Learning_Dashboard_Capstone_2021/blob/Machine_Learn/Images/DecisionTreeClassifier_ConfusionMatrix.png)
 
- It is important to mention that the Random Forest did give us the option to see the importance of features to the model based on percentage. At first glance 'In App
Purchases' seem to do the heavy lifting followed by 'Month Num' and 'Ad Supported'. Next, 'Price' is included in the list and then the entire model is finished off with all
the categories contributing minuscule amounts.

![Feature_Importance_List](https://github.com/Alyssa-Ann/Machine_Learning_Dashboard_Capstone_2021/blob/Machine_Learn/Images/Feature_Importance_List.png)

