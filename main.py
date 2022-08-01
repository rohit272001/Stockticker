# import dash
# from dash import html
# from dash import dcc
#
# app = dash.Dash()
#
# app.layout = html.Div([
#         html.H1("Hello Dash!"),
#         html.Div("This is my first application using plotly."),
#
#         dcc.Graph(
#             id = 'samplechart',
#             figure = {
#                 'data' : [
#                     { 'x':[4,6,8],'y':[12,16,18], 'type':'bar', 'name':'first chart'}
#                 ],
#                 'layout' : {
#                     'title' : 'simple bar chart'
#                 }
#             }
#          )
#               ])
#
# if __name__ == '__main__':
#     app.run_server(port=8080)
#


#This library is used to initialize the dash application.
import dash
# This library is used to add graphs,other visual components.
from dash import dcc
# This library is used to include html tags.
from dash import html
#For data manipulation and mathematical operations.
import pandas as pd
#Reading the csv file.
data = pd.read_csv("indexData.csv")
#Manipulating the date.
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
#Initialising application.
app = dash.Dash(__name__)

app.layout = html.Div(

    children=[

    html.H1(children="Stock Exchange Analytics",),
    html.P(
    children="Analyzing day wise high and low prices of indexes.",
        ),
    dcc.Graph(
    figure={
        "data": [
    {
        "x": data["Date"],
        "y": data["High"],
        "type": "lines",
        },
        ],
        "layout": {"title": "Day-wise highest prices of indexes"},
        },
        ),
        dcc.Graph(
        figure={
            "data": [
            {
            "x": data["Date"],
            "y": data["Low"],
            "type": "lines",
            },
            ],
        "layout": {"title": "Day-wise lowest prices of indexes"},
            },
            ),
        dcc.Graph(
        figure={
            "data": [
            {
            "x": data["Date"],
            "y": data["Close"],
            "type": "lines",
            },
            ],
        "layout": {"title": "Day-wise closing prices of indexes"},
            },
            ),
        dcc.Graph(
        figure={
            "data": [
            {
            "x": data["Date"],
            "y": data["Open"],
            "type": "lines",
            },
            ],
        "layout": {"title": "Day-wise opening prices of indexes"},
            },
            ),
            ] )

if __name__ == "__main__":
    app.run_server(debug=True)