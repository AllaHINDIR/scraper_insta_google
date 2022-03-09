
#import selenium drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#import helper libraries
import time
import os
import save_image

#custom patch libraries
import patch 

class GoogleImageScraper():
    def __init__(self,webdriver_path,image_path, search_key="Donald Trump",number_of_images=1,min_resolution=(0,0),max_resolution=(300,300)):
        #check parameter types
        image_path = os.path.join(image_path, search_key)
        if (type(number_of_images)!=int):
            print("[Error] Number of images must be integer value.")
            return
        if not os.path.exists(image_path):
            print("[INFO] Image path not found. Creating a new folder.")
            os.makedirs(image_path)
        #check if chromedriver is updated
        while(True):
            try:
                #try going to www.google.com
                options = Options()
                options.add_argument("headless")
                driver = webdriver.Chrome(webdriver_path, chrome_options=options)
                #driver.set_window_size(1400,1050)
                driver.get("https://www.google.com")
                break
            except:
                #patch chromedriver if not available or outdated
                try:
                    driver
                except NameError:
                    is_patched = patch.download_lastest_chromedriver()
                else:
                    is_patched = patch.download_lastest_chromedriver(driver.capabilities['version'])
                if (not is_patched): 
                    exit("[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
                    
        self.driver = driver
        self.search_key = search_key
        self.number_of_images = number_of_images
        self.webdriver_path = webdriver_path
        self.image_path = image_path
        self.url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"%(search_key)
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution


    def find_image_urls(self):
        print("[INFO] Scraping for image link... Please wait.")
        image_urls=[]
        count = 0
        number_of_unable_click = 0
        self.driver.get(self.url)
        time.sleep(1.5)
        numero_image = 1
        while self.number_of_images > count:
            try:
                #find and click image
                imgurl = self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%(str(numero_image)))
                imgurl.click()
                number_of_unable_click = 0
            except Exception:
                #print("[-] Unable to click this photo.")
                number_of_unable_click = number_of_unable_click + 1
                if (number_of_unable_click > 10):
                    print("[INFO] No more photos.")
                    break
                 
            try:
                #select image from the popup
                time.sleep(1)
                class_names = ["n3VNCb"]
                images = [self.driver.find_elements_by_class_name(class_name) for class_name in class_names if len(self.driver.find_elements_by_class_name(class_name)) != 0 ][0]
                for image in images:
                    #only download images that starts with https
                    src_link = image.get_attribute("src")
                    if("https" in  src_link):
                        print("[INFO] %d. %s"%(count,src_link))
                        if save_image.save_image(src_link,count,self.image_path,self.search_key,self.min_resolution,self.max_resolution) :
                            image_urls.append(src_link)
                            count +=1
                            break
            except Exception:
                print("[INFO] Unable to get link")

            try:
                #scroll page to load next image
                if(count%3==0):
                    self.driver.execute_script("window.scrollTo(0, "+str(numero_image*60)+");")
                element = self.driver.find_element_by_class_name("mye4qd")
                element.click()
                print("[INFO] Loading more photos")
                time.sleep(1.5)
            except Exception:  
                time.sleep(1)
            numero_image += 1
        self.driver.quit()
        print("[INFO] Google search ended")
        return image_urls





