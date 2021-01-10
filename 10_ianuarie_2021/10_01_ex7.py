
# ? 7.  Write a python function to find the longest word in a file.

def longest_word(filename):
    longest_word = ""
    with open(filename) as f:
        for line in f:
            for ch in [",", ".", "!", "?", "'", "\n"]:
                if ch in line:
                    line = line.replace(ch,"")
            for word in line.strip().split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

print(longest_word('sample2.txt'))