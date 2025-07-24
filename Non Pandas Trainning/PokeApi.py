import requests
import json

while True:
    pokemonNameInput = input('Write the name of the pokemon: ').lower()

    if pokemonNameInput.isalpha():
        break

baseUrl = f'https://pokeapi.co/api/v2/pokemon/{pokemonNameInput}'

response = requests.get(baseUrl)

if response.status_code == 200:
   baseData = response.json()

   abilities = baseData.get('abilities', [])
   types = baseData.get('types', [])
   stats = baseData.get('stats', [])

   abilitiesList = []
   typesList = []
   statsDict = {}

   for abilityData in abilities:
       ability = abilityData.get('ability', {})
       abilityName = ability.get('name', '')

       abilitiesList.append(abilityName)

   for typeData in types:
       typeBase = typeData.get('type', {})
       typeName = typeBase.get('name', '')

       typesList.append(typeName)

   for statData in stats:
       stat = statData.get('stat', {})
       statName = stat.get('name', '')
       statValue = statData.get('base_stat', '')

       if statName not in statsDict:
          statsDict[statName] = statValue


   pokemonData = {
      'name': baseData.get('name', ''),
      'type': typesList,
      'abilities': abilitiesList,
      'stats': statsDict
   }

   file_path = f'C:/Users/Albert Salas/Desktop/{pokemonNameInput}.json'

   while True:
        actionInput = input('Would you like to save this data ? (Yes or No): ').lower()

        if actionInput.isalpha():
            if actionInput == 'yes':
                with open(file_path, 'w') as file:
                    json.dump(pokemonData, file, indent=4)
                    print('File loaded!')
                    break
            else:
                print('Ok, here is the data:')
                print(json.dumps(pokemonData, indent=4))
                break

else:
   print('Error')