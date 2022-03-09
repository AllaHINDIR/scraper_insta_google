import json
import time
from pprint import pprint

from SPARQLWrapper import SPARQLWrapper, JSON
import concurrent.futures
from multiprocessing.dummy import Pool
import getOccupation

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
sparql = SPARQLWrapper(endpoint)


def extract_string(string):
    try:
        found = string.removeprefix("http://www.wikidata.org/entity/")
        print(found)
        return found
    except AttributeError:
        pass


def get_persons(occupation):
    sparql.setQuery("""
    SELECT DISTINCT ?human ?humanLabel ?humanDescription ?birth ?linkcount
    WHERE
    {
      {
      SELECT ?human ?humanLabel ?humanDescription ?birth ?linkcount WHERE {
      VALUES ?profession {wd:""" + extract_string(occupation['profession']['value']) + """}
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
    with open(occupation['professionLabel']['value'] + '.json', 'w') as fichier:
        json.dump(results, fichier)
    print(
        "----------------------------- " + occupation['professionLabel']['value'] + " --------------------------------")
    # pprint(results)
    return results


def main() :
    if __name__ == '__main__':
        start = time.time()
        occupations = getOccupation.get_occupation()
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as process:
            r = process.map(get_persons, [occupations['results']['bindings'][0], occupations['results']['bindings'][1],
                                       occupations['results']['bindings'][2], occupations['results']['bindings'][3],
                                       occupations['results']['bindings'][4], occupations['results']['bindings'][5]])
        end = time.time()
        print(end - start)
        return r

main()