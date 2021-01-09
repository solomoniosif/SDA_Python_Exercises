
 # * Varianta 1 (Salvarea inputului direct in variabilele finale prin tuple unpacking):
# country1, capital1 = input("Enter the first country and it's capital city: ").split(",")
# country2, capital2 = input("Enter the second country and it's capital city: ").split(",")
# country3, capital3 = input("Enter the third country and it's capital city: ").split(",")

# capitals = {country1.title():capital1.strip().title(), 
#             country2.title():capital2.strip().title(), 
#             country3.title():capital3.strip().title(),
#             }

# * Varianta 2 (Salvarea inputului intr-o lista cu cele doua variabile):
country1 = input("Enter the first country and it's capital city: ").split(",")
country2 = input("Enter the second country and it's capital city: ").split(",")
country3 = input("Enter the third country and it's capital city: ").split(",")

capitals = {country1[0].title(): country1[1].strip().title(),
            country2[0].title(): country2[1].strip().title(),
            country3[0].title(): country3[1].strip().title(),
            }


for country, capital in capitals.items():
    print(f"The capital city of {country} is {capital}.")