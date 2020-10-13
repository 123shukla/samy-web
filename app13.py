import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 13'),

    dcc.Link('Go to Node 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Go to Node 14', href='/apps/app14'),
    html.Br(),
    dcc.Link('Go to Node 18', href='/apps/app18'),
    html.Br(),
    dcc.Link('Go to Node 20', href='/apps/app20'),
])
