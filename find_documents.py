# import library
import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['learn_nosql']

# Connect to collection
collection = db['mongodb']

# Query the database for records with stock < 5 and harga > 100000
query = {"stock": {"$lt": 5}, "harga": {"$gt": 100000}}
results = collection.find(query)

# Write the data to a CSV file
with open('output/find_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in results:
        # Print the found data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])