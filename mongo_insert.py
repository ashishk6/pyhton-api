
import pymongo
from pymongo import MongoClient
import pprint
client = pymongo.MongoClient("localhost", 27017)
client
#MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
# database
collection_USER = client['local']
collection_USER
#Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'local')
# collection
emp = collection_USER.emp
# creating JSON documunt
emp_rec1 = { 
        "name":"Mr.Geek", 
        "roll":10, 
        "address":"delhi"
        } 
emp_rec2 = { 
        "name":"Mr.Shaurya", 
        "roll":11, 
        "adress":"delhi"
        } 

# Insert Data 
rec_id1 = emp.insert_one(emp_rec1) 
rec_id2 = emp.insert_one(emp_rec2) 

# Printing the data inserted 
for record in emp.find().limit(10):
     pprint.pprint(record)
