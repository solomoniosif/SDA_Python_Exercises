import re

# ######################     EXERCISE 1     ###################### #
print("""\nEx.1: Write a Python program to check that a string contains
only a certain set of characters (in this case a-z, A-Z and 0-9).""")

pattern = re.compile(r"[a-zA-Z0-9]+")

test_string_1 = 'test1234ASLFS'
test_string_2 = "ABC 234 xyz"
test_string_3 = "dfgvsljdfnvLBL:JN^%(^&)231236"

test_strings = [test_string_1, test_string_2, test_string_3]

for string in test_strings:
    match = re.fullmatch(pattern, string)
    print(f"{string}: {bool(match)}")

# ######################     EXERCISE 2     ###################### #
print("""\nEx.2: Write a Python program that matches a string 
that has an a followed by zero or more b's.""")

pattern = re.compile(r'ab*')

string_1 = "Carbuncle"
string_2 = "Abracadabra"
string_3 = "Soldier"

strings = [string_1, string_2, string_3]

for string in strings:
    match = re.search(pattern, string)
    print(f"{string}: {match.group() if match else None}")

# ######################     EXERCISE 3     ###################### #
print("""\nEx.3: Write a Python program that matches a string 
that has an a followed by one or more b's.""")

pattern = re.compile(r'ab+')

string_1 = "Carbuncle"
string_2 = "Abracadabra"
string_3 = "Soldier"

strings = [string_1, string_2, string_3]

for string in strings:
    match = re.search(pattern, string)
    print(f"{string}: {match.group() if match else None}")

# ######################     EXERCISE 4     ###################### #
print("""\nEx.4:  Write a Python program that matches a string 
that has an a followed by zero or one 'b'.""")

pattern = re.compile(r'ab?')

string_1 = "Cabin"
string_2 = "Abracadabra"
string_3 = "Abyss"

strings = [string_1, string_2, string_3]

for string in strings:
    match = re.search(pattern, string)
    print(f"{string}: {match.group() if match else None}")

# ######################     EXERCISE 5     ###################### #
print("""\nEx.5:  Write a Python program that matches a string 
that has an a followed by three 'b'.""")

pattern = re.compile(r'ab{3}')

string_1 = "Cabin"
string_2 = "Abracadabbbbra"
string_3 = "Abstract"

strings = [string_1, string_2, string_3]

for string in strings:
    match = re.search(pattern, string)
    print(f"{string}: {match.group() if match else None}")

# ######################     EXERCISE 6     ###################### #
print("""\nEx.6:  Write a Python program that matches a string 
that has an a followed by two to three 'b'.""")

pattern = re.compile(r'ab{2,3}')

string_1 = "Cabin"
string_2 = "Abracadabbbbra"
string_3 = "sabbs"

strings = [string_1, string_2, string_3]

for string in strings:
    match = re.search(pattern, string)
    print(f"{string}: {match.group() if match else None}")

# ######################     EXERCISE 7     ###################### #
print("""\nEx.7:  Write a Python program to find sequences of 
lowercase letters joined with a underscore.""")

pattern = re.compile(r'[a-z]+_[a-z]+')

string_1 = "Cabin"
string_2 = "__init__"
string_3 = "apply_discount"

strings = [string_1, string_2, string_3]

for string in strings:
    match = re.search(pattern, string)
    print(f"{string}: {match.group() if match else None}")

# ######################     EXERCISE 8     ###################### #
print("""\nEx.8:  Write a Python program to find the sequences of 
one upper case letter followed by lower case letters.""")

pattern = re.compile(r'[A-Z][a-z]+')

string_1 = "Cabin"
string_2 = "__init__"
string_3 = "Ludwig van Beethoven"

strings = [string_1, string_2, string_3]

for string in strings:
    matches = pattern.finditer(string)
    if matches:
        for match in matches:
            print(f"{string}: {match.group()}")
