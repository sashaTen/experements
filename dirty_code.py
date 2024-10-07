from  expr   import   load_data     ,   zen_sentiment_analysis_pipeline
## counts number  of the rows   in  df  and  if  >1000 retrains 
url = 'https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv'
def check_number_samples(df ,  url):
    if  df.shape[0]> 490:
        print('the   autoretrain  is  caused ')
        zen_sentiment_analysis_pipeline(url)
        return    
    else :
        print('not   enough samples  for  retrain ' ,    df.shape[0])
        return 
    

df   =   load_data(url)
#check_number_samples(df ,  url)






