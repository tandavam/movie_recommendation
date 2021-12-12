from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    CORS(app)
    with app.app_context():
        from movie_recommendation.content_based_filtering import movie_recommendation_blueprint
        from movie_recommendation.utils.exception import catch_exception
        from movie_recommendation.utils.helpers import ResponseError
        app.register_error_handler(ResponseError, catch_exception)
        app.register_error_handler(Exception, catch_exception)
        app.register_blueprint(movie_recommendation_blueprint, url_prefix="/recommendations")
        return app
