import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 4'),
    dcc.Dropdown(
        id='node-4-dropdown',
        options=[
            {'label': 'Node 4 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='node-4-display-value'),

])


@app.callback(
    Output('node-4-display-value', 'children'),
    [Input('node-4-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
