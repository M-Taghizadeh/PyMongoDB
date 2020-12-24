import pymongo

# Connect to Dataase
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyGram"]
coll = db["users"]

# Update Collection
query = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}
coll.update_one(query, new_values)

for doc in coll.find():
    print(doc)

# Update Many
query = {"address": {"$regex": "^A"}}
new_values = {"$set": {"name": "Minnie"}}
result = coll.update_many(query, new_values)
print(result.modified_count, "documents updated.")
