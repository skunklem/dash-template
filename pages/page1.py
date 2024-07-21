#!/usr/bin/env python3
"""A main landing page with plots that provide useful overviews"""
# Import necessary libraries 
import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Page 1", path="/page1",order=0, location='navbar')

print("getting page1 layout")

# page markdown
page_markdown = """
# Page 1
**Welcome to another page!**

We hope you love it here.

## Updating content
You can edit this page in `pages/page1.py`
"""

# page layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Markdown(page_markdown,id="home-page-markdown"),
        ]),
    ],
    ),
])