import re

title = '"The Adventures of Sherlock Holmes" by Arthur Conan Doyle'
for pattern in ["by", "by ......", "by .+", "bygone"]:
    match = re.search(pattern, title)
    if match:
        print(match.group())
    else:
        print(f"No match for '{pattern}'")
