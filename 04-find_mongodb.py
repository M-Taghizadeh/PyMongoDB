import pymongo

# Connect to Dataase
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyGram"]
coll = db["users"]

# # Find One
print(coll.find_one())
print(type(coll.find_one())) # <class 'dict'>

# Find All 
for doc in coll.find():
    print(doc)

# Return Only Some Fields
for doc in coll.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(doc)

for doc in coll.find({},{ "address": 0 }):
    print(doc)

# Count of docs
print(coll.find().count())
