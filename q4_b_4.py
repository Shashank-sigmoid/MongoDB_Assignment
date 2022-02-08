from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))

# Extracting all genres first
pipeline = [
    {
        "$unwind": "$genres"
    },
    {
        "$group": {"_id": "$genres", "count": {"$sum": 1}}
    }
]

results = movies_collection.aggregate(pipeline)

genres = []
for result in results:
    genres.append(result['_id'])

# Top n movies for each genre
for genre in genres:
    new_pipeline = [
        {
            "$match": {"genres": genre}
        },
        {
            "$sort": {"imdb.rating": -1}
        },
        {
            "$limit": n
        }
    ]
    new_results = movies_collection.aggregate(new_pipeline)
    print(f"Genre: {genre}")
    for new_result in new_results:
        print(f"Movie name: {new_result['title']} | Imdb rating: {new_result['imdb']['rating']}")

    print()