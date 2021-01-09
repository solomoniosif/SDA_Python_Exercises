# Inside that folder, create file printing-exercise.py.
# Print out numbers from 0 to 5, each in new line, starting with "|START|" string and ending
# with "|END|" string using a maximum of 2 print() functions. The result should look like that:
# |START|0|END|
# |START|1|END|
# |START|2|END|
# |START|3|END|
# |START|4|END|
# |START|5|END|

print("|START|", end="")
print(0, 1, 2, 3, 4, 5, sep="|END|\n|START|", end="|END|")




print()
print(help(print))










# print("\n\n|START|0|END|\n|START|1|END|\n|START|2|END|\n|START|3|END|\n|START|4|END|\n|START|5|END|")