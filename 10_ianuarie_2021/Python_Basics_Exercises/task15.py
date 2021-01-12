# Write a program that reads the text entered by the user and then divides it into individual words.
# Then counts the number of occurrences of words regardless of case and writes them to the console in alphabetical order.

# For example, for the text 'Ala likes cats, but she is not liked by Cats.' ',
# The program should write in the console:

# ala - 1
# but - 1
# is - 1
# cats - 2
# likes - 1
# liked - 1
# no - 1
# through - 1
# Assume that any punctuation marks may appear in the text.

# Get data from the user in the console using argument-less input().


user_input = input().replace(".", "").replace(
    ",", "").replace("!", "").replace("?", "")

words = user_input.lower().split()
words_count = {w: words.count(w) for w in words}

for word in sorted(words_count.items()):
    print(f"{word[0]} - {word[1]}")
