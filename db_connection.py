import pymongo as pm

# Establishing the connection with mongoDB server
try:
    client = pm.MongoClient('mongodb://127.0.0.1:27017')
except:
    print("Error in connection")

# Storing the database in variable mydb
mydb = client['mflix']
