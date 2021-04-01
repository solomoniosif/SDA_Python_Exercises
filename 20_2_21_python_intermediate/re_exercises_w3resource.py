import re


# ! EXERCISE 1
print("""\n1. Write a Python program to check that a string contains only
a certain set of characters (in this case a-z, A-Z and 0-9).""")

pattern = re.compile(r"^[a-zA-Z0-9]*$")

test_strings = ['Guido van Rossum',
                'guido@van-rossum.com', '+15771204321', 'guido']

for string in test_strings:
    print(
            f" >>> Test string '{string}':  {'Match found:' if pattern.search(string) else 'No match found'}")
    if pattern.search(string):
        print(f"\t{pattern.search(string).group()}")

# ! EXERCISE 2
print("""\n2. Write a Python program that matches a string
that has an a followed by zero or more b's.""")

pattern = re.compile(r"ab*")

test_strings = ['ab', 'abyss', 'Python', 'barbarian', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 3
print("""\n3. Write a Python program that matches a string
that has an a followed by one or more b's. """)

pattern = re.compile(r"ab+")

test_strings = ['ab', 'abyss', 'Python', 'barbarian', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 4
print("""\n4. Write a Python program that matches a string that
has an a followed by zero or one 'b'. """)

pattern = re.compile(r"ab?")

test_strings = ['ab', 'abyss', 'Python', 'barbarian', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 5
print("""\n5. Write a Python program that matches a string
that has an a followed by three 'b'.""")

pattern = re.compile(r"ab{3}")

test_strings = ['abbb', 'abb bb a_bb', 'barbarian', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 6
print("""\n6. Write a Python program that matches a string
that has an a followed by two to three 'b'. """)

pattern = re.compile(r"ab{2,3}")

test_strings = ['abbb', 'abb bb a_bb', 'barbarian', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 7
print("""\n7. Write a Python program to find sequences
of lowercase letters joined with a underscore.""")

pattern = re.compile(r"[a-z]+_[a-z]+")

test_strings = ['get_url', 'abb bb a_bb', 'APPLY_DISCOUNT', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 8
print("""\n8. Write a Python program to find the sequences
of one upper case letter followed by lower case letters.""")

pattern = re.compile(r"[A-Z][a-z]+")

test_strings = ['get_url', 'Abb Bo A_bb', 'APPLY_DISCOUNT', 'Abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 9
print("""\n9. Write a Python program that matches a string
that has an 'a' followed by anything, ending in 'b'.""")

pattern = re.compile(r"a.*?b$")

test_strings = ['get_url', 'abb bb a_bb', 'ab', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 10
print("""\n10. Write a Python program that matches
a word at the beginning of a string.""")

pattern = re.compile(r"^[a-zA-Z]+")

test_strings = ['test string', 'Python Course', ' magic method', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 11
print("""\n11. Write a Python program that matches a word at the end of string,
with optional punctuation.""")

pattern = re.compile(r"[A-Za-z]+[.!?]?$")

test_strings = ['Python is fun.', 'No match found!',
                'Regular expressions', 'abba']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 12
print("\n12. Write a Python program that matches a word containing 'z'.")

pattern = re.compile(r"\b\w*z\w*\b")

test_strings = ['Python is fun.', 'calzone recipe',
                'zi, azi', 'Peperoni pizza']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 13
print("""\n13. Write a Python program that matches a word containing 'z',
not at the start or end of the word.""")

pattern = re.compile(r"\b\w+z\w+\b")

test_strings = ['Python is fun.', 'calzone recipe',
                'zi, azi', 'Peperoni pizza']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 14
print("""\n14. Write a Python program to match a string that contains
only upper and lowercase letters, numbers, and underscores.""")

pattern = re.compile(r"^[A-Za-z0-9_]+$")

test_strings = ['Python is fun.', 'get_price',
                'zi, azi', 'Peperoni09']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 15
print("\n15. Write a Python program where a string will start with a specific number.")

pattern = re.compile(r"^(7.*)")

test_strings = ['exercise 7.', '7th floor',
                '7 days', 'bring 7 beers and 2 pizzas']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 16
print("\n16. Write a Python program to remove leading zeros from an IP address.")

pattern = re.compile(r"\.[0]{1,2}")

ip_adresses = ['192.158.001.038', '255.255.255.255',
               '168.212.026.204', '135.058.024.017']

for ip_address in ip_adresses:
    print(f" >>> {ip_address} => {re.sub(pattern, '.', ip_address)}")

# ! EXERCISE 17
print("\n17. Write a Python program to check for a number at the end of a string.")

pattern = re.compile(r"9$")

test_strings = ['exercise 9', '9th floor',
                '9 days', 'bring 7 beers and 2 pizzas']

for string in test_strings:
    print(
            f" >>> Test string '{string}': {'Match/es found:' if pattern.search(string) else 'No match found'}")
    matches = pattern.finditer(string)
    for match in matches:
        print(f"\t{match.group()}")

# ! EXERCISE 18
print("""\n18. Write a Python program to search the numbers (0-9)
of length between 1 to 3 in a given string.""")

pattern = re.compile(r"[0-9]{1,3}")

test_string = "Exercises number 1, 12, 13, and 345 are important"

print(f"Test string: {test_string}")
for match in pattern.finditer(test_string):
    print(f" >>> {match.group()}")

# ! EXERCISE 19
print("""\n19. Write a Python program to search some literals strings in a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'""")

pattern = re.compile(r"(fox|dog|horse)")

sample_text = 'The quick brown fox jumps over the lazy dog.'

for match in pattern.finditer(sample_text):
    print(f" >>> {match.group()}")

# ! EXERCISE 20
print("""\n20. Write a Python program to search a literals string in a string and
also find the location within the original string where the pattern occurs.

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'""")

pattern = re.compile(r"fox")

sample_text = 'The quick brown fox jumps over the lazy dog.'

for match in pattern.finditer(sample_text):
    print(f" >>> {match.group()}: {match.span()}")

# ! EXERCISE 21
print("""\n21. Write a Python program to find the substrings within a string.
Sample text :  'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'
Note: There are three instances of exercises in the input string.""")

pattern = re.compile(r"exercises")

sample_text = 'Python exercises, PHP exercises, C# exercises'

for match in pattern.finditer(sample_text):
    print(f" >>> {match.group()}")

# ! EXERCISE 22
print("""\n22. Write a Python program to find the occurrence and position
of the substrings within a string.
Sample text :  'Python exercises, PHP exercises, C# exercises'""")

pattern = re.compile(r"exercises")

pattern = re.compile(r"exercises")

sample_text = 'Python exercises, PHP exercises, C# exercises'

print(f"Number of occurrences: {len(pattern.findall(sample_text))}")
for match in pattern.finditer(sample_text):
    print(f" >>> {match.group()}: {match.span()}")

# ! EXERCISE 23
print("\n23. Write a Python program to replace whitespaces with an underscore and vice versa.")

pattern = re.compile(r" ")

sample_text = "This is a sample text."

subbed_text = re.sub(pattern, '_', sample_text)

print(f"Original text: {sample_text}")
print(f"Modified text: {subbed_text}")

subbed_text_2 = re.sub(r'_', ' ', subbed_text)
print(f"Modified text 2: {subbed_text_2}")

# ! EXERCISE 24
print("\n24. Write a Python program to extract year, month and date from an url.")

urls = ['www.geography.com/earth-quakes-in-europe-on/28-12-1994',
        'http://myblog.com/2014/11/30/sample-post',
        'http://www.newspaper.com/edition/2020-12-27.html'
        ]


def extract_date_from_url(url):
    pattern = re.compile(r"(\d{2,4})[/.-]?(\d{2})[/.-]?(\d{2,4})")
    date = pattern.search(url)
    if len(date.group(1)) == 4:
        year, month, day = date.group(1), date.group(2), date.group(3)
    elif len(date.group(3)) == 4:
        year, month, day = date.group(3), date.group(2), date.group(1)
    return year, month, day


for url in urls:
    year, month, day = extract_date_from_url(url)
    print(f"{url}\n >>> Year={year}, Month={month}, Day={day}")

# ! EXERCISE 25
print("""\n25. Write a Python program to convert a date of yyyy-mm-dd format
to dd-mm-yyyy format.""")


def convert_date(text_date: 'yyyy-mm-dd') -> str:  # dd-mm-yyy
    pattern = re.compile(r"(\d{4})-(\d{1,2})-(\d{1,2})")
    date = pattern.search(text_date)
    return '-'.join([date.group(3), date.group(2), date.group(1)])


sample_dates = [
        '2021-02-26',
        '1953-06-14',
        '1989-12-21'
]

for date in sample_dates:
    print(f" >>> {date} -> {convert_date(date)}")

# ! EXERCISE 26
print("""\n26. Write a Python program to match if two words from
a list of words starting with letter 'P'.""")


def two_words_with_P(words):
    # pattern = re.compile(r"")
    return re.search(r'(\bP\w+).*(\bP\w+)', words)


list_of_words = [
        'Python is Powerful',
        'Python is Easy',
        'SQL is Needed',
        'COMPROMISED POSITION'
]

for words in list_of_words:
    if bool(two_words_with_P(words)):
        print(f" >>> {words}: {bool(two_words_with_P(words))}  -> ({two_words_with_P(words).group(1)}, "
              f"{two_words_with_P(words).group(2)})")
    else:
        print(f" >>> {words}: {bool(two_words_with_P(words))}")

# ! EXERCISE 27
print("""\n27. Write a Python program to separate and print
the numbers of a given string.""")

test_string = 'We need to book a 2 bedroom apartment for \n5 nights for our trip to Greece in 25 July 2021.'


def extract_numbers(text):
    pattern = re.compile(r'\d+')
    matches = pattern.finditer(text)
    numbers = []
    for matches in matches:
        numbers.append(int(matches.group()))
    return numbers


print(f"Test string:\n{test_string} \n -> {extract_numbers(test_string)}")

# ! EXERCISE 28
print("""\n28. Write a Python program to find all words
starting with 'a' or 'e' in a given string.""")

test_string = "banana apple elephant airbag spear mouse cat elbow"

pattern = re.compile(r'\b[a|e]\w+\b')

matches = pattern.finditer(test_string)

print(f"Test string: '{test_string}'")
for match in matches:
    print(f" >>> {match.group()}")

# ! EXERCISE 29
print("""\n29. Write a Python program to separate and print
the numbers and their position of a given string.""")

test_string = '123abc456CDE789xyz'
pattern = re.compile(r'\d+')
matches = pattern.finditer(test_string)
print(f"Test string: {test_string}")
for match in matches:
    print(f" >>> {match.group()}, position: {match.span()[0]} - {match.span()[1]}")

# ! EXERCISE 30
print("""\n30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.""")

pattern = re.compile(r'Road')

test_string = 'Port Louis, Mauritius, 27 Costal Road'

subbed_string = pattern.sub('Rd.', test_string)

print(f"Original string: {test_string}")
print(f"Modified string: {subbed_string}")

# ! EXERCISE 31
print("""\n31. Write a Python program to replace all occurrences of space, comma, or dot with a colon.""")

pattern = re.compile(r'[\ |,|\.]')

test_string = """
Python is an interpreted, high-level and general-purpose
programming language. Python's design philosophy emphasizes
code readability with its notable use of significant indentation."""

subbed_string = pattern.sub(':', test_string)

print(f"Original string: {test_string}\n")
print(f"Modified string:{subbed_string}")

# ! EXERCISE 32
print("""\n32. Write a Python program to replace maximum 2
occurrences of space, comma, or dot with a colon.""")

sample_string = """
Paradigm: Multi-paradigm: functional, imperative, object-oriented, structured, reflective"""

pattern = re.compile(r'[\ |,|\.]')

modified_string = pattern.sub(':', sample_string, 2)

print(f"Original string: {sample_string}")
print(f"Modified string: {modified_string}")

# ! EXERCISE 33
print("""\n33. Write a Python program to find all five characters long word in a string.""")

test_string = """
Python is an interpreted, high-level and general-purpose
programming language. Python's design philosophy emphasizes
code readability with its notable use of significant indentation."""

pattern = re.compile(r'\b\w{5}\b')

matches = pattern.finditer(test_string)

print(f"Tets string:{test_string}")
for matche in matches:
    print(f" >>> {matche.group()}")

# ! EXERCISE 34
print("""\n34. Write a Python program to find all three,
four, five characters long words in a string.""")

test_string = """
Python is an interpreted, high-level and general-purpose
programming language. Python's design philosophy emphasizes
code readability with its notable use of significant indentation."""

pattern = re.compile(r'\b\w{3,5}\b')

matches = pattern.finditer(test_string)

print(f"Tets string:{test_string}")
for match in matches:
    print(f" >>> {match.group()}")

# ! EXERCISE 35
print("""\n35. Write a Python program to find all words which
are at least 4 characters long in a string.""")

test_string = """
Python is an interpreted, high-level and general-purpose
programming language. Python's design philosophy emphasizes
code readability with its notable use of significant indentation."""

pattern = re.compile(r'\b\w\w\w\w+\b')

matches = pattern.finditer(test_string)

print(f"Tests string:{test_string}")
for match in matches:
    print(f" >>> {match.group()}")


# # ! EXERCISE 36
# print("""\n36. Write a python program to convert
# camel case string to snake case string.""")
#
# def camel_to_snake_case(text):
#     pattern = re.compile(r'[a-z]+([A-Z])[a-z]+')
#     matches = pattern.finditer(text)
#
#
#
# # ! EXERCISE 37
# print("""\n37. Write a python program to convert
# snake case string to camel case string.""")


# ! EXERCISE 38
"""38. Write a Python program to extract values between quotation marks of a string.


# ! EXERCISE 39
39. Write a Python program to remove multiple spaces in a string.


# ! EXERCISE 40
40. Write a Python program to remove all whitespaces from a string.


# ! EXERCISE 41
41. Write a Python program to remove everything except alphanumeric characters from a string.


# ! EXERCISE 42
42. Write a Python program to find urls in a string.


# ! EXERCISE 43
43. Write a Python program to split a string at uppercase letters.


# ! EXERCISE 44
44. Write a Python program to do a case-insensitive string replacement.


# ! EXERCISE 45
45. Write a Python program to remove the ANSI escape sequences from a string.


# ! EXERCISE 46
46. Write a Python program to find all adverbs and their positions in a given sentence.

Sample text : "Clearly, he has no excuse for such behavior."


# ! EXERCISE 47
47. Write a Python program to split a string with multiple delimiters.

Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. An example of a delimiter is the comma character, which acts as a field delimiter in a sequence of comma-separated values.


# ! EXERCISE 48
48. Write a Python program to check a decimal with a precision of 2.



# ! EXERCISE 49
49. Write a Python program to remove words from a string of length between 1 and a given number.


# ! EXERCISE 50
50. Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow"""

# # ! EXERCISE 51
# print("""51. Write a Python program to insert spaces between words starting with capital letters.""")

# # ! EXERCISE 52
# print("""\n52. Write a Python program that reads a given expression and evaluates it.
# Terms and conditions:
# The expression consists of numerical values, operators and parentheses, and the ends with '='.
# The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
# When two operators have the same precedence, they are applied to left to right.
# You may assume that there is no division by zero.
# All calculation is performed as integers, and after the decimal point should be truncated Length of the expression will not exceed 100.
# -1 ? 10 9 = intermediate results of computation = 10 9""")

# # ! EXERCISE 53
# print("""\n53. Write a Python program to remove
# lowercase substrings from a given string.""")
