import sys

parameters = sys.argv[1:]

capitals = {parameters[0].title():parameters[1].title(),
            parameters[2].title():parameters[3].title(),
            parameters[4].title():parameters[5].title(),
            }

for country, capital in capitals.items():
    print(f"The capital city of {country} is {capital}.")