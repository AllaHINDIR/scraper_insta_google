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
import io
from tempfile import TemporaryFile

import numpy
import requests
from PIL import Image
import cv2
import celebrity_schema
import connexion

connexion.get_connexion()

def store_images(name ,image ,url) :

    celebrity = celebrity_schema.Celebrity(name = name)

    fp = TemporaryFile()
    image.save(fp,"JPEG")


    image_document = celebrity_schema.OneImage(url=url)
    #image_document.image.replace(image,filename=name + '.jpg')
    image_document.image.put(fp,filename=name + '.jpg')

    celebrity.images.append(image_document)

    celebrity.save()
    print('[INFO] Image saved.')

image = requests.get('https://www.jeunesfooteux.com/photo/art/grande/62997216-45523455.jpg?v=1647163193',timeout=10)
img1 = Image.open(io.BytesIO(image.content))
print(img1.format)

store_images('C7',img1,'https://www.jeunesfooteux.com/photo/art/grande/62997216-45523455.jpg?v=1647163193')








