class ContentBasedFiltering:
    def __init__(self):
        self.credits_dataset = "../datasets/tmdb_5000_credits.csv"
        self.movies_dataset = "../datasets/tmdb_5000_movies.csv"

    def get_the_recommended_movies(self, movie_data):
        return {
            "status_id": self.credits_dataset
        }
