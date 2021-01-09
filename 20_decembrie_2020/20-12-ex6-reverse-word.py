
# ? Write a Python program that accepts a word from the user and reverse it.

word = input("Enter a word to print it reversed: ")

# ! Rezolvarea 1
print(word[::-1])

# ! Rezolvarea 2
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word

print(reversed_word)

# ! Rezolvarea 3
reversed_word2 = ""
for i in range(len(word)-1, -1, -1):
    reversed_word2 += word[i]

print(reversed_word2)