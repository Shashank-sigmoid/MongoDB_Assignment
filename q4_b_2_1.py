from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))

# Top n directors with maximum no. of movies
pipeline = [
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

for result in results:
    if isinstance(result['_id'], list):
        print(f"Director Name: {result['_id'][0]} | Movies count: {result['count']}")