import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import base64
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as pyo
import textwrap
from datetime import datetime as dt
import plotly.express as px
import dash_auth
from apps import app31,app27,app116,app105,app106,app197,app186,app109,app189,app88,app114,app110,app180,app93,app107,app108,app100,app196,app112,app22,app113,app92,app72,app173,app122,app195,app133,app182,app69,app190,app125,app179,app80,app181,app62,app119,app172,app177,app192,app89,app65
from flask import Flask
from app import server
# node27, node116, node106, node197, node186, node109, node189, node88, node114, node110, node180, node93, node107, node108, node100, node196, node112, node22, node113, node1, node13, node14, node18, node20, node16, node3, node19, node17, node21, node4, node5, node6, node7, node8, node2, node15, node9, node10, node180_a
# 0.6.0 or above is required
server = app.server
# server = Flask(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

image_filename = 'Logo.png'
image_filename1 = 'DST.png'
image_filename2 = 'EPSRC.png'
image_filename3 = 'UoB.png'
image_filename4 = 'IITD.png'
image_filename5 = 'CBRIl.png'
image_filename6 = 'IITDD.png'
# replace with your own image
# image_filename1 = 'zero.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())
encoded_image4 = base64.b64encode(open(image_filename4, 'rb').read())
encoded_image5 = base64.b64encode(open(image_filename5, 'rb').read())
encoded_image6 = base64.b64encode(open(image_filename6, 'rb').read())
# encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
index_page = html.Div([
html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'width': '15%', 'height': '15%','textAlign': 'center'}),
html.Label(['User Login', html.A('Login', href='https://netzedlab.com/seema/website/login.php',style={'width': '50%', 'height': '40%','textAlign': 'center','font-size': '24px'})]),

# html.H3('Zero Peak Energy Design for India',style={'text-align':'top-center'}),
# html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),style={'width': '10%','display': 'inline-block','vertical-align': 'right
html.H4('ABOUT',style={'text-align':'center','background-color':'#F2F3F4'}),
html.P('This is an Indo-UK collaborative research project which aims to decouple building energy use from economic growth in India through a new science of zero peak energy building design. We aim to provide ‘Thermal Stress Free, living conditions whilst minimizing mean and peak energy demand under a changing Indian climate',style={'text-align':'center', 'margin': '10px 50px 20p'}),
# html.P('',style={'text-align':''}),
html.H4('FUNDING AGENCIES',style={'text-align':'center','background-color':'#F2F3F4','background-color':'#F2F3F4'}),
html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'middle','margin-left': '25%'}),
html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),style={'width': '15%', 'display': 'inline-block', 'vertical-align': 'middle','margin-left': '10%'}),
html.H4('COLLABORATING INSTITUTES',style={'text-align':'center','background-color':'#F2F3F4'}),
html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'width': '10%', 'display': 'inline-block','vertical-align': 'middle','margin-left': '25%'}),
html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={'width': '25%', 'display': 'inline-block','vertical-align': 'middle','margin-left': '0.5%'}),
html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'width': '10%', 'display': 'inline-block','vertical-align': 'middle','margin-left': '1%'}),
html.Img(src='data:image/png;base64,{}'.format(encoded_image6.decode()),style={'width': '10%', 'display': 'inline-block','vertical-align': 'middle','margin-left': '6%'}),
    html.Br(),
html.H4('PROJECT LOCATION',style={'text-align':'center','background-color':'#F2F3F4'}),
    html.Div([
        dcc.Graph(id='feature-graphic_1'),
                    dcc.Textarea(id='pogo',
                    placeholder='Enter a value...',
                    value=' Ahmedabad | Chennai | Delhi | Hyderabad | Dehradun | Mussoorie | Kolkata ',style={'text-align':'center','background-color':'#F2F3F4','width': '100%','aaa': '#ff0066','font-weight': 'bold','font-size': '23px'}
                    # style={'width': '100%'}
                    )

        ], style={'padding':10}),


])
# Page 1 callback
@app.callback(Output('feature-graphic_1', 'figure'),
              [Input('pogo', 'value')])

