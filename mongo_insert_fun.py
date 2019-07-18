import pymongo
from pymongo import MongoClient
import pprint


def insert(roll,name,address):
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
            "name":name, 
            "roll":(roll), 
            "address":address
            } 
    

    # Insert Data 
    rec_id1 = emp.insert_one(emp_rec1) 

    # Printing the data inserted 
    for record in emp.find().limit(10):
        pprint.pprint(record)

insert(2,'anil','mumbai')