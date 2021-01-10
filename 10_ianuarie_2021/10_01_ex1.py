
# ? 1. Given an input file, print out the number of text lines from the file.
# ? Skip counting the empty lines. Hint: use str.rstrip() method to eliminate the line separator \n


# ! Varianta 1
# lines = 0
# with open('sample.txt') as f:
#     for line in f:
#         if len(line.rstrip()) > 0:
#             lines += 1
        
# print(lines)


# ! Varianta 2
lines = 0
with open('sample.txt') as f:
    for line in f:
        if line.rstrip():
            lines += 1

print(lines)