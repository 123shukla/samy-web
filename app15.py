import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Node 15'),

    dcc.Link('Go to Node 2', href='/apps/app2'),
    html.Br(),
    dcc.Link('Go to Node 9', href='/apps/app9'),
    html.Br(),
    dcc.Link('Go to Node 10', href='/apps/app10'),

])
