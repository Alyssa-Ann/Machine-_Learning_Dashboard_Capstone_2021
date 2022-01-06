# Machine-_Learning_Dashboard_Capstone_2021
Rutgers Data Bootcamp Final Project

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
