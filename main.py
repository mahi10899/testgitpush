import pymongo
import urllib.parse

# Set the username and password
username = "mahindrabommu"
password = "Amma@143"

# Escape the username and password using urllib.parse.quote_plus
escaped_username = urllib.parse.quote_plus(username)
escaped_password = urllib.parse.quote_plus(password)

# Construct the MongoDB connection URI using the escaped username and password
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.c7yj0s6.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB using pymongo
client = pymongo.MongoClient(uri)
db= client.test

print(db)
d={
    "name": "mahi",
    "email": "mahi@mahi.com",
     "number":"1234567890"
}
db1= client['mongotest']
coll = db1['test']
coll.insert_one(d)