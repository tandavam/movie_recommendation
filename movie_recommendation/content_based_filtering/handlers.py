import pandas as pd
import os.path


class ContentBasedFiltering:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.credits_dataset_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../datasets"
                                                                                             "/tmdb_5000_credits.csv")
        self.movies_dataset_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../datasets"
                                                                                            "/tmdb_5000_movies.csv")
        self.credits_dataset = pd.read_csv(self.credits_dataset_path)
        self.movies_dataset = pd.read_csv(self.movies_dataset_path)

    def get_the_recommended_movies(self, movie_data):
        return {
            "status_id": self.credits_dataset
        }
