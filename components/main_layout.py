import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
# from dash_iconify import DashIconify
# from dnd.components.main_layout_callbacks import *

# styling:
url_theme1 = dbc.themes.BOOTSTRAP
url_theme2 = dbc.themes.CYBORG
# template_theme1 = "bootstrap" # useful if changing theme of plotly figures
# template_theme2 = "cyborg" # useful if changing theme of plotly figures

# # NOTE: tesing only (for local install)
# url_theme1 = 'assets/bootstrap.min.css'
# url_theme2 = 'assets/cyborg_bootstrap.min.css'

# # NOTE: find a place for this
# # app.css.config.serve_locally = True
# # app.scripts.config.serve_locally = True

notices = dbc.Row(id='top-alert-div')

def listPages():
    "converts items from pages to list of NavItems"
    # return [
    #     dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))
    #     for page in dash.page_registry.values()
    #     if page["name"] != "template"
    #     ]
    return [
        dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))
        for page in dash.page_registry.values()
        if page.get("location") == "navbar"
        ]

def get_themeSwitch():
    return ThemeSwitchAIO(
        aio_id="theme",
        # icons={"left": "bi bi-moon", "right": "bi bi-sun"},
        # icons={"left": DashIconify(icon="bi:moon", width=30), "right": DashIconify(icon="bi:sun", width=30)}, # bad
        themes=[url_theme1, url_theme2],
        )

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

from flask import Flask
from database.model import db
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, PAGES_FOLDER
from pathlib import Path

def layout():
    return html.Div([
        dbc.NavbarSimple(
            id="navbar",
            children=listPages() + [get_themeSwitch()],
            brand="Some app (change name in main_layout.py)",
            brand_href="/",
            ),
        dbc.Container([
            # dcc.Location(id='url'),
            dbc.Row([
                dbc.Col([
                    notices,
                    dash.page_container,
                    # html.Div(id='page-content', children=[],),
                ])
            ]),
        ],
        className="m-4",
        # fluid=True,
        ),
    ])

def getDashApp(name,server=None):
    """returns dash app"""

    print("preparing dash app")
    app = Dash(name,
                use_pages=True,
                external_stylesheets=[
                    # 'https://codepen.io/chriddyp/pen/bWLwgP.css',
                    dbc_css,
                    dbc.themes.BOOTSTRAP
                ],
                # url_base_pathname='somename/',
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True,
                # pages_folder=PAGES_FOLDER,
                # server=server,
            )
    app.layout = layout()
    server = app.server
    server.config['SECRET_KEY'] = SECRET_KEY
    server.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(server)
    return app
