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
