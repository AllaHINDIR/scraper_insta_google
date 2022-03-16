#If an image respect the resolution, it will be saved
import os
import requests
import io
from PIL import Image


def save_image( image_url, image_number,images_path,search_key,min_resolution,max_resolution):
    try:
        print("[INFO] Image url:%s" % (image_url))
        search_string = ''.join(e for e in search_key if e.isalpha() or e.isspace())
        image = requests.get(image_url, timeout=10)
        if image.status_code == 200:
            with Image.open(io.BytesIO(image.content)) as image_from_web:
                try:
                    image_resolution = image_from_web.size
                    if image_resolution != None:
                        if image_resolution[0] > min_resolution[0] and image_resolution[1] > min_resolution[1] and image_resolution[0] < max_resolution[0] and image_resolution[1] < max_resolution[1]:
                            filename = "%s%s.%s" % (search_string, str(image_number), image_from_web.format.lower())
                            image_path = os.path.join(images_path, filename)
                            print("[INFO] %d Image saved at: %s" % (image_number, image_path))
                            image_from_web.save(image_path)
                            image_from_web.close()
                        else:
                            print("[ERROR] The Image don't respect the resolution !")
                            return False
                except OSError:
                    rgb_im = image_from_web.convert('RGB')
                    rgb_im.save(image_path)

                image_from_web.close()
    except Exception as e:
        print("[ERREOR] Failed to be dowloaded", e)
        return False
    print("[INFO] Download Completed.")
    return True
