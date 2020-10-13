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

# df1 = pd.read_csv('merged_22_humidity_pressure_h.csv')
excel_data_df = pandas.read_excel('Book1.xlsx', sheet_name='Sheet105')
excel_data_df.columns = ["Date", "CO2 (ppm)", "Temperature (°Celsius)", "Humidity (%)", "Pressure (Pascal)"]



features = excel_data_df.columns

layout = html.Div([
    html.H3(('Bedroom (Node 105)'),style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='xaxis105',
            options=[{'label': i.title(), 'value': i} for i in features],
            value='CO2 (ppm)'
       )
   ],
style={'width': '48%', 'display': 'inline-block'}),

html.Div([  # this Div contains our output graph
        dcc.Graph(id='graph3')
        ], style={'width': '100%'}),
    html.Div([  # this Div contains our output graph
        dcc.Graph(id='graph4')
        ], style={'width': '100%'}),

# html.Div(id='node-31-display-value'),
html.A(html.Button('Go to Living Room (Node 31)', id='button-1', className='mr-1',style={'backgroundColor':'#C2F9EE'}),href='/apps/app31'),
])

@app.callback(Output('graph3', 'figure'),
              [Input('xaxis105', 'value')])

## Main Plotting Function

def update_graph(xaxis105_name):
    return {
           'data': [go.Scatter(
            x=excel_data_df['Date'],
            y=excel_data_df[xaxis105_name],
            #xbins=dict(start=5,end=30,size=1),
            # text=selected_city,
            marker_color='Orange',
            mode='lines',
            # filtered_df['Date'],

            )],
        'layout': go.Layout(
            xaxis={'title': 'Date/Time'},
            yaxis={'title': xaxis105_name.title()},
            title="Line Plot",
            margin={'l': 40, 'b': 200, 't': 30, 'r': 0},
            hovermode='closest'
        )
    }

@app.callback(Output('graph4', 'figure'),
              [Input('xaxis105', 'value')])

## Main Plotting Function

def update_graph(xaxis105_name):
    return {
           'data': [go.Histogram(
            x=excel_data_df[xaxis105_name],
            # xbins=dict(start=5,end=30,size=1),
            # text=selected_city,
            marker_color='Red'
            # filtered_df['Date'],

            )],
        'layout': go.Layout(
            xaxis={'title': xaxis105_name.title()},
            yaxis={'title': 'Temperature'},
            title="Histogram",
            margin={'l': 40, 'b': 100, 't': 30, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
