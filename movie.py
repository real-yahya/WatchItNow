import requests
import json
import random


class Movie:

    API_URL = 'http://www.omdbapi.com/'
    API_KEY = '6897961'
    title = None
    year = None
    rated = None
    released = None
    runtime = None
    genre = None
    director = None
    writer = None
    actors = None
    plot = None
    language = None
    country = None
    awards = None
    poster = None
    ratings = [
        {
            "Source": "Internet Movie Database",
            "Value": None
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": None
        },
        {
            "Source": "Metacritic",
            "Value": None
        }
    ]
    metaScore = None
    imdbRating = None
    imdbVotes = None
    imdbID = None
    type = None
    dvd = None
    boxOffice = None
    production = None
    website = None
    response = None

    def __init__(self, title):
        parameters = {
            'apikey': self.API_KEY,
            't': title
        }
        response = requests.get(self.API_URL, parameters)
        data = response.json()
        response.raise_for_status()
        self.title = data['Title']
        self.year = data['Year']
        self.rated = data['Rated']
        self.released = data['Released']
        self.runtime = data['Runtime']
        self.genre = data['Genre']
        self.director = data['Director']
        self.writer = data['Writer']
        self.actors = data['Actors']
        self.plot = data['Plot']
        self.language = data['Language']
        self.country = data['Country']
        self.awards = data['Awards']
        self.poster = data['Poster']
        self.ratings = [
            {
                "Source": "Internet Movie Database",
                "Value": data['Ratings'][0]['Value']
            },
            {
                "Source": "Rotten Tomatoes",
                "Value": data['Ratings'][1]['Value']
            },
            {
                "Source": "Metacritic",
                "Value": data['Ratings'][2]['Value']
            }
        ]
        self.metaScore = data['Metascore']
        self.imdbRating = data['imdbRating']
        self.imdbVotes = data['imdbVotes']
        self.imdbID = data['imdbID']
        self.type = data['Type']
        self.dvd = data['DVD']
        self.boxOffice = data['BoxOffice']
        self.production = data['Production']
        self.website = data['Website']
        self.response = data['Response']
