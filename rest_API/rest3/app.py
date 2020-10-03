from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
from database.db import initialize_db

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)

initialize_routes(api)

app.run()
