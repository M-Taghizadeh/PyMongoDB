import pymongo

# Connect to Dataase
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyGram"]
coll = db["users"]

# Sort the Result Ascending 
docs = coll.find().sort("name")
for doc in docs:
    print(doc)

# Sort the Result Descending
docs = coll.find().sort("name", -1)
for doc in docs:
    print(doc)