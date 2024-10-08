from  expr   import   load_data     ,   zen_sentiment_analysis_pipeline
from zenml.client import Client
## counts number  of the rows   in  df  and  if  >1000 retrains 
#  https://raw.githubusercontent.com/sardarosama/Stock-Market-Trend-Prediction-Using-Sentiment-Analysis/refs/heads/main/stock_data.csv
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
check_number_samples(df ,  url)

client = Client()

my_runs_on_current_stack = client.list_pipeline_runs(
    stack_id=client.active_stack_model.id,  # on current stack
    user_id=client.active_user.id,  # ran by you
    sort_by="desc:start_time",  # last 10
    size=10,
)


latest_pipeline_run_id   =    my_runs_on_current_stack[0].id

pipeline_run_id = latest_pipeline_run_id  
pipeline_run = client.get_pipeline_run(pipeline_run_id)

# Fetch the specific step output artifacts, including model and vectorizer
zen_train_model_step = pipeline_run.steps.get('zen_train_model')
model_artifact = zen_train_model_step.outputs['output'].load()

zen_preprocess_text_step = pipeline_run.steps.get('zen_preprocess_text')
vectorizer_artifact = zen_preprocess_text_step.outputs['output_1'].load()
print(model_artifact)
print(vectorizer_artifact)