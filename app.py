# -*- coding: utf-8 -*-

import dash
from dash import dcc
from dash import html
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
                                                dcc.Markdown('$${MII=({TEC\over{APC}}+PEC})\\times \sum_{i=1}^{num_{'
                                                             'SL}}\\times (SLECI\\times SSL)$$', mathjax=True),
                                                html.H6(
                                                    "The components of the index are defined like so: "
                                                ),
                                                html.Ul(
                                                    [
                                                        html.Li(
                                                            [
                                                                '𝑀𝐼𝐼=𝑀𝑖𝑙𝑒𝑒 𝐼𝑚𝑝𝑎𝑐𝑡 𝐼𝑛𝑑𝑒𝑥 (𝑖𝑛  (𝑔𝐶𝑂^2 𝑒𝑞)/𝑘𝑊ℎ)'
                                                            ]
                                                        ),
                                                        html.Li(
                                                            '𝑇𝐸𝐶=𝑇𝑟𝑎𝑖𝑛𝑖𝑛𝑔 𝐸𝑛𝑒𝑟𝑔𝑦 𝐶𝑜𝑠𝑡 (𝑖𝑛 𝑘𝑊ℎ)'
                                                        ),
                                                        html.Li(
                                                            '𝐴𝑃𝐶=𝐴𝑚𝑚𝑜𝑟𝑡𝑖𝑧𝑎𝑡𝑖𝑜𝑛 𝑃𝑟𝑜𝑚𝑝𝑡 𝐶𝑜𝑢𝑛𝑡 (𝑖𝑛 𝑢𝑛𝑖𝑡𝑠)'
                                                        ),
                                                        html.Li(
                                                            '𝑃𝐸𝐶=𝑃𝑟𝑜𝑚𝑝𝑡 𝐸𝑛𝑒𝑟𝑔𝑦 𝐶𝑜𝑠𝑡 (𝑖𝑛 𝑘𝑊ℎ)'
                                                        ),
                                                        html.Li(
                                                            '𝑆𝐿𝐸𝐶𝐼=𝑆𝑒𝑟𝑣𝑒𝑟 𝐿𝑜𝑐𝑎𝑡𝑖𝑜𝑛 𝐸𝑛𝑒𝑟𝑔𝑦 𝐼𝑛𝑡𝑒𝑛𝑠𝑖𝑡𝑦 (𝑖𝑛  (𝑔𝐶𝑂^2 𝑒𝑞)/𝑘𝑊ℎ)'
                                                        ),
                                                        html.Li(
                                                            '𝑆𝑆𝐿=𝑆ℎ𝑎𝑟𝑒 𝑜𝑓 𝑆𝑒𝑟𝑣𝑒𝑟𝑠 𝑖𝑛 𝐿𝑜𝑐𝑎𝑡𝑖𝑜𝑛 (𝑖𝑛 %)'
                                                        ),
                                                        html.Li(
                                                            '𝑁𝑢𝑚𝑆𝐿=𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑆𝑒𝑟𝑣𝑒𝑟 𝐿𝑜𝑐𝑎𝑡𝑖𝑜𝑛𝑠'
                                                        ),
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
