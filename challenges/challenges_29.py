# Challenge #1
# Create a function called serialize() that takes 3 arguments: 
# 1) the Python object you want to serialize, 
# 2) the file to which it serializes the object and 
# 3) the serialization protocol which is pickle or json.

# The function will create the file (the 2nd argument) and will write the 
# Python object to that file according to its 3rd argument. If the 3rd 
# argument is pickle, It will use pickle to serialize the object and if 
# the argument is json it will use json for serialization.

import pickle
import json
import requests
import csv

def serialize(obj, dest_path, prot):
    if prot.lower() == 'json':
        with open(dest_path, 'w') as f:
            json.dump(obj, f)
    else:
        with open(dest_path, 'wb') as f:
            pickle.dump(obj, f)

obj = {1:[1,2,3], 2:[2,3,4], 3:[3,4,5]}

serialize(obj, 'python/challenges/files/serialize_pickle.dat', 'pickle')
serialize(obj, 'python/challenges/files/serialize_json.txt', 'json')

# Challenge #2
# Create a function called deserialize() that takes 2 arguments: 1) the file 
# which contains serialized data and 2) the type of deserialization which is 
# pickle or json.
# The function will deserialize from the file into a Python object and will 
# return that object.

def deserialize(source_path, prot):
    
    if prot == 'json':
        with open(source_path, 'r') as f:
            new_obj = json.load(f)
    else:
        with open(source_path, 'rb') as f:
            new_obj = pickle.load(f)
    return new_obj

# Challenge #3
# Using requests connect to https://jsonplaceholder.typicode.com/users 
# and take the JSON encoded string in Python object

response = requests.get('https://jsonplaceholder.typicode.com/users')
obj = json.loads(response.text)

# Challenge #4
# The resulting Python object will be a list of dictionaries. Process the 
# list and extract the following information for each user:
# Name, City, GPS coordinates in form of (LAT, LNG), Company's name 

res = []
for user in obj:
    res.append([user['name'], user['address']['city'], (user['address']['geo']['lat'], user['address']['geo']['lng']), user['company']['name']])

# Challenge #4
# Write to a CSV File a row for each user. The fields of the CSV file 
# will be: name, city, GPS coordinates and company's name

with open('python/challenges/files/extracted_users.txt', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    header = ['name', 'city', 'GPS coordinates', 'company\'s name']
    writer.writerow(header)
    for user in res:
        writer.writerow(user)
