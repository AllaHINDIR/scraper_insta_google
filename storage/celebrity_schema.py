#we will use mongoengine instead of pymongo
from mongoengine import Document, ListField, StringField, ImageField, EmbeddedDocument, EmbeddedDocumentField


class OneImage(EmbeddedDocument):
    url = StringField(required=True)
    image = ImageField(required=True)

#creating the collection (class == collestion and instance == document)
class Celebrity(Document) :

    meta = {"collection" : "celebrities"}
    name = StringField(required=True,min_length=1)
    images = ListField(EmbeddedDocumentField(OneImage))

