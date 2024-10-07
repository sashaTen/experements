from  expr   import   load_data
## counts number  of the rows   in  df  and  if  >1000 retrains 

def check_number_samples(df):
    if  df.shape[0]> 1000:
        print('more than 1000')
        return    
    else :
        print('not   enough samples  for  retrain ')
        return 
    







