import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

#Using the get_coin_market_chart_by_id(id, vs_currency, days). id is the name of the coin you want, vs_currency is the currency you want the price in, and days is how many days back from today you want.
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

#get price data
bitcoin_price_data = bitcoin_data['prices']
bitcoin_price_data[0:5]

#convert the timestamp to datetime and save it as a column called Date
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

#find the min, max, open, and close for the candlesticks.
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

#create Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()