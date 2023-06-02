from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


def get_main_comparison():
    return html.Div(
                        [
                            html.Div(
                                children=[
                                    html.Div(
                                        [
                                            html.H3(
                                                "AI model comparison"
                                            ),
                                            html.P(
                                                "Here is the comparison of benchmarked models:"
                                            ),
                                            html.Div(
                                                [
                                                    get_main_chart()
                                                ],
                                                id="main_graph"
                                            )
                                        ]
                                    )
                                ],
                                id="main_chart_container",
                                className="pretty_container twelve columns"
                            ),
                        ],
                        className="content_holder row twelve columns"
                    )
def get_main_chart():
    # Load data from CSV file
    df = pd.read_csv('data/energy_emissions_california.csv')

    # Add data - chatgpt
    # Load
    df_chatgpt=pd.read_csv('data/chatgpt_pie.csv')




    fig = px.line(df, x="date", y="value est", width=800) #color='country'
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20)
    )

    #darkmode adjustment
    fig.layout.paper_bgcolor='#CCC'

    # Return chart
    return dcc.Graph(figure=fig)

def get_methodology():
    return html.Div(
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
                                id="methods_description",
                                className="pretty_container description twelve columns flex-display"
                            ),
                        ],
                        className="content_holder row twelve columns flex-display"
                    )

def get_facts_module():
    return html.Div(
                        children=[
                            html.Div(
                                [
                                    html.H3(
                                        "Fun Fax"
                                    ),
                                    html.P(
                                        "TBD"
                                    ),
                                ]
                            )
                        ],
                        id="facts_module",
                        className="pretty_container description twelve columns flex-display"
                    )

def get_pie_module():
    return html.Div(
                        children=[
                            html.Div(
                                [
                                    html.H3(
                                        "Graph"
                                    ),
                                    get_piechart()
                                ]
                            )
                        ],
                        id="pie_graph",
                        className="pretty_container ten columns",
                    )

def get_piechart(filename='data/chatgpt_pie.csv'):
    # Load data from CSV file
    data = pd.read_csv(filename)

    # Calculate the count of each category in the data
    category_counts = data['Type'].value_counts()

    # Create a pie chart using Plotly Express
    fig = px.pie(data_frame=data, names=data['Type'], values=data['Percentage'], title='Category Distribution')

    #darkmode adjustment
    fig.layout.paper_bgcolor='#CCC'
    # Return chart
    return dcc.Graph(figure=fig)
