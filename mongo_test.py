
import pymongo
from pymongo import MongoClient
import pprint
client = pymongo.MongoClient("localhost", 27017)
client
#MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
collection_USER = client['local']
collection_USER
#Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'local')
emp = collection_USER.emp
print('Total Record for the collection: ' + str(emp.count()))
for record in emp.find().limit(10):
     pprint.pprint(record)
