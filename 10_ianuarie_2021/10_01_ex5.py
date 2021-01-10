
# ? 5. Write a Python function to print first n lines of a file

# ! Varianta 1
def read_n_lines(filename, n):
    with open(filename) as f:
        for line_no, line in enumerate(f):
            if line_no < n:
                print(line, end="") 

read_n_lines("sample.txt",5)

# ! Varianta 2
def read_n_lines2(filename,n):
    with open(filename) as f:
        lines = f.readlines()
        for i in range(n):
            print(lines[i], end="")


read_n_lines2("sample.txt", 5)