from  expr   import   load_data     ,   zen_sentiment_analysis_pipeline
## counts number  of the rows   in  df  and  if  >1000 retrains 

def check_number_samples(df):
    if  df.shape[0]> 490:
        print('the   autoretrain  is  caused ')
        return    
    else :
        print('not   enough samples  for  retrain ' ,    df.shape[0])
        return 
    

df   =   load_data()
check_number_samples(df)






