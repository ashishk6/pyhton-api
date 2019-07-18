import pymongo
from pymongo import MongoClient
import pprint
def select(roll):
    client = pymongo.MongoClient("localhost", 27017)
    client
    #MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
    # database
    collection_USER = client['local']
    collection_USER
    #Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'local')
    # collection
    emp = collection_USER.emp
        

    # Printing the data  
    for record in emp.find({'roll':roll}):
        pprint.pprint(record)

roll=int(input('Enter the roll numner to get the record: '))
select(roll)
