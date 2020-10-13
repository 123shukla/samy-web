import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo
import base64
import textwrap
from datetime import datetime as dt
import plotly.express as px
import dash_auth
from app import app
import pandas


excel_data_df = pandas.read_excel('Book1.xlsx', sheet_name='Sheet172')

excel_data_df.columns = ["Date", "Temperature (°Celsius)", "Humidity (%)", "Pressure (Pascal)"]


features = excel_data_df.columns

layout = html.Div([
    html.H3(('Entrace (Node Sheet172)'),style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='xaxis172',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='Temperature (°Celsius)'
       )
   ],
style={'width': '48%', 'display': 'inline-block'}),

html.Div([  # this Div contains our output graph
        dcc.Graph(id='graph172')
        ], style={'width': '100%'}),
    html.Div([  # this Div contains our output graph
        dcc.Graph(id='graph175')
        ], style={'width': '100%'}),

# html.Div(id='node-31-display-value'),
# html.A(html.Button('Go to Bedroom (Node 80)', id='button-1', className='mr-1',style={'backgroundColor':'#C2F9EE'}),href='/nodes/node80'),
# dcc.Link('Go to Node 105', href='/nodes/node31')
])

@app.callback(Output('graph172', 'figure'),
              [Input('xaxis172', 'value')])

## Main Plotting Function

def update_graph(xaxis172_name):
    return {
           'data': [go.Scatter(
            x=excel_data_df['Date'],
            y=excel_data_df[xaxis172_name],
            #xbins=dict(start=5,end=30,size=1),
            # text=selected_city,
            marker_color='blue',
            mode='lines',
            # filtered_df['Date'],

            )],
        'layout': go.Layout(
            xaxis={'title': 'Date/Time'},
            yaxis={'title': xaxis172_name.title()},
            title="Line Plot",
            margin={'l': 40, 'b': 200, 't': 30, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(Output('graph175', 'figure'),
              [Input('xaxis172', 'value')])

## Main Plotting Function

def update_graph(xaxis172_name):
    return {
           'data': [go.Histogram(
            x=excel_data_df[xaxis172_name],
            # xbins=dict(start=5,end=30,size=1),
            # text=selected_city,
            marker_color='Red'
            # filtered_df['Date'],

            )],
        'layout': go.Layout(
            xaxis={'title': xaxis172_name.title()},
            yaxis={'title': 'Temperature'},
            title="Histogram",
            margin={'l': 40, 'b': 100, 't': 30, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)


# layout = html.Div([
#     html.H3('Node 105'),
#
#     dcc.Link('Go to Node 31', href='/nodes/node31')
# ])


# layout = html.Div([
#     html.H3('Node 116'),
#
#     dcc.Link('Go to Node 27', href='/nodes/node27')
# ])


# layout = html.Div([
#     html.H3('Node 197'),
#
#     dcc.Link('Go to Node 106', href='/nodes/node106')
# ])
