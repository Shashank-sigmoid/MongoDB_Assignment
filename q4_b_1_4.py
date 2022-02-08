import re
from pprint import pprint
from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))
pattern = input("Enter a pattern: ")
srch = re.compile(pattern, re.IGNORECASE)

# Top n movies with highest imdb rating with votes >1000
pipeline = [
    {
        "$match": {"title": srch}
    },
    {
        "$sort": {"tomatoes.rating": -1}
    },
    {
        "$limit": n
    }
]

results = movies_collection.aggregate(pipeline)

# print(results)
for result in results:
    print(f"Movie Name: {result['title']} | Imdb rating: {result['tomatoes']['viewer']['rating']}")