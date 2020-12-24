import pymongo # pip install pymongo

# Connect to Dataase
myclient = pymongo.MongoClient("mongodb://localhost:27017")
db = myclient["University2"]

# show dbs
print(myclient.list_database_names())

# check database if exists
if "db_name" in myclient.list_database_names():
    print("The database exists.")