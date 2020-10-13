import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 6'),
    dcc.Dropdown(
        id='node-6-dropdown',
        options=[
            {'label': 'Node 6 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='node-6-display-value'),

])


@app.callback(
    Output('node-6-display-value', 'children'),
    [Input('node-6-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
