from mongodb_assignment.load_comments_data import comments_collection

comment_sample = {'name': 'Shashank Dey',
                  'email': 'shashankdey@gmail.com',
                  'movie_id': {'$oid': '573a1390f29313caabcd418c'},
                  'text': 'The movie is superb, the plot is nice and the characters are so interesting. I loved it.',
                  'date': {'$date': {'$numberLong': '1332804016000'}}}

comment_samples = [
    {'name': 'Shreyansh Jain',
     'email': 'shreyanshjain@gmail.com',
     'movie_id': {'$oid': '573a1390f29313caabcd418c'},
     'text': 'The movie is nice, the plot is good too and the characters could have been better. I liked it though.',
     'date': {'$date': {'$numberLong': '1332804016000'}}},
    {'name': 'Lara Adams',
     'email': 'laraadams@gmail.com',
     'movie_id': {'$oid': '573a1390f29313caabcd418c'},
     'text': 'The movie is average, the plot could have been better. It is good for a one-time watch.',
     'date': {'$date': {'$numberLong': '1332804016000'}}},
]

# inserting one document in comments collection
comments_collection.insert_one(comment_sample)

# inserting multiple document in comments collection
comments_collection.insert_many(comment_samples)
