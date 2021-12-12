import pandas as pd
import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval


class ContentBasedFiltering:
    def __init__(self):
        self.credits_dataset_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../datasets"
                                                                                             "/tmdb_5000_credits.csv")
        self.movies_dataset_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../datasets"
                                                                                            "/tmdb_5000_movies.csv")
        self.credits_dataset = pd.read_csv(self.credits_dataset_path)
        self.movies_dataset = pd.read_csv(self.movies_dataset_path)
        self.credits_dataset.columns = ['id', 'tittle', 'cast', 'crew']
        self.movies_dataset = self.movies_dataset.merge(self.credits_dataset, on="id")
        self.features = ["cast", "crew", "keywords", "genres"]

    def get_recommendations(self, title, cosine_sim, indices):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movies_indices = [ind[0] for ind in sim_scores]
        movies = self.movies_dataset["title"].iloc[movies_indices]
        return movies.values

    @staticmethod
    def clean_data(data):
        if isinstance(data, list):
            return [str.lower(" ".join(row.split())) for row in data]
        elif isinstance(data, str):
            return str.lower(" ".join(data.split()))
        else:
            return ""

    @staticmethod
    def get_directors(movies):
        for data in movies:
            if data['job'] == "Director":
                return data['name']
        return np.nan

    @staticmethod
    def get_top_list(information):
        if isinstance(information, list):
            names = [info["name"] for info in information]
            if len(names):
                names = names[:3]
            return names

        return list()

    @staticmethod
    def create_soup(data):
        return ' '.join(data['keywords']) + ' ' + ' '.join(data['cast']) + ' ' + data['director'] + ' ' + ' '.join(
            data['genres'])

    def get_the_recommended_movies(self, movie_name):

        for feature in self.features:
            self.movies_dataset[feature] = self.movies_dataset[feature].apply(literal_eval)

        self.movies_dataset["director"] = self.movies_dataset["crew"].apply(self.get_directors)

        features = ["cast", "keywords", "genres"]
        for feature in features:
            self.movies_dataset[feature] = self.movies_dataset[feature].apply(self.get_top_list)

        self.movies_dataset[['title', 'cast', 'director', 'keywords', 'genres']].head()

        features = ['cast', 'keywords', 'director', 'genres']
        for feature in features:
            self.movies_dataset[feature] = self.movies_dataset[feature].apply(self.clean_data)

        self.movies_dataset["soup"] = self.movies_dataset.apply(self.create_soup, axis=1)

        count_vectorizer = CountVectorizer(stop_words="english")
        count_matrix = count_vectorizer.fit_transform(self.movies_dataset["soup"])

        cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

        self.movies_dataset = self.movies_dataset.reset_index()
        indices = pd.Series(self.movies_dataset.index, index=self.movies_dataset['title'])
        movies = self.get_recommendations(movie_name['movie_name'], cosine_sim2, indices)
        # import pdb;pdb.set_trace()
        return {
            "movies": list(movies)
        }


