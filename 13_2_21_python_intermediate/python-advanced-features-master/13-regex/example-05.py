import re

lines = [
    "VII.   The Adventure of the Blue Carbuncle",
    "VIII.  The Adventure of the Speckled Band",
    "IX.    The Adventure of the Engineer's Thumb",
    "X.     The Adventure of the Noble Bachelor",
    "XI.    The Adventure of the Beryl Coronet",
]
pattern = re.compile("([IVX]+)\.\s+The Adventure of ([a-zA-Z' ]+)")
for l in lines:
    match = re.search(pattern, l)
    if match:
        print(match.groups())
