# import library
import csv
from pymongo import MongoClient
from pprint import pprint

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['learn_nosql']

# Insert a Single Document in to collection
collection = db['mongodb']

# Delete one document
query = {'nama': 'The Alchemist'}
result = collection.delete_one(query)

# Print the deleted data
pprint(f'{result.deleted_count} document(s) deleted')
