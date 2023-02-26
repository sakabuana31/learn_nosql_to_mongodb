# import library
import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['learn_nosql']

# Insert Many Document in to collection
collection = db['mongodb']
many = [
        {
        "nama": "The Power of Now",
        "author": "Eckhart Tolle",
        "tags": "Spirituality",
        "harga": 79000,
        "stock": 8
        },
        {
        "nama": "The Alchemist",
        "author": "Paulo Coelho",
        "tags": "Fiction",
        "harga": 120000,
        "stock": 3
        },
        {
        "nama": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "tags": "History",
        "harga": 135000,
        "stock": 7
        },
        {
        "nama": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "tags": "Psychology",
        "harga": 112000,
        "stock": 2
        },
        {
        "nama": "The 7 Habits of Highly Effective People",
        "author": "Stephen Covey",
        "tags": "Self-Improvement",
        "harga": 105000,
        "stock": 3
        }
        ]
for record in many:
    # Ignore data that already exist
    collection.update_many(record, {'$set': record}, upsert=True)

# Write the data to a CSV file
with open('output/data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nama', 'author', 'tags', 'harga', 'stock'])
    for record in collection.find():
        # Print the inserted data
        pprint(record)
        writer.writerow([record['nama'], record['author'], record['tags'], record['harga'], record['stock']])