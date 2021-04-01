"""Write a Python program that matches a string that has an a followed by zero or more b's"""

import re

pattern = re.compile(r'ab*')

string_1 = "Carbuncle"
string_2 = "Abracadabra"
string_3 = "Soldier"

strings = [string_1, string_2, string_3]

for string in strings:
    print(re.search(pattern, string))
