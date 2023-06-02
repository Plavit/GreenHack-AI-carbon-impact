# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
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


app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

server = app.server

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
                            "eGovernment index dashboard",
                            style={"margin-bottom": "0px"},
                        ),
                        html.H5(
                            "A simple overview of UN and EU eGovernment benchmark indices",
                            style={"margin-top": "0px"}
                        ),
                        html.I(
                            [
                                "Created as part of a paper submission for the Cambridge Journal of Science and Policy "
                                "by Marek Szeles and Anshumaan Krishnan Ayyangar, expanding on ",
                                html.A(
                                    "previous work done by the former",
                                    href="https://github.com/Plavit/eGovernment-index-dashboard",
                                    target="_blank"
                                )
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
                                                    "UN eGovernment index"
                                                ),
                                                html.P(
                                                    "The e-Government Development Index (EGDI) is being published by "
                                                    "the United Nations since 2001. It is a composite indicator "
                                                    "involving three components – Online Service Index(OSI), "
                                                    "Telecommunication Infrastructure Index (TII) "
                                                    "and Human Capital Index (HCI). The final index is calculated "
                                                    "using the following formula:"
                                                ),
                                                html.I("EGDI = ⅓ × (OSI+TII+HCI)"
                                                       ),
                                                html.H6(
                                                    "The three components of the index are defined like so: "
                                                ),
                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            "OSI is the normalised score between 0 and 1, which"
                                                            " is equal to the difference of the "
                                                            "actual total score and the lowest total score divided by "
                                                            "the range of total score values for all countries. "
                                                        ),
                                                        html.Li(
                                                            [
                                                                "Each country’s TII is the arithmetic average of",
                                                                html.Ul(
                                                                    [
                                                                        html.Li(
                                                                            "Estimated internet users "
                                                                            "per 100 inhabitants;",
                                                                        ),
                                                                        html.Li(
                                                                            "Number of mobile subscribers "
                                                                            "per 100 inhabitants;"
                                                                        ),
                                                                        html.Li(
                                                                            "Active mobile broadband subscriptions"
                                                                            "per 100 inhabitants;"
                                                                        ),
                                                                        html.Li(
                                                                            "Number of fixed broadband subscriptions "
                                                                            "per 100 inhabitants"
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        html.Li(
                                                            [
                                                                "Each country’s HCI is calculated using:",
                                                                html.Ul(
                                                                    [
                                                                        html.Li(
                                                                            "The adult literacy rate;",
                                                                        ),
                                                                        html.Li(
                                                                            "The combined primary, secondary and "
                                                                            "tertiary gross enrolment ratio;"
                                                                        ),
                                                                        html.Li(
                                                                            "Expected years of schooling;"
                                                                        ),
                                                                        html.Li(
                                                                            "Average years of schooling."
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                html.P(
                                                    [
                                                        "More information about the methodology can be found in ",
                                                        html.A(
                                                            "documents published directly by the UN",
                                                            href="https://www.un.org/development/desa/"
                                                                 "publications/publication/"
                                                                 "2020-united-nations-e-government-survey",
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
