# test_load_data.py

import pandas as pd
import pytest 
from   expr   import load_data

url = 'https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv'

def test_load_data():
    # Check if the input is a string
    assert isinstance(url, str), "Input should be a string"

    # Load the data
    df = load_data(url)

    # Check if the output is a DataFrame
    assert isinstance(df, pd.DataFrame), "Output should be a DataFrame"

    # Check if the DataFrame has the 'head' method
    assert hasattr(df, 'head'), "DataFrame should have a 'head' method"

    # Optionally, you can also check if the DataFrame is not empty
    assert not df.empty, "DataFrame should not be empty"