## Main Plotting Function

def update_graph(sos):

    india_cities = pd.read_csv("k.csv")
    fig = px.scatter_mapbox(india_cities, lat="lat", lon="lon", hover_name="City", hover_data=["Country"],
                            color_discrete_sequence=["Cyan"], zoom=3.4, height=400)
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
          ])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app31':
        return app31.layout
    elif pathname == '/apps/app105':
        return app105.layout
    elif pathname == '/apps/app27':
        return app27.layout
    elif pathname == '/apps/app116':
        return app116.layout
    elif pathname == '/apps/app106':
            return app106.layout
    elif pathname == '/apps/app197':
            return app197.layout
    elif pathname == '/apps/app186':
            return app186.layout
    elif pathname == '/apps/app109':
            return app109.layout
    elif pathname == '/apps/app189':
            return app189.layout
    elif pathname == '/apps/app88':
            return app88.layout
    elif pathname == '/apps/app114':
            return app114.layout
    elif pathname == '/apps/app110':
            return app110.layout
    elif pathname == '/apps/app180':
            return app180.layout
    elif pathname == '/apps/app93':
           return app93.layout
    elif pathname == '/apps/app107':
           return app107.layout
    elif pathname == '/apps/app108':
           return app108.layout
    elif pathname == '/apps/app100':
           return app100.layout
    elif pathname == '/apps/app196':
           return app196.layout
    elif pathname == '/apps/app112':
           return app112.layout
    elif pathname == '/apps/app22':
          return app22.layout
    elif pathname == '/apps/app113':
          return app113.layout
    elif pathname == '/apps/app13':
          return app13.layout
    elif pathname == '/apps/app14':
          return app14.layout
    elif pathname == '/apps/app18':
          return app18.layout
    elif pathname == '/apps/app20':
          return app20.layout
    elif pathname == '/apps/app16':
          return app16.layout
    elif pathname == '/apps/app3':
          return app3.layout
    elif pathname == '/apps/app19':
          return app19.layout
    elif pathname == '/apps/app17':
          return app17.layout
    elif pathname == '/apps/app21':
          return app21.layout
    elif pathname == '/apps/app4':
          return app4.layout
    elif pathname == '/apps/app5':
          return app5.layout
    elif pathname == '/apps/app6':
          return app6.layout
    elif pathname == '/apps/app7':
          return app7.layout
    elif pathname == '/apps/app8':
          return app8.layout
    elif pathname == '/apps/app2':
          return app2.layout
    elif pathname == '/apps/app15':
          return app15.layout
    elif pathname == '/apps/app9':
          return app9.layout
    elif pathname == '/apps/app10':
          return app10.layout
    elif pathname == '/apps/app92':
          return app92.layout
    elif pathname == '/apps/app72':
          return app72.layout
    elif pathname == '/apps/app173':
          return app173.layout
    elif pathname == '/apps/app122':
          return app122.layout
    elif pathname == '/apps/app195':
          return app195.layout
    elif pathname == '/apps/app133':
          return app133.layout
    elif pathname == '/apps/app182':
          return app182.layout
    elif pathname == '/apps/app69':
          return app69.layout
    elif pathname == '/apps/app190':
          return app190.layout
    elif pathname == '/apps/app125':
          return app125.layout
    elif pathname == '/apps/app179':
          return app179.layout
    elif pathname == '/apps/app80':
          return app80.layout
    elif pathname == '/apps/app181':
          return app181.layout
    elif pathname == '/apps/app62':
          return app62.layout
    elif pathname == '/apps/app119':
          return app119.layout
    elif pathname == '/apps/app172':
          return app172.layout
    elif pathname == '/apps/app177':
          return app177.layout
    elif pathname == '/apps/app192':
          return app192.layout
    elif pathname == '/apps/app89':
          return app89.layout
    elif pathname == '/apps/app65':
          return app65.layout

    else:
        return index_page

if __name__ == '__main__':
    app.run_server()
