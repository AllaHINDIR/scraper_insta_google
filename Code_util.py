def save_images(self, image_urls):
    # save images into file directory
    """
        This function takes in an array of image urls and save it into the prescribed image path/directory.
        Example:
            google_image_scraper = GoogleImageScraper("webdriver_path","image_path","search_key",number_of_photos)
            image_urls=["https://example_1.jpg","https://example_2.jpg"]
            google_image_scraper.save_images(image_urls)

    """
    print("[INFO] Saving Image... Please wait...")
    for indx, image_url in enumerate(image_urls):
        try:
            print("[INFO] Image url:%s" % (image_url))
            search_string = ''.join(e for e in self.search_key if e.isalnum())
            image = requests.get(image_url, timeout=5)
            if image.status_code == 200:
                with Image.open(io.BytesIO(image.content)) as image_from_web:
                    try:
                        filename = "%s%s.%s" % (search_string, str(indx), image_from_web.format.lower())
                        image_path = os.path.join(self.image_path, filename)
                        print("[INFO] %d .Image saved at: %s" % (indx, image_path))
                        image_from_web.save(image_path)
                    except OSError:
                        rgb_im = image_from_web.convert('RGB')
                        rgb_im.save(image_path)
                    image_resolution = image_from_web.size
                    if image_resolution != None:
                        if image_resolution[0] < self.min_resolution[0] or image_resolution[1] < self.min_resolution[
                            1] or image_resolution[0] > self.max_resolution[0] or image_resolution[1] > \
                                self.max_resolution[1]:
                            image_from_web.close()
                            # print("GoogleImageScraper Notification: %s did not meet resolution requirements."%(image_url))
                            os.remove(image_path)

                    image_from_web.close()
        except Exception as e:
            print("[ERROR] Failed to be downloaded", e)
            pass
    print(
        "[INFO] Download Completed. Please note that some photos are not downloaded as it is not in the right format (e.g. jpg, jpeg, png)")
