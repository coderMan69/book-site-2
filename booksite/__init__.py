from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resourses={r'/*': {'origins': '*'}})

db = SQLAlchemy()

from booksite import routes
