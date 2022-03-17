import io
import requests
from PIL import Image
from storage import connexion
from storage import celebrity_schema
from cash import cash_image


def NotExist(name ,image ,url ) :
    connexion.get_connexion()
    try :
        celebrity_count = celebrity_schema.Celebrity.objects(name=name).count()
        if celebrity_count == 0 :
            print('[STOP] The celecbrity dont exists !')
            return True
        else:
            for celebrity in celebrity_schema.Celebrity.objects(name=name):
                for img in celebrity.images :
                    #Verification par url !!
                    if img.url == url :
                        print('[STOP] Image already exists.')
                        return False
                    else:
                        imgfile = io.BytesIO(img.image.read())
                        pil_image = Image.open(imgfile)

                        if cash_image.open_cv(image,pil_image) is False :  #return true if they are not the same
                            print('[STOP] Image already exists.')
                            return False
            print('[INFO] Image not already exists.')
            return True
    except Exception as ex:
        print('[ERROR] There is an exception : ',ex)

"""
image = requests.get('https://www.jeunesfooteux.com/photo/art/grande/62997216-45523455.jpg?v=1647163193',timeout=10)
img1 = Image.open(io.BytesIO(image.content))
image2 = requests.get('https://static.onzemondial.com/8/2022/03/photo_article/766605/301457/1200-L-manchester-united-limination-historique-pour-cristiano-ronaldo-une-stat-vieille-de-16-ans-tombe.jpg',timeout=10)
img2 = Image.open(io.BytesIO(image2.content))
"""

image3 = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/1200px-President_Barack_Obama.jpg',timeout=10)
img3 = Image.open(io.BytesIO(image3.content))
print(NotExist('barack obama',img3,'qlq chose'))