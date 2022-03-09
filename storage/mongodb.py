"""
import pymongo

#the connexion
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ingeniance"]

#Get the list of our DBs
print(client.list_database_names())



#Crate a collection
collection = db["celebrity"]
"""
import celebrity_schema
import connexion

connexion.get_connexion()
celebrity = celebrity_schema.Celebrity(name = "Ellen")

image_path = "../photos/Ellen/Ellen0.jpeg"
image = open(image_path,'rb')
#celebrity.images.replace(image,filename="Ellen0.jpeg")
print(type(celebrity.images))
#celebrity.save()






