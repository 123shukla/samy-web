import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 17'),

    dcc.Link('Go to Node 16', href='/apps/app16'),
    html.Br(),
    dcc.Link('Go to Node 3', href='/apps/app3'),
    html.Br(),
    dcc.Link('Go to Node 19', href='/apps/app19'),
    html.Br(),
    dcc.Link('Go to Node 21', href='/apps/app21'),
])
