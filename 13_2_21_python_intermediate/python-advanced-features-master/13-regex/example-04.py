import re

lines = [
    "I.     A Scandal in Bohemia",
    "II.    The Red-Headed League",
    "III.   A Case of Identity",
    "IV.    The Boscombe Valley Mystery",
    "V.     The Five Orange Pips",
]
pattern = re.compile("[IV]+\.\s+[A-Za-z ]{1,200}")
for l in lines:
    match = re.search(pattern, l)
    if match:
        print(match.group())
