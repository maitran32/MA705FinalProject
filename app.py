#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Wed Dec  9 15:34:11 2020

@author: maitran

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([html.H1('Hello', style={'textAlign': 'center'})])

    server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
