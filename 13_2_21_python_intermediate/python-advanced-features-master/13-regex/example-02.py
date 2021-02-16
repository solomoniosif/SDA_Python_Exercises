import re

lines = [
    "I.     A Scandal in Bohemia",
    "II.    The Red-Headed League",
    "III.   A Case of Identity",
    "IV.    The Boscombe Valley Mystery",
    "V.     The Five Orange Pips",
]
pattern = re.compile("\w+\.")
for l in lines:
    match = re.search(pattern, l)
    if match:
        print(match.group())
