# import library
import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['learn_nosql']

# Get the MongoDB collection
collection = db['mongodb']

# Define the updates
updates = [
    {
        'filter': {'nama': 'The Power of Now'},
        'update': {'$set': {'harga': 80000, 'stock': 10}}
    },
    {
        'filter': {'nama': 'The Alchemist'},
        'update': {'$set': {'harga': 110000}}
    },
    {
        'filter': {'nama': 'Sapiens: A Brief History of Humankind'},
        'update': {'$set': {'harga': 140000}}
    },
    {
        'filter': {'nama': 'Thinking, Fast and Slow'},
        'update': {'$set': {'harga': 120000, 'stock': 5}}
    },
    {
        'filter': {'nama': 'The 7 Habits of Highly Effective People'},
        'update': {'$set': {'harga': 119000}}
    },
]

# Update the documents
for update in updates:
    collection.update_many(update['filter'], update['update'], upsert=True)

# Write the data to a CSV file
with open('output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the updated data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])

