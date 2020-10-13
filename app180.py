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

excel_data_df = pandas.read_excel('Book1.xlsx', sheet_name='Sheet180')

excel_data_df.columns = ["Date", "Temperature (°Celsius)", "Humidity (%)", "Pressure (Pascal)"]


features = excel_data_df.columns

layout = html.Div([
    html.H3(('Power Supply (Node 180)'),style={'textAlign': 'center'}),
    html.Div([
         dcc.Dropdown(
            id='xaxis180',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='Temperature (°Celsius)'
        )
    ],
 style={'width': '48%', 'display': 'inline-block'}),

 html.Div([  # this Div contains our output graph
        dcc.Graph(id='graph26')
        ], style={'width': '100%'}),
    html.Div([  # this Div contains our output graph
        dcc.Graph(id='graph27')
        ], style={'width': '100%'}),

# html.Div(id='node-31-display-value'),
# dcc.Link('Go to Node 105', href='/nodes/node105')
])

@app.callback(Output('graph26', 'figure'),
              [Input('xaxis180', 'value')])

## Main Plotting Function

def update_graph(xaxis180_name):
    return {
           'data': [go.Scatter(
            x=excel_data_df['Date'],
            y=excel_data_df[xaxis180_name],
            #xbins=dict(start=5,end=30,size=1),
            # text=selected_city,
            marker_color='Red',
            mode='lines',
            # filtered_df['Date'],

            )],
        'layout': go.Layout(
            xaxis={'title': 'Date/Time'},
            yaxis={'title': xaxis180_name.title()},
            title="Line Plot",
            margin={'l': 40, 'b': 200, 't': 50, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(Output('graph27', 'figure'),
              [Input('xaxis180', 'value')])

## Main Plotting Function

def update_graph(xaxis180_name):
    return {
           'data': [go.Histogram(
            x=excel_data_df[xaxis180_name],
            #xbins=dict(start=5,end=30,size=1),
            # text=selected_city,
            marker_color='Green'
            # filtered_df['Date'],

            )],
        'layout': go.Layout(
            xaxis={'title': xaxis180_name.title()},
            yaxis={'title': 'Temperature'},
            title="Histogram",
            margin={'l': 40, 'b': 100, 't': 30, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
