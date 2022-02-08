from mongodb_assignment.load_theaters_data import theaters_collection

# Top 10 closest theaters to a given coordinates
var = theaters_collection.aggregate([
    {
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [25.087626, 55.151134]
                },
            }
        }
    },
    {
        "$limit": 10
    }]
)
for result in var:
    print(result)