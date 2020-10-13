import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 16'),
    dcc.Dropdown(
        id='node-16-dropdown',
        options=[
            {'label': 'Node 16 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='node-16-display-value'),
    dcc.Link('Go to Node 3', href='/apps/app3'),
    html.Br(),
    dcc.Link('Go to Node 19', href='/apps/app19'),
    html.Br(),
    dcc.Link('Go to Node 17', href='/apps/app17'),
    html.Br(),
    dcc.Link('Go to Node 21', href='/apps/app21'),
])


@app.callback(
    Output('node-16-display-value', 'children'),
    [Input('node-16-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
