# 2. Inside that folder, create file strings-exercise.py.
# Write a program that operates on a provided string, that always has length of at least 10
# characters.
# a. If the string length is even, retrieve a substring that is exactly 4 characters long and is
# exactly in the middle of the original string.
# b. If the string length is odd, retrieve a substring that is exactly 5 characters long and is
# exactly in the middle of the original string.
# Tips: Make use of the len() and int() as well as the % and [] operators. Example of the int()
# function.
# a = int(3 / 2) # rounds down 1.5 to 1 and assigns it to a


def get_middle_substring(string):
    mid_idx = int(len(string) / 2)
    if len(string) < 10:
        return "The input string is too short"
    elif len(string) % 2 == 0:
        return string[mid_idx-2:mid_idx+2]
    else:
        return string[mid_idx-2:mid_idx+3]


# print(get_middle_substring("1234567891"))
# print(get_middle_substring("12345678912"))


string = "1234567890"

middle_substring = string[int(len(string)/2) -
                          2:int(len(string)/2)+2 + len(string) % 2]

print(middle_substring)

print(string[::-3])
