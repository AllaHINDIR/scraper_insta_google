import io

import numpy
import numpy as np
import requests
from PIL import Image, ImageChops
import hashlib
import cv2
import imutils
from numpy import average
from skimage.metrics import structural_similarity as ssim


## methode with md5

def hashfile(file):
    # A arbitrary (but fixed) buffer
    # size (change accordingly)
    # 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536

    # Initializing the sha256() method
    md5 = hashlib.md5()

    # Opening the file provided as
    # the first commandline argument
    with open(file, 'rb') as f:

        while True:

            # reading data = BUF_SIZE from
            # the file and saving it in a
            # variable
            data = f.read(BUF_SIZE)

            # True if eof = 1
            if not data:
                break

            # Passing that data to that sh256 hash
            # function (updating the function with
            # that data)
            md5.update(data)

    # sha256.hexdigest() hashes all the input
    # data passed to the sha256() via sha256.update()
    # Acts as a finalize method, after which
    # all the input data gets hashed hexdigest()
    # hashes the data, and returns the output
    # in hexadecimal format
    return md5.hexdigest()


def main_md5():
    # Calling hashfile() function to obtain hashes
    # of the files, and saving the result
    # in a variable
    f1_hash = hashfile('a.jpg')
    f2_hash = hashfile('a.jpg')

    # Doing primitive string comparison to
    # check whether the two hashes match or not
    if f1_hash == f2_hash:
        print("Both files are same")
        print(f"Hash: {f1_hash}")

    else:
        print("Files are different!")
        print(f"Hash of File 1: {f1_hash}")
        print(f"Hash of File 2: {f2_hash}")


# methode PIL
def pil(image1,image2):

    diff = ImageChops.difference(image1,image2)

    if diff.getbbox():
        diff.show()
    else:
        print('Kif Kif :) ')

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err
    # return the MSE, the lower the error, the more "similar"
    # the two images are

# methode Opencv
def open_cv(image1,image2):
    try :
        # use numpy to convert the pil_image into a numpy array
        numpy_image1 = numpy.array(image1)
        numpy_image2 = numpy.array(image2)

        # convert to a openCV2 image, notice the COLOR_RGB2BGR which means that
        # the color is converted from RGB to BGR format
        img1 = cv2.cvtColor(numpy_image1, cv2.COLOR_RGB2BGR)
        img2 = cv2.cvtColor(numpy_image2, cv2.COLOR_RGB2BGR)

        #img1 = cv2.imread(image1)
        #img2 = cv2.imread(image2)

        dim = (500,500)
        img1 = cv2.resize(img1,dim,interpolation=cv2.INTER_AREA)
        img2 = cv2.resize(img2,dim,interpolation=cv2.INTER_AREA)

        x1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        x2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


        # cette methode compare les couleurs (B/R/V)
        diff = cv2.subtract(img1, img2)
        #print(diff)
        result = not np.any(diff)  # if diff is all zero it will return False


        m = mse(x1, x2)
        s = ssim(x1, x2)
        print ("mse: %s, ssim: %s" % (m, s))
        #Par ImageChops (PIL)
        pil(image1,image2)

        if result is True:
            print("Images are the same !")
            print('[STOP] Image already exist.')
            return False
        else:
            #cv2.imwrite('result.jpg', diff)
            print("The Images are different")
            return True
    except Exception as ex :
        print('[ERROR] There are an exception : ', ex)


"""
image = requests.get('https://www.jeunesfooteux.com/photo/art/grande/62997216-45523455.jpg?v=1647163193',timeout=10)
img1 = Image.open(io.BytesIO(image.content))
image2 = requests.get('https://static.onzemondial.com/8/2022/03/photo_article/766605/301457/1200-L-manchester-united-limination-historique-pour-cristiano-ronaldo-une-stat-vieille-de-16-ans-tombe.jpg',timeout=10)
img2 = Image.open(io.BytesIO(image2.content))
open_cv(img1,img1)
"""


