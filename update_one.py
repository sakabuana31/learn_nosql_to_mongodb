# import library
import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['learn_nosql']

# Insert a Single Document in to collection
collection = db['mongodb']

# Update the harga field of a document
query = {"nama": "Atomic Habits"}
new_values = {"$set": {"harga": 120000,"stock" : 30}}
collection.update_one(query, new_values)

# Write the data to a CSV file
with open('output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the updated data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])

    