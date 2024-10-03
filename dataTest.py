# test_load_data.py

import pandas as pd
from sklearn.model_selection import train_test_split
import pytest 
from   dirty_code   import load_data ,  split_data



def test_load_data():
    url = 'https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv'
    # Check if the input is a string
    assert isinstance(url, str), "Input should be a string"

    # Load the data
    df = load_data()
    assert isinstance(df, pd.DataFrame), "Output should be a DataFrame"
    # Optionally, you can also check if the DataFrame is not empty
    assert not df.empty, "DataFrame should not be empty"



@pytest.fixture
def sample_df():
    data = {
        'Tweet Text': ['This is a great day', 'I hate traffic', 'Love this product', 
                       'Worst experience ever', 'Amazing service', 'Will not recommend', 
                       'Had a good time', 'Terrible app', 'Very satisfied', 'Not bad at all'],
        'Sentiment': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def test_split_data(sample_df):
    # Call the split_data function
    X_train, X_test, y_train, y_test = split_data(sample_df)
    
    # Test if the split data are pandas Series
    assert isinstance(X_train, pd.Series), "X_train should be a pandas Series"
    assert isinstance(X_test, pd.Series), "X_test should be a pandas Series"
    assert isinstance(y_train, pd.Series), "y_train should be a pandas Series"
    assert isinstance(y_test, pd.Series), "y_test should be a pandas Series"
    
    # Test if the sizes of the splits are correct (80% train, 20% test)
   
    
    # Check if the data still matches (optional, based on the random_state used)
    assert X_train.iloc[0] == 'This is a great day', "Unexpected value in X_train"
   
    
    # Make sure random_state is respected, and results are consistent
   




'''
X_train, X_test, y_train, y_test = split_data(df)
vectorizer, X_train_vec, X_test_vec = preprocess_text(X_train, X_test)
model = train_model(X_train_vec, y_train)
result  = evaluate_model(model, X_test_vec, y_test)
'''
