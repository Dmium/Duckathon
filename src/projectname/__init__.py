from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__, static_folder="views", template_folder="views")
app.config.from_object('projectnameconfig')
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

import projectname.controllers.index
