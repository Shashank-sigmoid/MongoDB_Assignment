from mongodb_assignment.load_users_data import users_collection

user_sample = {
    'name': 'Shashank Dey',
    'email': 'shashankdey@gmail.com',
    'password': '1234'
}

user_samples = [
    {
        'name': 'Shreyansh Jain',
        'email': 'shreyanshjain@gmail.com',
        'password': '6789'
    },
    {
        'name': 'Lara Adams',
        'email': 'laraadams@gmail.com',
        'password': '2345'
    }
]

# inserting one document in users collection
users_collection.insert_one(user_sample)

# inserting multiple documents in users collection
users_collection.insert_many(user_samples)
