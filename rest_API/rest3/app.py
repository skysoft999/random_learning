from flask import Flask
from database.db import initialize_db
from resources.movie import movies

# from database.models import Movie
# import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)

app.register_blueprint(movies)

app.run()
