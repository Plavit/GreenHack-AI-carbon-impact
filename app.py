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

from modules import get_methodology, get_facts_module, get_pie_module, get_main_comparison, \
    get_carbot_estimates_2_module, get_carbon_estimates_module, get_top_module

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
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
        get_top_module(),

        html.Div(
            [
                html.Div(
                    [
                        get_main_comparison(),
                        html.Div(
                            [
                                get_carbot_estimates_2_module(),
                                get_pie_module()
                            ],
                            className="content_holder row 2 columns flex-display top",
                            style={'columnCount': 2, 'display': 'flex', "flex-direction": "row"}
                        ),
                        html.Div(
                            [
                                get_facts_module(),
                                get_methodology(),
                            ],
                            className="content_holder row 2 columns flex-display bottom",
                            style={'columnCount': 2, 'display': 'flex', "flex-direction": "column"}
                        )
                    ],
                    className="pretty_container_bg twelve columns",
                    style={'columnCount': 2, 'display': 'flex', "flex-direction": "column", 'justifyContent': 'space-between'}
                ),
            ],
            className="row flex-display",
            style={'columnCount': 1, 'rowCount': 3, "display": "flex", "flex-direction": "column", 'justifyContent': 'space-between'},
        ),
    ],
    id="mainContainer",
    style={'columnCount': 1, "display": "flex", "flex-direction": "column", 'justifyContent': 'space-between'},
)

app.title = 'GreenHack'


if __name__ == '__main__':
    app.run_server(debug=True)
