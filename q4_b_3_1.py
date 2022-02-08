from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))

# Top n actors with maximum no. of movies
pipeline = [
    {
        "$unwind": "$cast"
    },
    {
        "$group": {"_id": "$cast", "count": {"$sum": 1}}
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": n
    }
]

results = movies_collection.aggregate(pipeline)

for result in results:
    print(f"Actor Name: {result['_id']} | Movies count: {result['count']}")