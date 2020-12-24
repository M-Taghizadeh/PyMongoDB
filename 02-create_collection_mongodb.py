import pymongo

# Connect to Dataase
myclient = pymongo.MongoClient("mongodb://localhost:27017")
db = myclient["PyGram"]
coll = db["users"]

# show collections list
coll_list = db.list_collection_names()
print(coll_list)