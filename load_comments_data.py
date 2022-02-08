from pprint import pprint
from mongodb_assignment.db_connection import mydb
from bson import ObjectId
import json

comments_collection = mydb['comments']

comments_data = []

# Reading the json data of file comments
with open('Sample_data/comments.json') as f:
    for obj in f:
        if obj:
            data = json.loads(obj)
            data["_id"] = ObjectId(data["_id"]["$oid"])
            comments_data.append(data)

# comments_collection.insert_many(comments_data)

# Counting the no. of documents in the collection
print(comments_collection.count_documents({}))

# To see the structure of the document
pprint(comments_collection.find_one())

# to check if insert did work
for comment in comments_collection.find():
    if comment['name'] == 'Shashank Dey':
        print(comment)
        break
