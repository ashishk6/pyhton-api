
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
     # delete all the employee data  
result = emp.remove( 
        {"roll":10}
        ) 

  # Printing the data inserted 
for record in emp.find().limit(10):
     pprint.pprint(record)
