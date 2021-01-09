import sys

# ! Varianta 1 - cu toti parametri separati de virgula
# parameters = sys.argv[1].split(",")

# capitals = {parameters[0].title():parameters[1].title(),
#             parameters[2].title():parameters[3].title(),
#             parameters[4].title():parameters[5].title(),
#             }

# ! Varianta 2 - cu virgula intre tara si capitala ei si spatiu inaintea urmatoarei tari
parameters = sys.argv[1:]
country1, capital1 = parameters[0].split(',')
country2, capital2 = parameters[1].split(',')
country3, capital3 = parameters[2].split(',') 

capitals = {country1.title():capital1.title(),
            country2.title():capital2.title(),
            country3.title():capital3.title(),
            }

for country, capital in capitals.items():
    print(f"The capital city of {country} is {capital}.")

    