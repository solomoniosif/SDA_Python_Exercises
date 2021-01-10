
# ? 2. Write a function to search in the file for a word given by the user 


def search_word_in_file():
    searched_word = input("\nEnter word to search: ")
    filename = input("Enter the name of the file to search: ")
    try:
        with open(filename, 'r') as f:
            for number, line in enumerate(f):
                if searched_word in line:
                    print(f"\nThe word '{searched_word}' was found in line {number}:")
                    print(f"'{line.rstrip()}'")
                    return True
                print(f"\nThe word '{searched_word}' was not found in '{filename}'")
                return False
    except FileNotFoundError:
        print(f"\nThere is no '{filename}' file in current folder!")

if __name__ == '__main__':
    search_word_in_file()
