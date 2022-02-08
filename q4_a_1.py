from mongodb_assignment.load_comments_data import comments_collection

# Top 10 users with most no. of comments
pipeline = [
    {
        "$group": {"_id": "$name", "count": {"$sum": 1}}
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
    print(f"Username: {result['_id']} | Comments count: {result['count']}")