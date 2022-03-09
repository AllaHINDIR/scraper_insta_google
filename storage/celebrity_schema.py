#we will use mongoengine instead of pymongo
from mongoengine import Document, ListField, StringField,ImageField

#creating the collection (class == collestion and instance == document)
class Celebrity(Document) :

    meta = {"collection" : "celebrities"}
    name = StringField(required=True,min_length=1)
    images = ListField(ImageField(required=True))

