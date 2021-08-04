import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

df = pd.read_excel('https://github.com/kdboller/pythonsp500-plotly-dash/blob/master/Sample%20stocks%20acquisition%20dates_costs.xlsx?raw=true')
df.head(10)

df.describe()

df.info()

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2018,7,20)

end_of_last_year = datetime.datetime(2017, 12,29)

stock_start = datetime.datetime(2010, 1, 1)
stocks_end = datetime.datetime(2018, 7, 13)

from pandas_datareader import data as pdr
import yfinance as yf

from pandas_datareader import data as pdr
yf.pdr_override()
sp500 = pdr.get_data_yahoo('^GSPC', start, end)                        
sp500.head()

sp500.tail()

sp_500_adj_close = sp500[['Adj Close']].reset_index()
sp_500_adj_close.tail()

tickers = df['Ticker'].unique()
print(tickers)
