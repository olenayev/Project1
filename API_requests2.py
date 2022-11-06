import requests
import pandas as pd
import json

#Using ExchangeRate-API we will extract currency exchange rate data

url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=G146fPyLUGpNFGm1qeHL91PSHmmtvfl7" 
data  = requests.get(url).text 
#Save as DataFrame
df = pd.DataFrame(json.loads(data)).reset_index()
df = df.set_index('index')
# Drop unnescessary columns
df = df.drop(['success', 'timestamp','base','date'], axis=1)
# Save the Dataframe
df.to_csv("exchange_rates_1.csv", sep='\t')