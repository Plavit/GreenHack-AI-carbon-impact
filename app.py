# -*- coding: utf-8 -*-

import dash
from dash import dcc
from dash import html
from dash import Dash
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import pathlib

from dash.dependencies import Input, Output
from urllib.parse import quote as urlquote
from flask import Flask, send_from_directory, send_file

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Used dataset version names
DATA_MOCK = 'chatGPT_users.csv'

df = pd.read_csv('data/{}'.format(DATA_MOCK))

# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
server = Flask(__name__)


@server.route("/data/<path:path>")
def download(path):
    """Downloads the desired file from the data folder."""
    return send_file('data/' + path,
                     mimetype='text/csv',
                     attachment_filename=path,
                     as_attachment=True)


# Download link generation
def file_download_link(filename):
    """Creates a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/data/{}".format(urlquote(filename))
    return html.Div(
        [
            html.A(
                html.Button("Download the full dataset: " + filename),
                href=location,
            )
        ],
        className="download-button"
    )

def get_piechart():
    # Load data from CSV file
    data = pd.read_csv('data/dummy_pie.csv')

    # Calculate the count of each category in the data
    category_counts = data['Type'].value_counts()

    # Create a pie chart using Plotly Express
    fig = px.pie(data_frame=data, names=category_counts.index, values=category_counts.values, title='Category Distribution')

    # Create the Dash application
    app = Dash(__name__)

    # Define the layout of the application
    return html.Div(
        children=[
            html.H1('Plotly Pie Chart'),
            dcc.Graph(figure=fig)
        ]
    )

# App server setup
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)
server = app.server

# App layout rendering
app.layout = html.Div(
    children=[
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src='assets/Logo-text-en.png',
                            draggable='False',
                            id="logo",
                            height='auto',
                            width=220,
                        )
                    ],
                    className="three columns",
                ),
                html.Div(
                    [
                        html.H3(
                            "Milee GreenAI benchmark",
                            style={"margin-bottom": "0px"},
                        ),
                        html.H5(
                            "The green AI climate impact metric",
                            style={"margin-top": "0px"}
                        ),
                        html.I(
                            [
                                "Created by ",
                                html.A(
                                    "Marek Miltner",
                                    href="https://github.com/Plavit",
                                    target="_blank"
                                ),
                                ", and ",
                                html.A(
                                    "Alena Moravová",
                                    href="https://github.com/moraval",
                                    target="_blank"
                                ),
                            ],
                            style={"margin-top": "0px"}
                        ),

                    ],
                    className="eight columns",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Contact the authors", id="contact-button"),
                            href="mailto:marek.szeles@eforce.cvut.cz",
                        )
                    ],
                    className="three columns",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    children=[
                                        html.Div(
                                            [
                                                html.H3(
                                                    "Methodology"
                                                ),
                                                html.P(
                                                    "The final index is calculated "
                                                    "using the following formula:"
                                                ),
                                                html.I("EGDI = ⅓ × (OSI+TII+HCI)"
                                                       ),
                                                html.H6(
                                                    "The components of the index are defined like so: "
                                                ),
                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "1"
                                                        ),
                                                        html.Li(

                                                            "2",


                                                        ),
                                                        html.Li(

                                                            "3",


                                                        )
                                                    ]
                                                ),
                                                html.P(
                                                    [
                                                        "More information about the methodology can be found on ",
                                                        html.A(
                                                            "the project Open Source repository",
                                                            href="https://github.com/Plavit/GreenHack-AI-carbon-impact",
                                                            target="_blank",
                                                        ),
                                                        "."
                                                    ]
                                                )
                                            ]
                                        )
                                    ],
                                    id="un_description",
                                    className="pretty_container description twelve columns flex-display"
                                ),
                            ],
                            className="content_holder row twelve columns flex-display"
                        ),

                    ],
                    className="pretty_container_bg twelve columns",
                ),
            ],
            className="row flex-display",
        ),


    ],
    id="mainContainer",
    style={'columnCount': 1, "display": "flex", "flex-direction": "column"},
)

app.title = 'GreenHack'


if __name__ == '__main__':
    app.run_server(debug=True)
