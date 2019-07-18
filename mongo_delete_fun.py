import pymongo
from pymongo import MongoClient
import pprint
def delete(roll):
    client = pymongo.MongoClient("localhost", 27017)
    client
    #MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
    # database
    collection_USER = client['local']
    collection_USER
    #Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'local')
    # collection
    emp = collection_USER.emp
       

    # update Data 
    rec_id1 = emp.remove({"roll":roll} ) 

    # Printing the data inserted 
    for record in emp.find():
        pprint.pprint(record)

delete(1)
