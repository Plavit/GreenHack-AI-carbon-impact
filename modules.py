from dash import dcc
from dash import html

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
                                    html.P(
                                        "TBD "
                                    ),
                                ]
                            )
                        ],
                        id="pie_graph",
                        className="pretty_container description twelve columns flex-display"
                    )