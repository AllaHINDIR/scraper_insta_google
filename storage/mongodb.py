import io
from tempfile import TemporaryFile
import requests
from PIL import Image
import celebrity_schema
import connexion

connexion.get_connexion()

def save_celebrity(name ,image ,url):
    celebrity = celebrity_schema.Celebrity(name = name)
    fp = TemporaryFile()
    image.save(fp,"JPEG")
    image_document = celebrity_schema.OneImage(url=url)
    #image_document.image.replace(image,filename=name + '.jpg')
    image_document.image.put(fp,filename=name + '.jpg')
    celebrity.images.append(image_document)
    celebrity.save()
    print('[INFO] Image and Celebrity are saved.')

def store_images(name ,image ,url) :
    try :
        celebrity_count = celebrity_schema.Celebrity.objects(name=name).count()
        if celebrity_count == 0 :
            print('[INFO] The celecbrity dont exists !...Wait to add it to DB.')
            save_celebrity(name,image,url)
        else:
            for celebrity in celebrity_schema.Celebrity.objects(name=name):
                fp = TemporaryFile()
                image.save(fp, "JPEG")
                image_document = celebrity_schema.OneImage(url=url)
                image_document.image.put(fp, filename=name + '.jpg')
                celebrity.images.append(image_document)
                celebrity.save()
                print('[INFO] Image saved.')
    except Exception as ex:
        print('[ERROR] There is an exception : ',ex)


image = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/1200px-President_Barack_Obama.jpg',timeout=10)
img1 = Image.open(io.BytesIO(image.content))
store_images('barack obama',img1,'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/1200px-President_Barack_Obama.jpg')








