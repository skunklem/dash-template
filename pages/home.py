#!/usr/bin/env python3
"""A main landing page with plots that provide useful overviews"""
# Import necessary libraries 
import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Project overview", path="/",order=0)

print("getting home page layout")

# page markdown
page_markdown = """
**Welcome to the home page!**

We hope you love it here.

## Updating content
You can edit this page in `pages/home.py`
"""

# page layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Label(html.H3("Home page",style={"color":"success"}),id="list-label"
                    # className="m-8"
                    ),
            dcc.Markdown(page_markdown,id="home-page-markdown"),
        ]),
        # dbc.Col([
        #     dbc.Button("Refresh", id="project-refresh", 
        #             #    className="me-1",
        #                     n_clicks=0),
        # ], 
        # # style={'padding': 10, 'flex': 1}
        # )
    ],
    ),
    # dmc.Alert(children="Rando alert",color="violet")
])