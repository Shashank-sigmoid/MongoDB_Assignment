from mongodb_assignment.load_movies_data import movies_collection

n = int(input("Enter a number: "))
year = input("Enter the year: ")

# Top n actors with maximum no. of movies in a given year
pipeline = [
    {
        "$unwind": "$cast"
    },
    {
        "$match": {"year.$numberInt": year}
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

print(f"Calendar year: {year}")
for result in results:
    print(f"Actor Name: {result['_id']} | Movies count: {result['count']}")