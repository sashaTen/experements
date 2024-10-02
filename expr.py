import    pandas as  pd 
url = 'https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv'
def load_data(url):
    
    df = pd.read_csv(url)
    return df



df =    load_data(url)
print(df.head())



