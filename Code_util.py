def save_images(self, image_urls):
    # save images into file directory
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

def get_actors():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q33999}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 3000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40

    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()

    with open('actors.json', 'w') as actors_fichier:
        json.dump(results, actors_fichier)
    print("-----------------------------get_actors--------------------------------")
    # pprint(results)


def get_singer():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q177220}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 3000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40

    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('singers.json', 'w') as singers_fichier:
        json.dump(results, singers_fichier)
    print("-----------------------------get_singer--------------------------------")


def get_politician():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q82955}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1950-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 3000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40
    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('politician.json', 'w') as politician_fichier:
        json.dump(results, politician_fichier)
    print("-----------------------------get_politician--------------------------------")


def get_footballeur():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q937857}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 3000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40
    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('footbolleur.json', 'w') as footbolleur_fichier:
        json.dump(results, footbolleur_fichier)
    print("-----------------------------get_footballeur--------------------------------")


def get_dancers():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q5716684}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 30000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40
    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('dancers.json', 'w') as dancers_fichier:
        json.dump(results, dancers_fichier)
    print("-----------------------------get_dancers--------------------------------")


def get_basketbolleur():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q3665646}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 30000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40
    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('basketbolleur.json', 'w') as basketbolleur_fichier:
        json.dump(results, basketbolleur_fichier)
    print("-----------------------------get_basketbolleur--------------------------------")

def get_youtubeur():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q17125263}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 30000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40
    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('youtubeur.json', 'w') as youtubeur_fichier:
        json.dump(results, youtubeur_fichier)
    print("-----------------------------get_youtubeur--------------------------------")

def get_animateur():
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:Q13590141}
      ?human wdt:P31 wd:Q5.    
      ?human wdt:P106 ?profession.
      ?human wdt:P569 ?birth.
      ?human wikibase:sitelinks ?linkcount.
      FILTER("1980-01-01"^^xsd:dateTime <= ?birth).
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
      }
      LIMIT 30000
    }
    }
    ORDER BY DESC (?linkcount)
    LIMIT 40
    """)

    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    with open('animateurs.json', 'w') as animateur_fichier:
        json.dump(results, animateur_fichier)
    print("-----------------------------get_animateurs--------------------------------")