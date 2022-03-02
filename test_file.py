import json
import pandas as pd
# dataset of the most followed in Instagram

data = pd.read_csv('https://query.data.world/s/bn4p3ji6o7sm22pzkxszkm7x4gwcyi',encoding="latin-1",usecols=['BRAND', 'CATEGORIES 1'])

print(data)
print(type(data))

result = data.to_json(orient="index")
parsed = json.loads(result)
celebritys = []
for i in range(0,99) :
    a = str(i)
    if parsed.a.CATEGORIES_1 == "celebrities":
        celebritys.append(parsed.a.BRAND)
print(parsed)
print(json.dumps(parsed, indent=4))
print(celebritys)