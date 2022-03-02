#Import libraries
import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys= ['emmanuelmacron','cristiano ronaldo','trump donald']

    #Parameters
    number_of_images = 2
    min_resolution=(0,0)
    max_resolution=(600,600)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()

    
    #Release resources    
    del image_scrapper