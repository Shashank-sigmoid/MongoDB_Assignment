from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))

# Top n movies with highest imdb rating
pipeline = [
    {
        "$sort": {"imdb.rating": -1}
    },
    {
        "$limit": n
    }
]

results = movies_collection.aggregate(pipeline)

for result in results:
    print(f"Movie name: {result['title']} | Imdb rating: {result['imdb']['rating']['$numberInt']}")

