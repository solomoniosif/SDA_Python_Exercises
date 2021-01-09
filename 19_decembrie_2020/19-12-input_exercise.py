
# ! Input exercises
# 1. In PyCharm, create folder 08-user-input.
# 2. Inside that folder, create file input-exercise-01.py.
# 3. Write an application that prints a dictionary containing 3 country - capital pairs:
# a. Use input function to query user for a country and its capital three times for each pair (6
# inputs total).
# b. Print out the resulting dictionary.
# 4. In folder 08-user-input create file input-exercise-02.py.
# 5. Write the same application this time using input() only 3 times.
# a. User should input country and its capital in one input, separated by a comma
# "Japan,Tokyo".
# b. Use string split(",") function to split the string into a list of 2 substrings - the country
# and the city. The split(",") function splits a string by a programmer defined delimiter
# into a list of substrings, for example: 'Japan,TokĀo' => ['Japan', 'TokĀo']
# c. Print out the resulting dictionary

country1 = input("Enter the name of the first country: ")
capital1 = input("Enter the capital city of the first country: ")

country2 = input("Enter the name of the second country: ")
capital2 = input("Enter the capital city of the second country: ")

country3 = input("Enter the name of the third country: ")
capital3 = input("Enter the capital city of the third country: ")


capitals = {country1:capital1, country2:capital2, country3:capital3}

print(capitals)