from mongodb_assignment.load_theaters_data import theaters_collection

theater_sample = {'theaterId': {'$numberInt': '100001'},
                  'location': {'address': {'street1': '340 B-Town Hall',
                                           'city': 'Las Vegas', 'state': 'MN', 'zipcode': '55125'},
                               'geo': {'type': 'Point', 'coordinates': [{'$numberDouble': '-93.24565'},
                                                                        {'$numberDouble': '44.85466'}]}}}

theater_samples = [
    {'theaterId': {'$numberInt': '100002'},
     'location': {'address': {'street1': '789 Bakers-Street',
                              'city': 'Los Angeles', 'state': 'MN', 'zipcode': '55345'},
                  'geo': {'type': 'Point', 'coordinates': [{'$numberDouble': '-93.24565'},
                                                           {'$numberDouble': '44.85466'}]}}},
    {'theaterId': {'$numberInt': '100003'},
     'location': {'address': {'street1': '456 Landmines Escape',
                              'city': 'San Francisco', 'state': 'MN', 'zipcode': '55785'},
                  'geo': {'type': 'Point', 'coordinates': [{'$numberDouble': '-93.24565'},
                                                           {'$numberDouble': '44.85466'}]}}}
]

# inserting one document in theaters collection
theaters_collection.insert_one(theater_sample)

# inserting multiple documents in theaters collection
theaters_collection.insert_many(theater_samples)
