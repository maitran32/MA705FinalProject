#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Wed Dec  9 15:34:11 2020

@author: maitran

"""

import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

marketingdata = pd.read_csv('marketingdata.csv', usecols=['EMPLOYER', 'STATE', 'JOB TITLE', 'BASE SALARY', 'STATE', 'SUBMIT YEAR', 'START YEAR'])
#create a histogram for distribution of H1B in all states over the year (submit year

if __name__ == '__main__':
    app.run_server(debug=True)
