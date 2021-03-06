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
    html.H1('Insights of H1B Data 2011-2020', style={'textAlign': 'center'}),
    dcc.Markdown("""
                 *The dashboard app was built on data from website h1bdata.info
                 
                     By exploring the distribution of H1B filing submissions and their successful status\
                         through out the years, states, employers, the app could be used as an efficient strategy tool\
                             for foreigners who are in search of jobs/employers that support working visa application in the US,\
                                  especially in marketing field.*
                     
                 """,style={'textAlign': 'center'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }
        ),
    html.Div([
        
        html.Div([
             html.Br(),
             html.Br(),
            html.Br(),
       
            html.H6("Select Year:"),
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
              html.H6("Select State: "),
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
    html.H6("*"),
    dcc.Markdown("""
                 *The data is missing from year 2011 and year 2012 because job titles\
                     in Marketing Field started to be able to apply for H1B Visa from 2013.
                     Since then, California has been the top state that submitted H1B Visas for\
                         foreigners the most.*
                     
                 """)], 
    style={'display':'inline-block','width':'49%','float':'left'})
    ,
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
    html.Div([
     
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
    html.P("Enter number to display (maximum 50):"),
    daq.NumericInput(
        id='my-numeric-input',
        value=50
    )],
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

    ])])]) 

@app.callback(
    dash.dependencies.Output('stateSubmitgraph','figure'),
    [dash.dependencies.Input('yearDropdown','value'),
     dash.dependencies.Input('stateDropdown','value')]
    )
       
# Update the histogram

def update_hist(year_show, states_to_display):
    marketingdata = pd.read_csv('marketingdata.csv', usecols=['EMPLOYER', 'STATE', 'JOB TITLE', 'BASE SALARY', 'STATE', 'SUBMIT YEAR', 'START YEAR'])
    marketingdata = marketingdata[marketingdata['SUBMIT YEAR'] == int(year_show)]
    newdata = marketingdata[marketingdata.STATE.isin(states_to_display)]
    newfig = px.histogram(newdata,x="STATE")
    newfig.update_layout(
    title="Distribution of H1B Submissions in Selected States (Marketing Field Focus)",
    yaxis_title="H1B Filings Count",
    font=dict(
        size=8
    )
)
    return newfig


@app.callback(
    dash.dependencies.Output("barChart", "figure"), 
    [dash.dependencies.Input("cate-dropdown", "value"), 
     dash.dependencies.Input("my-numeric-input", "value")])

def update_bar_chart(cate, limit):
    data = pd.read_csv(cate)
    data['count'] = pd.to_numeric(data['count'])
    
    newdata = data.nlargest(limit,['count'])
    catname = newdata.columns[0]
    fig = px.bar(newdata, x=catname, y="count", barmode="group", height=400)
    fig.update_layout(
    title="Top Employers/State applying for H1B the most from 2011 to 2020",
    yaxis_title="H1B Filings Count",
    font=dict(
        size=8
    )
)

    return fig



#============================================================================#

certified1 = pd.read_csv('certified1.csv')
certified2 = pd.read_csv('certified2.csv')
deniedDf = pd.read_csv('deniedDf.csv')
withdrawnDf = pd.read_csv('withdrawnDf.csv')
cer_withDf = pd.read_csv('cer_withDf.csv')

frames = [certified1, certified2, deniedDf, withdrawnDf,cer_withDf ]

caseStatusData = pd.concat(frames)

@app.callback(
    dash.dependencies.Output("unstackedBar", "figure"), 
    [dash.dependencies.Input("sort_by_dropdown", "value")])


def update_unstack_barchart(ctg):
    if ctg == 'STATE':
        datadf = caseStatusData.groupby(['STATE', 'CASESTATUS']).size()
    if ctg == 'EMPLOYER':
        topEmList = caseStatusData['EMPLOYER'].value_counts()[:50].index.tolist()
        topEmDf= caseStatusData[caseStatusData['EMPLOYER'].isin(topEmList)]
        datadf = topEmDf.groupby(['EMPLOYER', 'CASESTATUS']).size()
    wide_df = datadf.unstack(level=-1)
    name = wide_df.index
    fig = px.bar(wide_df, x=name, y= ['CERTIFIED','CERTIFIED - WITHDRAWN','DENIED','WITHDRAWN'])
    fig.update_layout( title="H1B Case Status by Employers/States",
    yaxis_title="H1B Filings Count",
    font=dict(
        size=8
    )
)

    return fig



server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
