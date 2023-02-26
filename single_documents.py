# import library
import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['learn_nosql']

# Insert a Single Document in to collection
collection = db['mongodb']
data = [
        {
        "nama" : "Atomic Habits", 
        "author" : "James Clear", 
        "tags" : "Self Improvements", 
        "harga" : 108000, 
        "stock" : 10
        }
        ]
for record in data:
    # Ignore data that already exist
    collection.update_one(record, {'$set': record}, upsert=True)

# Write the data to a CSV file
with open('output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the inserted data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])
