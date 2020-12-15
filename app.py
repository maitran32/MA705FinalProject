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
import dash_daq as daq


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
    html.H1('Insights of H1B Data 2011-2020', style={'textAlign': 'center'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),
    html.Div([
        
        html.Div([
             html.Br(),
             html.Br(),
            html.Br(),
       
            html.H4("Select Year:"),
              dcc.Dropdown(options=[{'label': '2011', 'value': '2011'},
                                    {'label': '2012', 'value': '2012'},
                                    {'label': '2013', 'value': '2013'},
                                    {'label': '2014', 'value': '2014'},
                                    {'label': '2015', 'value': '2015'},
                                    {'label': '2016', 'value': '2016'},
                                    {'label': '2017', 'value': '2017'},
                                    {'label': '2018', 'value': '2018'},
                                    {'label': '2019', 'value': '2019'},
                                    {'label': '2020', 'value': '2020'}],
                           id='yearDropdown',
                           value='2020'),
              html.H4("Select State: "),
    dcc.Dropdown(options=[{'label': 'Connecticut', 'value': 'CT'},{'label': 'Georgia', 'value': 'GA'},
                           {'label': 'New Jersey', 'value': 'NJ'},{'label': 'Pennsylvania', 'value': 'PA'},
                           {'label': 'Texas', 'value': 'TX'},{'label': 'New York', 'value': 'NY'},
                           {'label': 'California', 'value': 'CA'},{'label': 'Illinois', 'value': 'IL'},
                           {'label': 'Virginia', 'value': 'VA'},{'label': 'Missouri', 'value': 'MO'},
                           {'label': 'Massachusettes', 'value': 'MA'},{'label': 'Washington', 'value': 'WA'},
                           {'label': 'Florida', 'value': 'FL'},{'label': 'Delaware', 'value': 'DE'},
                           {'label': 'Oregon', 'value': 'OR'},{'label': 'Arizona', 'value': 'AZ'},
                           {'label': 'Minnesota', 'value': 'MN'},{'label': 'Indiana', 'value': 'IN'},
                           {'label': 'Maryland', 'value': 'MD'},{'label': 'North Carolina', 'value': 'NC'},
                           {'label': 'Michigan', 'value': 'MI'},{'label': 'Ohio', 'value': 'OH'},
                           {'label': 'Idaho', 'value': 'ID'},{'label': 'Kansas', 'value': 'KS'},
                           {'label': 'Utah', 'value': 'UT'},{'label': 'Tennessee', 'value': 'TN'},
                           {'label': 'Colorado', 'value': 'CO'},{'label': 'Rhode Island', 'value': 'RI'},
                           {'label': 'Hawaii', 'value': 'HI'},{'label': 'New Hampshire', 'value': 'NH'},
                           {'label': 'Kentucky', 'value': 'KY'}],multi=True,
                            id="stateDropdown",
                            value=['CT', 'GA', 'NJ','PA','TX','NY','CA','IL',
                                   'VA','MO','MA','WA','FL','DE','OR','AZ','MI','IN'],
                            style={'height': '5px'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4("*"),
    dcc.Markdown("""
                 ***The data is missing from year 2011 and year 2012 because job titles\
                     in Marketing Field started to be able to apply for H1B Visa from 2013.
                     Since then, California has been the top state that submitted H1B Visas for\
                         foreigners the most.
                     
                 """)], 
    style={'display':'inline-block','width':'49%','float':'left'})
    ,
    html.Div([
    html.H4("Histogram of H1B Visa Submissions in Selected States\n Marketing Field Focus"),
     
    dcc.Graph(id='stateSubmitgraph',
              style={'display':'inline-block','width':'49%','float':'right'})]),
    html.Br(),
    html.Br(),
    
    html.Div([
      html.Br(),
             html.Br(),
            html.Br(),
       
    dcc.Graph(id="barChart"),
    html.P("Select category to display:"),
    dcc.Dropdown(id="cate-dropdown", 
                 options=[{'label': 'Employers', 'value': 'employerCount.csv'},
                                    {'label': 'States', 'value': 'stateCount.csv'}],
                 value='stateCount.csv'),
    html.P("Enter number to display (maximum 50):")],
    style={'width': '49%', 'display': 'inline-block', 'float': 'left'}),

    html.Div([
      html.Br(),
             html.Br(),
            html.Br(),
       
    dcc.Graph(id="unstackedBar"),
    html.P("Select category to display:"),
    dcc.Dropdown(id="sort_by_dropdown", 
                 options=[{'label': 'Employers', 'value': 'EMPLOYER'},
                                    {'label': 'States', 'value': 'STATE'}],
                 value='STATE')
    ],
    style={'width': '49%', 'display': 'inline-block', 'float': 'right','borderBottom': 'thin lightgrey solid'})

    ])])

server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
