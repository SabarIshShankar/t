import dash
import dash_core_components as dcc 
import das_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np 
import pandas_datareader.data as web
import plotly.graph_objs as go 
from datetime import datetime


app = dash.Dash()

tickers = pd.read_csv('https://raw.githubusercontent.com/kdboller/pythonsp500-plotly-dash/master/tickers.csv')
tickers.set_index('Ticker', inplace = True)
data = pd.read_csv('https://raw.githubusercontent.com/kdboller/pythonsp500-plotly-dash/master/analyzed_portfolio.csv')
options = []

for tic in tickers.index:
	ndict = {}
	ndict ['label'] = tic
	ndict['value'] = tic
	options.append(ndict)

app.layout = html.Div([
	html.H1('Dashboard'),
	dcc.Markdown('''---'''),
	html.H1('Relative returns comparison'),
	html.Div([html.H1('Enter a symbol', style={'paddingRight': '30px'}),
	dcc.Dropdown(
		id='my_ticker_sumbol',
		options = options,
		value = ['SPY'],
		multi = True
	)
	
	], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
	html.Div([html.H3('Enter start / end date:'),
	dcc.DatePickerRange(id='my_data_picker',
	min_date_allowed = datetime(2015,1,1),
	max_date_allowed = datetime.today(),
	start_date = datetime(2018,1,1),
	end_date = datetime.today()
	)], style={'display':'inline-block'}),
])