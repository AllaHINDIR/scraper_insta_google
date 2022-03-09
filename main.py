#Import libraries
import os
import time
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable
import get_celebrities
from multiprocessing.dummy import Pool
import concurrent.futures

# search key (celebrities)
# search_keys= ['emmanuelmacron','cristiano ronaldo','trump donald']
search_keys2 = get_celebrities.get_name_celebrities()
search_keys = [search_keys2[i] for i in range(1, 31)]

def get_images(search_key) :
    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    # Parameters
    number_of_images = 20
    min_resolution = (0, 0)
    max_resolution = (10000, 10000)

    # Main program
    image_scrapper = GoogleImageScraper(webdriver_path, image_path, search_key, number_of_images, min_resolution, max_resolution)
    image_urls = image_scrapper.find_image_urls()

    # Release resources
    del image_scrapper

if __name__ == "__main__":
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor :
        executor.map(get_images,search_keys)
    end = time.time()
    print(end-start)