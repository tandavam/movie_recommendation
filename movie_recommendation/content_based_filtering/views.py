from .handlers import ContentBasedFiltering
from flask import Blueprint, jsonify, request

movie_recommendation_blueprint = Blueprint("movie_recommendation_blueprint", __name__)


@movie_recommendation_blueprint.route("/movies", methods=["POST"])
def movies():
    return jsonify(ContentBasedFiltering().get_the_recommended_movies(request.json))
