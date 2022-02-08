from mongodb_assignment.load_movies_data import movies_collection

movie_sample = {'plot': 'Two teenagers share a profound, magical connection upon discovering they are swapping bodies.',
                'genres': ['Short'],
                'runtime': {'$numberInt': '1'},
                'cast': ['Taki Tachibana', 'Mitsuha Miyamizu'],
                'num_mflix_comments': {'$numberInt': '1'},
                'title': 'Kimi No Na Wa',
                'countries': ['Japan'],
                'released': {'$date': {'$numberLong': '-2418768000000'}},
                'directors': ['Makoto Shinkai'],
                'rated': 'UNRATED', 'awards': {'wins': {'$numberInt': '1'}, 'nominations': {'$numberInt': '0'},
                                               'text': '1 win.'},
                'lastupdated': '2015-08-26 00:03:50.133000000',
                'year': {'$numberInt': '2016'},
                'imdb': {'rating': {'$numberDouble': '8.4'},
                         'votes': {'$numberInt': '1189'},
                         'id': {'$numberInt': '5'}},
                'type': 'movie',
                'tomatoes': {'viewer': {'rating': {'$numberInt': '3'},
                                        'numReviews': {'$numberInt': '184'},
                                        'meter': {'$numberInt': '32'}},
                             'lastUpdated': {'$date': {'$numberLong': '1435516449000'}}}}

movie_samples = [
    {'plot': 'High-school boy Hodaka Morishima runs away from his troubled rural home '
             'to Tokyo and befriends an orphan girl who can manipulate the weather.',
     'genres': ['Short'],
     'runtime': {'$numberInt': '1'},
     'cast': ['Hodaka', 'Hina'],
     'num_mflix_comments': {'$numberInt': '1'},
     'title': 'Tenki No Ko',
     'countries': ['Japan'],
     'released': {'$date': {'$numberLong': '-2418768000000'}},
     'directors': ['Makoto Shinkai'],
     'rated': 'UNRATED', 'awards': {'wins': {'$numberInt': '1'}, 'nominations': {'$numberInt': '0'},
                                    'text': '1 win.'},
     'lastupdated': '2015-08-26 00:03:50.133000000',
     'year': {'$numberInt': '2019'},
     'imdb': {'rating': {'$numberDouble': '7.5'},
              'votes': {'$numberInt': '1189'},
              'id': {'$numberInt': '5'}},
     'type': 'movie',
     'tomatoes': {'viewer': {'rating': {'$numberInt': '3'},
                             'numReviews': {'$numberInt': '184'},
                             'meter': {'$numberInt': '32'}},
                  'lastUpdated': {'$date': {'$numberLong': '1435516449000'}}}},

    {
        'plot': ' The mission is to defeat a demon who has been tormenting people and '
                'killing the demon slayers who oppose it.',
        'genres': ['Short'],
        'runtime': {'$numberInt': '1'},
        'cast': ['Tanjiro', 'Nezuko'],
        'num_mflix_comments': {'$numberInt': '1'},
        'title': 'Demon Slayer',
        'countries': ['Japan'],
        'released': {'$date': {'$numberLong': '-2418768000000'}},
        'directors': ['Haruo Sotozaki'],
        'rated': 'UNRATED', 'awards': {'wins': {'$numberInt': '1'}, 'nominations': {'$numberInt': '0'},
                                       'text': '1 win.'},
        'lastupdated': '2015-08-26 00:03:50.133000000',
        'year': {'$numberInt': '2020'},
        'imdb': {'rating': {'$numberDouble': '8.4'},
                 'votes': {'$numberInt': '1189'},
                 'id': {'$numberInt': '5'}},
        'type': 'movie',
        'tomatoes': {'viewer': {'rating': {'$numberInt': '3'},
                                'numReviews': {'$numberInt': '184'},
                                'meter': {'$numberInt': '32'}},
                     'lastUpdated': {'$date': {'$numberLong': '1435516449000'}}}}
]

# inserting one document in movies collection
movies_collection.insert_one(movie_sample)

# inserting multiple documents in movies collection
movies_collection.insert_many(movie_samples)
