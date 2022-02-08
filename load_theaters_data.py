from pprint import pprint

from mongodb_assignment.db_connection import mydb
from bson import ObjectId
import json

theaters_collection = mydb['theaters']

theaters_data = []

# Reading the json data of file theaters
with open('Sample_data/theaters.json') as f:
    for obj in f:
        if obj:
            data = json.loads(obj)
            data["_id"] = ObjectId(data["_id"]["$oid"])
            theaters_data.append(data)

# theaters_collection.insert_many(theaters_data)

# Counting the no. of documents in the collection
print(theaters_collection.count_documents({}))

# To see the structure of the document
pprint(theaters_collection.find_one())

# to check if insert did work
for theater in theaters_collection.find():
    if theater['theaterId'] == {'$numberInt': '100002'}:
        print(theater)
        break

