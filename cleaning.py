import pandas as pd
from path import Path
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pymongo
from pymongo import MongoClient
import pandas as pd
from pandas import DataFrame
from IPython.display import HTML
from bs4 import BeautifulSoup

def clean_data(collection):
    hundred = collection.find().limit(5)
    list_cursor = list(hundred)
    app_data = pd.DataFrame(list_cursor)

    # Set the index to the App Name moving forward
    app_data = app_data.set_index('App Name')

    # Dropped the _id column did not add to the data
    app_data = app_data.drop(["_id"],axis=1)
    app_data = app_data.drop(app_data.columns[0], axis=1)

    return app_data
    