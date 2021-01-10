
# ? 1. Write an application that will count how many times a word has occurred in the file and will
# calculate total words in the file and save the results to a new file.
# 2. Be careful not to count a word and a non word character such as a comma as one word (e.g.
# "Hello, World!" should count 2 words total, one "Hello" and one "World").
# 3. Be careful not to be case sensitive (e.g. "Hello hello" should count 2 words total, two "Hello").
# Hint: use str.replace(x, "") to replace unwanted characters like ",", ".", "!", "?"
# Hint: use str.split(" ") to retrieve a list of words from a string


def count_words_in_file(filename):
    words_dict = {}
    with open(filename) as f:
        for line in f:
            for ch in [",", ".", "!", "?", "'", "\n"]:
                if ch in line:
                    line = line.replace(ch,"")
            for word in line.split():
                word = word.lower()
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
    with open("output2.txt","w") as output_f:
        for word in words_dict:
            output_f.write(f"The word '{word}' was found {words_dict[word]} times in '{filename}' file.\n")
        output_f.write(f"The total number of words found in '{filename}': {len(words_dict)}.")

if __name__ == '__main__':
    count_words_in_file('sample.txt')
