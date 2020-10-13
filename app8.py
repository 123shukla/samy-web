import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 8'),
    dcc.Dropdown(
        id='node-8-dropdown',
        options=[
            {'label': 'Node 8 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='node-8-display-value'),

])


@app.callback(
    Output('node-8-display-value', 'children'),
    [Input('node-8-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
