# test_load_data.py

import pandas as pd
import pytest 
from   dirty_code   import load_data



def test_load_data():
    url = 'https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv'
    # Check if the input is a string
    assert isinstance(url, str), "Input should be a string"

    # Load the data
    df = load_data()
    assert isinstance(df, pd.DataFrame), "Output should be a DataFrame"
    # Optionally, you can also check if the DataFrame is not empty
    assert not df.empty, "DataFrame should not be empty"







'''
X_train, X_test, y_train, y_test = split_data(df)
vectorizer, X_train_vec, X_test_vec = preprocess_text(X_train, X_test)
model = train_model(X_train_vec, y_train)
result  = evaluate_model(model, X_test_vec, y_test)
'''
