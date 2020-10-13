import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 1'),
    dcc.Dropdown(
        id='node-1-dropdown',
        options=[
            {'label': 'Node 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='node-1-display-value'),
    dcc.Link('Go to Node 13', href='/apps/app13'),
    html.Br(),
    dcc.Link('Go to Node 14', href='/apps/app14'),
    html.Br(),
    dcc.Link('Go to Node 18', href='/apps/app18'),
    html.Br(),
    dcc.Link('Go to Node 20', href='/apps/app20'),
])


@app.callback(
    Output('node-1-display-value', 'children'),
    [Input('node-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
