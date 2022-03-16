
# dataset of the most followed in Instagram
from Dataset import getDataset

def get_name_celebrities() :
    """
        data = pd.read_csv('https://query.data.world/s/bn4p3ji6o7sm22pzkxszkm7x4gwcyi',encoding="latin-1",usecols=['BRAND', 'CATEGORIES 1'])

        result = data.to_json(orient="table")
        parsed = json.loads(result)
        celebritys = []
        for i in range(0,99) :
            if parsed['data'][i]['CATEGORIES 1'] == "celebrities":
                celebritys.append(parsed['data'][i]['BRAND'] )
        return celebritys
    """
    celebritys = []
    list_categorie_celebritie = getDataset.main()
    for categorie in list_categorie_celebritie :
        for element in categorie['results']['bindings']:
            celebritys.append(element['humanLabel']['value'])
    print(celebritys)
    print(len(celebritys))
    return celebritys


