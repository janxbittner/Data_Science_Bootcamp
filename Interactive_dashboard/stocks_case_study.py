'''
In this case i will show Amazon and it competitors stocks in dashboard.
'''

# %% Data load
import pandas_datareader.data as web
import datetime as dt

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

AMZN = web.DataReader("AMZN", 'yahoo', start, end)
EBAY = web.DataReader("EBAY", 'yahoo', start, end)
BABA = web.DataReader("BABA", 'yahoo', start, end)
BIG = web.DataReader("BIG", 'yahoo', start, end)
BBY = web.DataReader("BBY", 'yahoo', start, end)

# %% Dashboard create
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

year_option = AMZN.index.year.unique().to_list()
year_option = [str(i) for i in year_option]
year_option.append('2015-2020')
app.layout = html.Div([
    html.H1("Amazon vs. Competitiors",
            style = {'textAlign': 'center'}),
    html.H4("Choose year"),
    html.Div(
        [
            dcc.Dropdown(
                id="Year",
                options=[{
                    'label': i,
                    'value': i
                } for i in year_option],
                value='2015-2020'),
        ],
        style={'width': '25%',
               'display': 'inline-block',
               'textAlign': 'center'}),
    dcc.Graph(id='Close-graph'),
    dcc.Graph(id='Volume-graph'),
    dcc.Graph(id='Heat-map',
              style={'width': '80%',
                     'padding-left':'10%', 'padding-right':'10%'})
])

'''Adjust scatter chart'''

@app.callback(
    dash.dependencies.Output('Close-graph', 'figure'),
    [dash.dependencies.Input('Year', 'value')])
def update_graph(Year):
    if '-' not in Year:
        Year = int(Year)

    if isinstance(Year,int):
        df_AMZN = AMZN[AMZN.index.year == Year]
        df_EBAY = EBAY[EBAY.index.year == Year]
        df_BABA = BABA[BABA.index.year == Year]
        df_BIG = BIG[BIG.index.year == Year]
        df_BBY = BBY[BBY.index.year == Year]
    else:
        df_AMZN = AMZN.copy()
        df_EBAY = EBAY.copy()
        df_BABA = BABA.copy()
        df_BIG = BIG.copy()
        df_BBY = BBY.copy()

    trace1 = go.Scatter(x=df_AMZN.index, y=df_AMZN.Close, name='Amazon')
    trace2 = go.Scatter(x=df_EBAY.index, y=df_EBAY.Close, name='eBuy')
    trace3 = go.Scatter(x=df_BABA.index, y=df_BABA.Close, name='Alibaba')
    trace4 = go.Scatter(x=df_BIG.index, y=df_BIG.Close, name='Big Lots')
    trace5 = go.Scatter(x=df_BBY.index, y=df_BBY.Close, name='Best Buy')

    return {
        'data': [trace1,trace2,trace3,trace4,trace5],
        'layout':
        go.Layout(
            title='Close values for {}'.format(Year),
            yaxis_type = 'log',
            yaxis_title = 'Value in $ [Log scale]')
    }
'''Adjust bar chart: '''

@app.callback(
    dash.dependencies.Output('Volume-graph', 'figure'),
    [dash.dependencies.Input('Year', 'value')])
def update_Volume(Year):
    if '-' not in Year:
        Year = int(Year)

    if isinstance(Year,int):
        df_AMZN = AMZN[AMZN.index.year == Year]
        df_EBAY = EBAY[EBAY.index.year == Year]
        df_BABA = BABA[BABA.index.year == Year]
        df_BIG = BIG[BIG.index.year == Year]
        df_BBY = BBY[BBY.index.year == Year]
    else:
        df_AMZN = AMZN.copy()
        df_EBAY = EBAY.copy()
        df_BABA = BABA.copy()
        df_BIG = BIG.copy()
        df_BBY = BBY.copy()

    trace1 = go.Bar(x=df_AMZN.index, y=df_AMZN.Volume, name='Amazon')
    trace2 = go.Bar(x=df_EBAY.index, y=df_EBAY.Volume, name='eBuy')
    trace3 = go.Bar(x=df_BABA.index, y=df_BABA.Volume, name='Alibaba')
    trace4 = go.Bar(x=df_BIG.index, y=df_BIG.Volume, name='Big Lots')
    trace5 = go.Bar(x=df_BBY.index, y=df_BBY.Volume, name='Best Buy')

    return {
        'data': [trace1,trace2,trace3,trace4,trace5],
        'layout':
        go.Layout(
            title='Volume values for {}'.format(Year),
            yaxis_type = 'log',
            yaxis_title = 'Volume in Log scale',
            barmode='stack')
    }
        
""" Adjust heat map"""
@app.callback(
    dash.dependencies.Output('Heat-map', 'figure'),
    [dash.dependencies.Input('Year', 'value')])
def update_Heatmap(Year):
    if '-' not in Year:
        Year = int(Year)

    if isinstance(Year,int):
        df_AMZN = AMZN[AMZN.index.year == Year]
        df_EBAY = EBAY[EBAY.index.year == Year]
        df_BABA = BABA[BABA.index.year == Year]
        df_BIG = BIG[BIG.index.year == Year]
        df_BBY = BBY[BBY.index.year == Year]
    else:
        df_AMZN = AMZN.copy()
        df_EBAY = EBAY.copy()
        df_BABA = BABA.copy()
        df_BIG = BIG.copy()
        df_BBY = BBY.copy()

    df_closes = pd.concat([df_AMZN.Close, df_EBAY.Close,df_BABA.Close,
                           df_BIG.Close,df_BBY.Close], axis=1,)
    
    df_closes.columns = ['Close_Amazon','Close_eBuy','Close_Alibaba',
                         'Close_Big','Close_Best_Buy']
    df_closes = df_closes.corr()
    z = df_closes.values
    y = df_closes.columns.to_list()
    x = df_closes.columns.to_list()
    
    trace1 = go.Heatmap(z = z, x=x, y=y, colorscale = 'Viridis')

    return {
        'data': [trace1],
        'layout':
        go.Layout(
            title='Correlation of Close value for {}'.format(Year),
            yaxis_title = 'Columns name',
            yaxis_automargin = True,
            xaxis_title = 'Columns name')
    }
        

if __name__ == '__main__':
    app.run_server(debug=False)
        
#%% SAVE DASHBOARD TO HTML
import plotly.offline 

plotly.offline.plot(
  app,
  show_link=False,
  filename = 'my_file.html')

