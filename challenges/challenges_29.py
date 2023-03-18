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

print(deserialize('python/challenges/files/serialize_pickle.dat', 'pickle'))
print(deserialize('python/challenges/files/serialize_json.txt', 'json'))
