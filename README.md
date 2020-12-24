# Get started with Mongo DB
MongoDB is a cross-platform document-oriented database program.
Classified as a NoSQL database program, MongoDB uses JSON-like documents

- [Installation](#Installation)
- [Create DataBase](#Create-DataBase)
- [Drop DataBase](#Drop-DataBase)
- [Create Collection](#Create-Collection)
- [Insert documents to collection](#Insert-documents-to-collection)
- [Find documents of collection](#Find-documents-of-collection)
- [Update documents](#Update-documents)
- [Replace documents](#Replace-documents)
- [Delete documents](#Delete-documents)
- [Counts of document](#Counts-of-document)
- [Sorting Document](#Sorting-Document)
- [Pagination : Limit and Skip commands](#Pagination:Limit-and-Skip-commands)
- [$inc $set $rename $unset](#$inc-$set-$rename-$unset)
- [$gt $lt $gte $lte](#$gt-$lt-$gte-$lte)
- [BulkWrite](#bulkWrite)
- [Search and Indexing in MongoDB](#Search-in-MongoDB(Indexing))
- [Backup and Restore Database](#Backup-and-Restore-Database)

### Installation
Download mongodb from here : https://www.mongodb.com/try/download/community


### Create-DataBase
```shell 
>>> show dbs # show all databases
>>> use db_name # create and switch to db
>>> db.db_name.insert({"name": "mohammad"})
```

### Drop-DataBase
```shell 
>>> use db_name
>>> db.dropDatabase()
resutl : { "dropped" : "db_name", "ok" : 1 }
>>> db.copyDatabase("old db name","new db name") # rename database
```

### Create-Collection
**Collection** in mongoDB == **Table** in relational database : Mongo uses collections instead of tables for store data <br>
**Document**  in mongoDB == **Record** in relational database : The collection includes documents

```shell 
>>> db.createCollection("coll_name")
>>> show collections
>>> db.coll_name.renameCollection("new_coll_name")
>>> db.coll_name.drop()
```

### Insert-documents-to-collection
```shell 
>>> use University
>>> db.createCollection("Students")
>>> db.Student.insertOne({"student_id":1, "name":"Mohammad Taghizadeh", "field":"comuter", "entry_date":1395})
>>> db.Student.insert([
        {"student_id":1, "name":"Mohammad Taghizadeh", "field":"comuter", "entry_date":1395},
        {"student_id":2, "name":"Ali", "field":"art", "entry_date":1399},
        {"student_id":3, "name":"Reza", "field":"comuter", "entry_date":1390},
    ])
```

### Find-documents-of-collection
```shell 
>>> db.Student.findOne({"name":"Mohammad"})
>>> db.Student.find() # find all of docs
>>> db.Student.find().pretty() 
>>> db.Student.find({"name":"Mohammad"}).pretty() 

```

### Update-documents
```shell 
>>> db.Student.update({"_id" : ObjectId("5fe490ad2b7f96f9a5f8249b")}, 
    {
        $set: {
            "name": "Ahmad"
        }
    })

>>> db.Student.update({"name" : "Mohammad")}, {
        $set: {"name": "Ahmad"}
    })

>>> db.Student.updateMany({name : "Mohammad")}, {
        $set: {"create_date": Date()}
    })

>>> db.Student.updateMany({}, {
        $set: {"create_time": Date()}
    })
```

### Replace-documents 
```shell 
>>>  db.Student.replaceOne({name: "Mohammad Taghizadeh"}, {fullname: "MTaghizadeh", age: 23})
```

### Delete-documents
```shell 
>>> db.Student.deleteOne({name: "Mohammad"})
>>> db.Student.deleteMany({name: "Mohammad"})
```

### Counts-of-document
```shell 
>>> db.Student.find().count()
>>> db.Student.find({name: "Mohamamd"}).count()
```

### Sorting-Document
```shell   
>>> db.Student.find().sort({student_id:  1}).pretty() # 1 : acs
>>> db.Student.find().sort({student_id: -1}).pretty() # 2 : desc
>>> db.Student.find({field: "computer"}).sort({student_id: -1}).pretty() # 2 : desc
```

### Pagination:Limit-and-Skip-commands
```shell 
>>> db.Posts.find().sort({create_date: -1}).limit(3).pretty() # limit
>>> db.Posts.find().sort({create_date: -1}).skip(3).limit(3).pretty() # skip
>>> db.Posts.find().sort({create_date: -1}).skip(6).limit(3).pretty() # skip
>>> db.Posts.find().sort({create_date: -1}).skip(paginated_by * (page -1)).limit(paginated_by).pretty() # (for example: paginated_by : 9)
```

### $inc-$set-$rename-$unset
```shell
>>> db.Posts.updateOne({title: "post1"}, {$inc: {likes: 1}}) # rather than get value and update database (2 connection), $inc: (1 connection) 
>>> db.Posts.updateOne({title: "post1"}, {$inc: {likes: -1}}) # rather than get value and update database (2 connection), $inc: (1 connection) 
>>> db.Posts.updateMany({}, {$set: {views: 0}}) # $set
>>> db.Posts.updateMany({}, {$rename: {views: "dislikes"}}) # $rename
>>> db.Posts.updateMany({}, {$unset: {views: ""}}) # $remove or $unset
```

### $gt-$lt-$gte-$lte
```shell 
>>>  db.products.find({price: {$gt: 1000}}).pretty() # greater than
>>>  db.products.find({price: {$lt: 1000}}).pretty() # less than
>>>  db.products.find({price: {$gte: 1000}}).pretty() # greater than equal
>>>  db.products.find({price: {$lte: 1000}}).pretty() # less than equal
```
 
### bulkWrite
```shell 
>>> db.products.bulkWrite(
    [
        {
            insertOne: {
                'document': {
                    title: "Phone",
                    price: 1000,
                    likes: 0
                }
            }
        },
        {
            insertOne: {
                'document': {
                    title: "Laptop",
                    price: 890,
                    likes: 0
                }
            }
        },
        {
            updateMany: {
                filter: {
                    likes: {
                        $gte: 100
                    }
                },
                update: {
                    $set: {
                        popular: true
                    }
                }
            }
        },
        {
            delteOne: {
                filter: {
                    title: "Phone"
                }
            }
        },
    ]
)
```

### Search-in-MongoDB(Indexing)
```shell 
# 1) create index on field
>>> db.products.createIndex({title: "text"})
# 2) search
>>> db.products.find({$text: {$search: "Phone"}}).pretty()
```

### Backup-and-Restore-Database
```shell 
>>> mongodump --db db_name  
>>> mongorestore --db db_name <db_address>
```