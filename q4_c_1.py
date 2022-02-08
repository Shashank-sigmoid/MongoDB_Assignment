from mongodb_assignment.load_theaters_data import theaters_collection

# Top 10 cities with maximum no. of theaters
pipeline = [
    {
        "$group": {"_id": "$location.address.city", "count": {"$sum": 1}}
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 10
    }
]

results = theaters_collection.aggregate(pipeline)

for result in results:
    print(f"City name: {result['_id']} | Theaters count: {result['count']}")