from bson import ObjectId
from mongodb_assignment.load_comments_data import comments_collection
from mongodb_assignment.load_movies_data import movies_collection

# Top 10 movies with most no. of comments
pipeline = [
    {
        "$group": {"_id": "$movie_id", "count": {"$sum": 1}}
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 10
    }
]

results = comments_collection.aggregate(pipeline)

for result in results:
    movie_name = {}
    movie_id = result['_id']['$oid']
    for movie in movies_collection.find():
        if movie['_id'] == ObjectId(movie_id):
            movie_name = movie['title']
            break

    print(f"Movie Name: {movie_name} | Comments count: {result['count']}")