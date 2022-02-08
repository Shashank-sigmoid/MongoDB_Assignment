from pprint import pprint
from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))

# Top n movies with highest imdb rating with votes >1000
pipeline = [
    {
        "$match": {"imdb.votes.$numberInt": {"$gt": "1000"}}
    },
    {
        "$sort": {"imdb.rating": -1}
    },
    {
        "$limit": n
    }
]

results = movies_collection.aggregate(pipeline)

for result in results:
    print(f"Movie Name: {result['title']} | Imdb rating: {result['imdb']['rating']['$numberInt']} "
          f"| Votes: {result['imdb']['votes']['$numberInt']}")