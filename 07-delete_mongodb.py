import pymongo

# Connect to Dataase
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyGram"]
coll = db["users"]

# Delete Document
query = {"address": "Mountain 21"}
coll.delete_one(query)

# Delete Many Documents
query = {"address": {"$regex": "^S"}}
result = coll.delete_many(query)
print(result.deleted_count, " documents deleted.")

# Delete All Documents in a Collection
result = coll.delete_many({})
print(result.deleted_count, " documents deleted.")