import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

df = pd.read_excel('https://github.com/kdboller/pythonsp500-plotly-dash/blob/master/Sample%20stocks%20acquisition%20dates_costs.xlsx?raw=true')
df.head(10)

df.describe()
df.info()
start_sp = datetime.datetime(2010,1,1)
end_sp = datetime.datetime(2021,1,1)

end_of_last_year = datetime.datetime(2018, 12 ,2)

stocks_start = datetime.datetime(2010,1,1)
stocks_end = datetime.datetime(2021,1,1) 

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
sp500 = pdr.get_data_yahoo('^GSPC',start_sp,end_sp)
sp500.head()


# In[11]:


sp500.tail()


# In[12]:


sp_500_adj_close = sp500[['Adj Close']].reset_index()
sp_500_adj_close.tail()

sp_500_adj_close.tail()

tickers = df['Ticker'].unique()
tickers

def get(tickers, startdate, enddate):
    def data(ticker):
        return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas = map(data, tickers)
    return(pd.concat(datas, keys=tickers, names=['Ticker','Date']))

all_data = get(tickers, stocks_start, stocks_end)

all_data.tail()

all_data.head()

adj_close=all_data[['Adj Close']].reset_index()
adj_close.head()

adj_close.plot()

adj_close['Ticker'].unique()

adj_close_start = adj_close[adj_close['Date']==end_of_last_year]
adj_close.head()

adj_close_latest = adj_close[adj_close['Date']==stocks_end]
adj_close_latest.tail()

merge = pd.merge(df, adj_close_latest, on='Ticker')
merge.head(10)

merge['ticker return'] = merge['Adj Close']/merge['Unit Cost']-1
merge.head()

merged_sp = pd.merge(merge, sp_500_adj_close, left_on='Acquisition Date', right_on='Date')
merged_sp.head()

