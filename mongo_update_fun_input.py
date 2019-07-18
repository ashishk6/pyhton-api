import pymongo
from pymongo import MongoClient
import pprint


def update(roll,name,address):
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
    rec_id1 = emp.update_many({"roll":roll}, 
        { 
                "$set":{ 
                        "name":name,
                        "address": address
                        } 
                  
                } ) 

    # Printing the data updated record 
    print("Here is the updated data of the employee:")
    for record in emp.find({"roll":roll}):
        pprint.pprint(record)

roll=int(input("Enter the roll number for which you want to update: "))
name=input("Enter the updated name of employee: ")
address=input("Enter the updated address: ")
update(roll,name,address)
