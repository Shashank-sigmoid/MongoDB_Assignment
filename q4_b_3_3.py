from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))
genres = input("Enter the genre: ")

# Top n actors with maximum no. of movies for a given genre
pipeline = [
    {
        "$unwind": "$cast"
    },
    {
        "$match": {"genres": {"$in": [genres.title()]}}
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

print(f"Genre: {genres.title()}")
for result in results:
    print(f"Actor Name: {result['_id']} | Movies count: {result['count']}")