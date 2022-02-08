from pprint import pprint

from mongodb_assignment.db_connection import mydb
from bson import ObjectId
import json

movies_collection = mydb['movies']

movies_data = []

# Reading the json data of file movies
with open('Sample_data/movies.json') as f:
    for obj in f:
        if obj:
            data = json.loads(obj)
            data["_id"] = ObjectId(data["_id"]["$oid"])
            movies_data.append(data)

# movies_collection.insert_many(movies_data)

# Counting the no. of documents in the collection
print(movies_collection.count_documents({}))

# To see the structure of the document
pprint(movies_collection.find_one())

# to check if insert did work
for movie in movies_collection.find():
    if movie['title'] == 'Demon Slayer':
        print(movie['imdb'])
        break

