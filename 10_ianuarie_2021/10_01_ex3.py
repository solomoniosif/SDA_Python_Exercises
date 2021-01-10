
# ? 3. Repeat previous 2 exercises and write the result in a file called output.txt

def search_word_in_file():
    searched_word = input("\nEnter word to search: ")
    filename = input("Enter the name of the file to search: ")
    try:
        with open(filename, 'r') as f:
            for number, line in enumerate(f):
                with open("output.txt", "w") as output_f:
                    if searched_word in line:
                        print(f"The word '{searched_word}' was found in line {number}. The results were saved to 'output.txt'")
                        output_f.write(f"The word '{searched_word}' was found in line {number}:")
                        output_f.write(f"\n'{line}'")
                        break
                    print(f"\nThe word '{searched_word}' was not found in '{filename}'")
                    output_f.write(f"The word '{searched_word}' was not found in '{filename}'")
                    break
    except FileNotFoundError:
        print(f"\nThere is no '{filename}' file in current folder!")

if __name__ == '__main__':
    search_word_in_file()