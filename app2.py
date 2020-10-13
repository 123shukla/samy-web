import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 2'),
    dcc.Dropdown(
        id='node-2-dropdown',
        options=[
            {'label': 'Node 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='node-2-display-value'),
    dcc.Link('Go to Node 15', href='/apps/app15'),
    html.Br(),
    dcc.Link('Go to Node 9', href='/apps/app9'),
    html.Br(),
    dcc.Link('Go to Node 10', href='/apps/app10'),

])


@app.callback(
    Output('node-2-display-value', 'children'),
    [Input('node-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
