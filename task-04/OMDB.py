import os

import requests


def get_movie_info(movieTitle):
    url = 'http://www.omdbapi.com/?i=tt3896198&apikey=26033b3'
    api_key = os.getenv('26033b3')
    data = {'26033b3':api_key,'t':movieTitle}
    response = requests.get(url,data).json()

    if response.get("Response") != "True":
        return None

    movie_info = {}
    movie_info["title"] = response.get("Title")
    movie_info["Poster"] = response.get("Poster")
    movie_info["year"] = response.get("Year")
    movie_info["plot"] = response.get("Plot")
    movie_info["actors"] = response.get("Actors")
    movie_info["ratings"] = response.get("Ratings")
    movie_info["imdb_rating"] = response.get("imdbRating")


    return movie_info