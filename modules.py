from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objs as go
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
                                                    # get_chart_2()
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
    df_chatgpt = pd.read_csv('data/chatgpt_pie.csv')

    #Cost in kWh
    query_cost = {"chatgpt": 0.00297,
                  "dalle2": 0.00014,
                  "stablediffusion": 0.00005,
                  }

    df['chatgpt_carbon_cost'] = df['value est'] * query_cost["chatgpt"]/df["chatgpt est"]
    df['dalle2_carbon_cost'] = df['value est'] * query_cost["dalle2"]/df["dalle est"]
    df['stabledif_carbon_cost'] = df['value est'] * query_cost["stablediffusion"]/df["stabdif est"]

    df = df.sort_values(by="date", ascending=True)

    fig = px.line(df, x="date", y=["chatgpt_carbon_cost","dalle2_carbon_cost","stabledif_carbon_cost"], width=800) #color='country'
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(tickformat='%b\n%Y')
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
                                    html.P("Training ChatGPT is a minor factor in the total energy consumption of a prompt, as its effect is diluted by the frequent and long-term use of the model."),
                                    html.P("Optimizing prompts can significantly reduce the carbon footprint of your queries. Here are some tips on how to optimize them:"),
                                    html.Ul(children=[
                                        html.Li([html.Strong("Use follow-up prompts:"), " Using follow-up prompts and natural language, you can have ChatGPT make changes to the tables it has drawn and even produce them in a standard format that can be understood by another program."], style={'margin': '10px'}),
                                        html.Li([html.Strong("Assign a role:"), " Assigning a role to ChatGPT can help you get the most out of it. Give it a level of expertise with which to view your prompt or question."], style={'margin': '10px'}),
                                        html.Li([html.Strong("Use prompting techniques:"), " There are several prompting techniques that can help you get more appropriate responses to your prompts. For example, you can assign ChatGPT a role, use multiple prompts, or use specific keywords in your prompts."], style={'margin': '10px'})
                                    ], style={'list-style-type': 'disc', 'margin': '20px'}),
                                ]
                            )
                        ],
                        id="facts_module",
                        className="pretty_container description twelve columns flex-display"
                    )


def get_carbon_estimates_module():
    return html.Div(children=[
                        html.Div(
                            [
                                html.H3(
                                    "Carbon emissions per Query"
                                ),
                                html.Ul(children=[
                                    html.Li([html.Strong("ChatGPT - regular prompt size:\t"), "1e-3"], style={'margin': '20px'}),
                                    html.Li([html.Strong("ChatGPT - small prompt size:\t"), "5e-4"], style={'margin': '20px'}),
                                    html.Li([html.Strong("Dalle-2:\t"), "5e-5"], style={'margin': '20px'}),
                                    html.Li([html.Strong("Stable Diffusion:\t"), "5e-5"], style={'margin': '20px'}),
                                ], style={'list-style-type': 'disc', 'margin': '20px'}),
                            ]
                        )
                    ],
                    id="carbons",
                    className="pretty_container ten columns",
                )


def get_carbot_estimates_2_module():
    return html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3("Carbon emissions per Query", style={'whiteSpace': 'nowrap'}),
                                html.Table(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Td("Model type", style={'padding': '20px', 'whiteSpace': 'nowrap', 'font-size': 22}),
                                                html.Td("C02 [Kg]", style={'padding': '20px', 'whiteSpace': 'nowrap', 'font-size': 22})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td(html.Strong("ChatGPT - regular prompt size:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("1e-3", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td(html.Strong("ChatGPT - small prompt size:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("5e-4", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td(html.Strong("Dalle-2:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("5e-5", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td(html.Strong("Stable Diffusion:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("5e-5", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        )
                                    ],
                                    # style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
                                )
                            ],
                            id="carbons",
                            className="pretty_container ten columns",
                            style={'min-width': '450px', 'justify-content': 'center', "align-items": "center"}
                        )
                    ],
                    className="main-container"
                )


def get_carbon_estimates_total_module():
    return html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H3("Carbon emissions Total"),
                                html.Table(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Td("Model type", style={'padding': '20px', 'whiteSpace': 'nowrap', 'font-size': 22}),
                                                html.Td("Total C02 [Tons]", style={'padding': '20px', 'whiteSpace': 'nowrap', 'font-size': 22}),
                                                html.Td("Kms of driving", style={'padding': '20px', 'whiteSpace': 'nowrap', 'font-size': 22}),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                # kms of driving
                                                html.Td(html.Strong("ChatGPT - regular prompt size:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td(1e-3 * 5434 * 10e3, style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("378,148,921", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                
                                                html.Td(html.Strong("ChatGPT - small prompt size:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td(5e-4 * 5434 * 10e3, style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("189,074,460", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td(html.Strong("Dalle-2:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td(round(5e-5 * 192 * 10e3,0), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("668,058", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td(html.Strong("Stable Diffusion:"), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td(round(5e-5 * 214 * 10e3,0), style={'padding': '20px', 'whiteSpace': 'nowrap'}),
                                                html.Td("744,606", style={'padding': '20px', 'whiteSpace': 'nowrap'})
                                            ]
                                        )
                                    ],
                                    # style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
                                )
                            ],
                            id="carbons",
                            className="pretty_container ten columns",
                            style={'min-width': '700px', 'justify-content': 'center', "align-items": "center"}
                        )
                    ],
                    className="main-container"
                )


def get_pie_module():
    return html.Div(children=[
                        html.Div(
                            [
                                html.H3(
                                    "Training vs prompt: Impact on CO2 emissions"
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

    # Create a pie chart using Plotly Express
    fig = px.pie(data_frame=data, names=data['Type'], values=data['Percentage'])

    # Set custom colors for the pie slices
    colors = ['#FF6384', '#36A2EB', '#FFCE56', '#33FF8F', '#A633FF']
    fig.update_traces(marker=dict(colors=colors))

    # Add a cool gradient background to the chart
    fig.update_layout(
        paper_bgcolor='#222',
        plot_bgcolor='#222',
        font=dict(color='#FFF', size=16),
        legend={
            'font': {
                'size': 18,
                'color': '#FFF'
            }
        },
    )

    # Return the chart as a dcc.Graph component
    return dcc.Graph(
        figure=fig,
        style={'height': '400px'}  # Adjust the height of the chart as desired
    )


def get_top_module():
    return html.Div(
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
        )