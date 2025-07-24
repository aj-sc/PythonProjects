import requests

base_url = 'https://pokeapi.co/api/v2'

def getPokemonInfo(PokemonName):
    url = f'{base_url}/pokemon/{PokemonName.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemonData = response.json()

        if pokemonData:
            print(f'Name: {pokemonData['name'].capitalize()}')
            types = pokemonData['types']
            for type_info in types:
                type_name = type_info['type']['name']
                print(f'Type: {type_name}')

getPokemonInfo('Ampharos')
