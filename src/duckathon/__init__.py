from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder="views", template_folder="views")
app.config.from_object('duckathonconfig')
CORS(app)

import duckathon.controllers.index
