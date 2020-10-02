from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie
import json
import time


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
   'host': 'mongodb://localhost/movie-bag'
}


initialize_db(app)

@app.route('/movies')
def get_movies():
    import pdb;pdb.set_trace()
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    # import pdb;pdb.set_trace()
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200


@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200


@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200

app.run()