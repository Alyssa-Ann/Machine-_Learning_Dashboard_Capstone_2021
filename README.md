# Machine-_Learning_Dashboard_Capstone_2021
Rutgers Data Bootcamp Final Project

## Data Preprocessing

. Imported data from MongoDB Online database
. Set the index to be the 'App Name'.
. Dropped the unnamed column, and _id column.
. Explored the data to find the median of both the 'Rating' column and Maximum Installs column.
. Created a 'Good_App' column based on groups classification of a good app. (Above median Rating, above 250 rating count, above median Maximum Installs).
. Used pd.to_datetime to changed the Released date column.
. Extracted the month number from the updated Released date column.
. Encoded the 'Category' column for use.
. Dropped the 'Released' column and 'Size (Mb)' column.
