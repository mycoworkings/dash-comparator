import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from coworkings import CW1, CW2

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(
                src=app.get_asset_url("godyuela.jpg"),
                id="plotly-image",
                style={
                    "height": "60px",
                    "width": "auto",
                    "margin-bottom": "25px",
                },
            )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H2(
                    "COMPARADOR",
                    style={"margin-bottom": "0px"},
                ),
            ])
        ],
            className="one-half column",
            id="title",
        ),
        html.Div([
            html.A(
                html.Button("Learn More", id="learn-more-button"),
                href="https://plot.ly/dash/pricing/",
            )
        ],
            className="one-third column",
            id="button",
        ),
    ],
        id="header",
        className="row flex-display",
        style={"margin-bottom": "25px"},
    ),

    html.Div([
        html.Div(
            dcc.Dropdown(
                id='cw1',
                options=[{'label': f'{CW1.get("name")}', 'value': f'{CW1.get("name")}'},
                         {'label': f'{CW2.get("name")}', 'value': f'{CW2.get("name")}'}],
                value=f'{CW1.get("name")}',
            ), style={'width': '49%', 'display': 'inline-block'},
        ),
        html.Div(
            dcc.Dropdown(
                id='cw2',
                options=[{'label': f'{CW1.get("name")}', 'value': f'{CW1.get("name")}'},
                         {'label': f'{CW2.get("name")}', 'value': f'{CW2.get("name")}'}],
                value=f'{CW2.get("name")}',
            ), style={'width': '49%', 'float': 'right', 'display': 'inline-block'},
        )
    ]),

    html.Div([
        html.Div([
            html.H3(
                "Servicios",
                style={"margin-bottom": "0px"},
            ),
        ])
    ]),

    html.Div([
        html.Div(
            [dcc.Graph(id="main_graph")],
        ),
        html.Div(
            [dcc.Graph(id="individual_graph")],
        ),
    ],
        className="row flex-display",
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
