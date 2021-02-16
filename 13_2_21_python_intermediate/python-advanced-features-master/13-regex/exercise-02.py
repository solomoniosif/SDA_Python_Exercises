"""
UUID (universally unique identifier) format is defined as:
5 groups of lowercase letters and digits
Separated with dashes
Group lengths: 8-4-4-4-12
Write a pattern which matches the UUID format and test it with:
    377b1a2e-79c1-4c32-9ef2-92389f16f0de
    3e233770-9f67-4999-9944-563ce50f1678
    626ce1cd-4441-4957-bbae-5582096cf62d
"""
import re

pattern = re.compile("^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$")
uuids = [
    "377b1a2e-79c1-4c32-9ef2-92389f16f0de",
    "3e233770-9f67-4999-9944-563ce50f1678",
    "626ce1cd-4441-4957-bbae-5582096cf62d",
]
for u in uuids:
    match = pattern.search(u)
    if match:
        print(match.group())
