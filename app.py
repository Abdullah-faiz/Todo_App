import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

from api.views import api_blueprint
from db import db

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(api_blueprint)

app.config.from_object(os.environ.get("APP_SETTINGS"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

if __name__ == '__main__':
    app.run(debug=True)
