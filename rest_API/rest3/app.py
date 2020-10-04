from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
from flask_mail import Mail

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
from resources.routes import initialize_routes

jwt = JWTManager(app)


MONGODB_SETTINGS = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)

initialize_routes(api)
