from pprint import pprint
from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))
year = input("Enter the year: ")

# Top n movies with highest imdb rating in a given year
pipeline = [
    {
        "$match": {"year.$numberInt": year}
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
    print(f"Movie Name: {result['title']} | Imdb rating: {result['imdb']['rating']['$numberInt']} | Year: {result['year']['$numberInt']}")