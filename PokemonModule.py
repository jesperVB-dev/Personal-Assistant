import json
from pprint import pprint

Data = json.load(open('PokemonInfo.json'))

AllPokemon = [[str(Data[key]["name"]).lower(),key] for key in Data]

#print(AllPokemon)
#pprint(data)

class Pokemon:
    def Questions(text):
        for i in AllPokemon:
            if i[0] in text:
                Pokemon = Data[i[1]]
                if " type" in text:
                    return str(Pokemon["types"]).replace("'","").replace("[","").replace("]","").replace(",", "")
                elif " stats" in text:
                    return "hp " + str(Pokemon["attack"]) + "attack " + str(Pokemon["attack"]) + " defense " + str(Pokemon["defense"]) + " special attack " + str(Pokemon["spattack"])+ " special defense " + str(Pokemon["spdefense"]) + " speed " + str(Pokemon["speed"])
        return False

