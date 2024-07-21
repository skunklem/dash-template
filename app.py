#!/usr/bin/env python3

import os
import dash
from dash import html
import dash_bootstrap_components as dbc

# local imports
# from components.main_layout import getApp
from database.model import db
from components.main_layout import getDashApp #,listPages,themeSwitch,notices
# from database.edit import insert_test_data

def main(app, server):
    print("Starting app...")
    server.run(debug=True)
    return server

app = getDashApp(name="whiskyface",server=None)
application = app.server
if __name__ == '__main__':
    main(app, app.server)

# # app, server = getApp(__name__)
# def startApp():
#     # flask_app = Flask(__name__)
#     app, server = getApp(__name__)

#     db.init_app(server)
#     with server.app_context():
#         db.create_all()
#         insert_test_data()
#     # from __init__ import app, server, db
#     # from database.model import db
#     # db = SQLAlchemy(server)
#     return app,server

# if __name__ == '__main__':
#     app,server = startApp()
#     main(app, server)
