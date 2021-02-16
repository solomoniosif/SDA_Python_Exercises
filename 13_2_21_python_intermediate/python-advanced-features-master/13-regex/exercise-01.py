"""
Write regular expression which finds matches the first three word characters of a line
Test it with:
I.     A Scandal in Bohemia
II.    The Red-Headed League
III.   A Case of Identity
IV.    The Boscombe Valley Mystery
V.     The Five Orange Pips
"""
import re

lines = [
    "I.     A Scandal in Bohemia",
    "II.    The Red-Headed League",
    "III.   A Case of Identity",
    "IV.    The Boscombe Valley Mystery",
    "V.     The Five Orange Pips",
]

for l in lines:
    match = re.search("^\w\w\w", l)
    if match:
        print(match.group())
