import requests

def get_pokemon(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    data = response.json()

    return data


pokemon = get_pokemon("pikachu")

print("Nome:", pokemon["name"])

print("Tipos:")
for t in pokemon["types"]:
    print("-", t["type"]["name"])
