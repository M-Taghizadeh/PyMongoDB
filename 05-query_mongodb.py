import pymongo

# Connect to Dataase
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyGram"]
coll = db["users"]

# Filter the Result
query = {"address": "Park Lane 38"}
docs = coll.find(query)
for doc in docs:
    print(doc)

# Advanced Query
query = {"address": {"$gt": "S"}}
docs = coll.find(query)
for doc in docs:
    print(doc)

# Filter With Regular Expressions
query = {"address": {"$regex": "^S"}}
docs = coll.find(query)
for doc in docs:
    print(doc)