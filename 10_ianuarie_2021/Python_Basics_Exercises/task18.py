# Write a program that encrypts a given string using the Caesar cipher,
# which is a special case of a mono-alphabetic substitution cipher.
# The program retrieves the text to be encrypted from the user
# and the number n by which the alphabet is moved by which the text
# is encrypted, and then prints the encrypted text in the console.
# For simplicity, it can be assumed that the input string consists only
# of lowercase letters of the English alphabet, i.e. 'a' - 'z' and spaces.

# Example a: text: alice has a cat, n: 1, result: bmjdf ibt b dbu

# Example b: text: alice has a cat, n: 26, result: alice has a cat

# Get data from the user in the console using argument-less input().
import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)

message = input().lower()
n = int(input())

encrypted_message = ""

for letter in message:
    if letter in alphabet:
        new_letter = alphabet[alphabet.index(letter)+n]
        encrypted_message += new_letter
    else:
        encrypted_message += letter

print(encrypted_message)
