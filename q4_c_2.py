from mongodb_assignment.load_theaters_data import theaters_collection

lat = float(input("Enter the latitude: "))
lng = float(input("Enter the longitude: "))

theaters_collection.create_index({"location": "2dsphere"})
theaters_collection.find().sort("_id", -1)

# Top 10 closest theaters to a given coordinates
pipeline = [
    {
        "$geoNear": {"near": {"type": "Point", "coordinates": [lat, lng]},
                     "maxDistance": 1000000, "distanceField": "distance"}
    },
    {
        "$project": {"location.address.city": 1, "_id": 0, "location.geo.coordinates": 1}
    },
    {
        "$limit": 10
    }
]

results = theaters_collection.aggregate(pipeline)
for result in results:
    print(result)
