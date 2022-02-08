from mongodb_assignment.db_connection import mydb
from bson import ObjectId
import json

users_collection = mydb['users']

users_data = []

# Reading the json data of file users
with open('Sample_data/users.json') as f:
    for obj in f:
        if obj:
            data = json.loads(obj)
            data["_id"] = ObjectId(data["_id"]["$oid"])
            users_data.append(data)

# users_collection.insert_many(users_data)

# Counting the no. of documents in the collection
print(users_collection.count_documents({}))

# to check if insert did work
for user in users_collection.find():
    if user['name'] == 'Shashank Dey':
        print(user)
        break


