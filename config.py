SECRET_KEY = 'mysecretkey'
import os
APP_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:///{APP_DIR}/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PAGES_FOLDER = f"{APP_DIR}/pages"
PORT = '5000'

# host name for local testing
# enables testing on other devices (phones) on the same network
# found via: `hostname -I`
HOST = "0.0.0.0"