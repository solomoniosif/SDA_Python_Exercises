
# ? 6. Write a Python function to read a file line by line and store it into a list.

def save_file_to_list(filename):
    lines_list = []
    with open(filename) as f:
        for line in f.readlines():
            lines_list.append(line.strip())
    return lines_list

lines_list = save_file_to_list('sample.txt')

print(lines_list)
