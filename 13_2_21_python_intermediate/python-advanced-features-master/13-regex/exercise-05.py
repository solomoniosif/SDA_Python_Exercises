"""
Using re.findall and provided file holmes.txt, find all the words which end 
the sentence. Count them.
"""
import re

with open("13-regex/holmes.txt") as f:
    text = f.read()
    ends = re.findall("\w+\.", text)
print(ends)
print(f"Count: {len(ends)}")
