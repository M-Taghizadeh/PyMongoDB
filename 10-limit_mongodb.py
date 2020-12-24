import pymongo

# Connect to Dataase
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyGram"]
coll = db["users"]

docs = coll.find().limit(5)
for doc in docs:
    print(doc)

# skip
docs = coll.find().skip(10).limit(5)
for doc in docs:
    print(doc)

# Pagination
page = 2
paginate_by = 5
docs = coll.find().skip(paginate_by * (page-1)).limit(paginate_by)
for doc in docs:
    print(doc)
