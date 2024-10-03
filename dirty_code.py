from zenml import pipeline, step
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score  ,  f1_score
from typing import Tuple
import random
from scipy.sparse import csr_matrix







def load_data():
    url = 'https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv'
    df = pd.read_csv(url)
    return df

# Step 2: Split data into train and test sets

def split_data(df):
    X_train, X_test, y_train, y_test = train_test_split(
        df['Tweet Text'], df['Sentiment'], test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test

# Step 3: Preprocess and vectorize the text data

def preprocess_text(X_train, X_test) :
    vectorizer = CountVectorizer(stop_words='english', max_features=1000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    return vectorizer, X_train_vec, X_test_vec


def train_model(X_train_vec, y_train):
    model = LogisticRegression()
    model.fit(X_train_vec, y_train)
    return model

# Step 5: Evaluate the model

def evaluate_model(model, X_test_vec, y_test) :
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    print(f"Model Accuracy: {accuracy:.2f}")
    return   f1

#
df = load_data()
X_train, X_test, y_train, y_test = split_data(df)
vectorizer, X_train_vec, X_test_vec = preprocess_text(X_train, X_test)
model = train_model(X_train_vec, y_train)
result  = evaluate_model(model, X_test_vec, y_test)
print(result)



