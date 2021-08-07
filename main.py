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
	dcc.DatePickerRange(id='my_date_picker',
	min_date_allowed = datetime(2015,1,1),
	max_date_allowed = datetime.today(),
	start_date = datetime(2018,1,1),
	end_date = datetime.today()
	)], style={'display':'inline-block'}),
	html.Div([
		html.button(id='submit-button',
		n_clicks = 0,
		children = 'Submit',
		style = {'fontSize':24, 'marginLeft':'30px'})
	], style={'display':'inline-block'}), 

	dcc.Graph(id='my_graph',
	figure={'data': [
		{'x':[1,2],'y':[3,1]}
	], 'layout':go.Layout(title='Relative Stock Returns Comparison',
	yaxis = {'title':'Returns', 'tickerformat': ".2%"}
	)}),
	dcc.Markdown('''---'''),
	html.H1('YTD and total position return versurs S7P 500'),
	dcc.Graph(id='ytd1',
	figure = {'data':[
		go.Bar(
			x=data['Ticker'][0:20],
			y = data['Share YTD'][0:20],
			name = 'Ticker YTD'
		),
		go.Scatter(
			x=data['Ticker'][0:20],
			y = data['SP 500 YTD'][0:20],
			name = 'SP500 YTD'
		)
	],
	'layout':go.Layout(title='YTD Return vs S&P 500 YTD',
	barmode='group'
	xaxis = {'title':'Ticker'},
	yaxis = {'title':'Returns',
	'tickerFormat':".2%"}
	)}, style={'width':'50%','display':'inline-block'}
	),
	dcc.Graph(id='total1',
	figure = {'data': [
		go.Bar(
			x = data['Ticker #'][0:20],
			y = data['Ticker return'][0:20],
			name = 'Ticker total return'
		),
		go.Scatter(
			x = data['Ticker #'][0:20],
			y = data['SP Return'][0:20],
			name = 'SP500 total return'
		)
	],
	'layout':go.Layout(title:'Total return vs S&P 500',
	barmode='group',
	xaxis = {'title':'Ticker'},
	yaxis = {'title':'Returns', 'tickerformat':".2%"})}, 
	style={'wdith':'50%', 'display':'inline-block'}),

	dcc.Markdown(''' --- '''),
	html.H1('Cumulative Returns per position over time'),
	dcc.Graph(id='crot1', figure = {
		'data': [
			go.Bar(
				x = data['Ticker #'][0:20],
				y = data['Stock gain/loss'][0:20],
				name = 'Ticker total return ($)'
			),
			go.Bar(
				x = data['Ticker #'][0:20],
				y = data['SP 500 gain/loss'][0:20],
				name = 'SP500 total return ($)'
			),
			go.Scatter(
				x = data['Ticker #'][0:20],
				y= data['Ticker return'][0:20],
				name  = 'Ticker total Return %', yaxis = 'y2'
			)
		],
		'layout': go.Layout(title='Gain/Loss and Total return vs SP500',
		barmode = 'group',
		xaxis = {'title': 'Ticker'},
		yaxis={'title': 'Gain/Loss ($)'},
		yaxis2 = {'title':'Ticker Return', 'overlaying':'y','side':'right', 'tickerformat':".1%"},
		legend = {'x':'0.75','y':'1.2'}
		)
	}, style {'width': '100%'}),

	dcc.Markdown(''' --- '''),
	html.H1('Total cumulative investments by portfolio over time'),
	dcc.Graph(id = 'tcot1',
	figure = {'data': [
		go.Scatter(
			x = data['Ticker #'],
			y = data['Cum Invst'],
			mode = 'lines+markers',
			name = 'Cum Invst'
		),
		go.Scatter(
			x=data['Ticker #'],
			y = data['Cum Ticker Returns'],
			mode = 'lines+markers',
			name = 'Cum Ticker Returns'
		),
		go.Scatter(
			x = data['Ticker #'],
			y = data['Cum Ticker Returns'],
			mode = 'lines+markers',
			name = 'Cum Ticker Returns'
		),
		go.Scatter(
		x = data['Ticker #'],
		y = data['Cum SP Returns'],
		mode = 'lines+markers',
		name = 'Cum SP500 Returns')
	],
	'layout':
	go.Layout(title: 'Cumulative Investment Returns',
	xaxis={'title': 'Ticker'},
	yaxis = {'title': 'Returns'},
	legend = {'x':'1'})},
	style={'width': '100%'}
	),
	dcc.Graph(id='tcot2',
	figure = {'data': [
		go.Bar(
			x = data['Ticker #'],
			y = data['Cum Invst'],
			name = 'Cum Invst'
		),
		go.Bar(
			x = data['Ticker #'],
			y = data['Cum SP Returns'],
			name = 'Cum SP500 Returns'
		),
		go.Bar(
			x = data['Ticker #'],
			y = data['Cum Ticker Returns'],
			name = 'Cum Ticker Returns'
		),
		go.Scatter(
			x = data['Ticker #'],
			y = data['Cum Ticker ROI Multi']
			name = 'Cum ROI Mult', yaxis = 'y2'
		)
	],
	'layout':go.Layout(title='Total Cumulative Invesments ROI Multiple, over time', barmode='group',
	xaxis = {'title':'ticker'},
	yaxis = {'title': 'Returns'},
	yaxis2 = {'title': 'Cum ROI Multi', 'overlaying':'y', 'side':'right'},
	legend: {'x':'0.75','y':'1.2'}
	)}, style= {'width': '100%'}),
	
	dcc.Markdown(''' --- '''),
	html.H1('Current share price vs closing high since purchased'),
	dcc.Graph(id='cvh1', figure = {'data': [
		go.Bar(
			x = data['Ticker #'][0:20],
			y = data['Pct off high'][0:20],
			name = 'Pct off high'
		),
		go.Scatter(
			x = data['Ticker #'][0:20],
			y = [-0.25, -0.25, -0.25, -0.25, -0.25, -0.25,-0.25, -0.25, -0.25,-0.25, -0.25, -0.25,-0.25, -0.25, -0.25,-0.25, -0.25, -0.25,-0.25, -0.25],
			mode = 'lines',
			name = 'Trailing stop marker',
			ine = {'color':'red'}
		)
	], 'layout': go.Layout(title='Adj Close % off of high since purchased', barmode = 'group',xaxis = {'title':'Ticker'},
	yaxis = {'title':'%Below High since purchased', 'tickformat': '0.2%'},
	legend = {'x':'o.8','y':'1.2'}
	)}, style={'width': '100%'}
	),
	dcc.Markdown(''' --- ''')
])

@app.callback(Output('my_graph', 'figure'),
[Input('submit-button', 'n_clicks')],
[State('my_ticker_symbol', 'value'),
State('my_date_picker', 'start_date'),
State('my_date_picker', 'end_date')
])