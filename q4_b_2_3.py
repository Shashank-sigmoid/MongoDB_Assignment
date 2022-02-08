from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))
genres = input("Enter the genre: ")

# Top n directors with maximum no. of movies for a given genre
pipeline = [
    {
        "$match": {"genres": {"$in": [genres.title()]}}
    },
    {
        "$group": {"_id": "$directors", "count": {"$sum": 1}}
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": n + 1
    }
]

results = movies_collection.aggregate(pipeline)

print(f"Genre: {genres.title()}")
for result in results:
    if isinstance(result['_id'], list):
        print(f"Director Name: {result['_id'][0]} | Movies count: {result['count']}")
