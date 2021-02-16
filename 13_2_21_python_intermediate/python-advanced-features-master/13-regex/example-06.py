import re

lines = """
    VII.   The Adventure of the Blue Carbuncle
    VIII.  The Adventure of the Speckled Band
    IX.    The Adventure of the Engineer's Thumb
    X.     The Adventure of the Noble Bachelor
    XI.    The Adventure of the Beryl Coronet
"""
matches = re.findall("The Adventure of [a-zA-Z' ]+", lines)
print(matches)
it = re.finditer("The Adventure of [a-zA-Z' ]+", lines)
print(it)
