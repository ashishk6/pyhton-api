# Pyhon scripts for connecting to MongoDB

>Python script is a very powerful script which can help you to perform any task with just a few lines of codes.
>Here we will discuss on the CRUD operation on mongoDB using Python script.

Steps to configure mongoDB on your machine:
- For mongoDB, we will be using docker container. Click [MongoDB](https://hub.docker.com/_/mongo) to see the container under docker hub.
- Use the below script to configure the container:
docker run -it --rm -d -p 27017:27017 mongo

Steps to configure Python on your machine:
- sudo apt-get update
- sudo apt-get install python3.6

Create a database(local) and a collection(emp)
db.emp.insert({'roll':1,"name":"Ramesh",'address':'Hyderabad'})
db.emp.insert({'roll':2,"name":"Rajesh",'address':'Mumbai'})
and so on

# Attaching the code that will perform the CRUD operation


### Link for learning Python and mongoDB

 - [mongoDB](https://docs.mongodb.com/manual/introduction/)
 - [Python](https://docs.python.org/3.6/tutorial/index.html)
  
 Note: Every operation had been defined in a seperate branch.
