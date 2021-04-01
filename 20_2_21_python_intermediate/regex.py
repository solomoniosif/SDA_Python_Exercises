import re

# text = "ala Ola Ela"
# pattern = re.compile(f"[A-Z]la")
#
# print(re.search(pattern, text))


text2 = "Thomas W. (33), last seen in Krakow"
# pattern_gresit = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+) l.\)"

pattern2 = r"([A-Z]{1}[a-z]+ [A-Z]{1}\.) \((\d+)\)"

print(re.search(pattern2, text2))
print(re.match(pattern2, text2))


text3 = "https://doi.org/10.1038/nphys1170"
# pattern3 = r"^10.\d{4}/\d+-\d+X?\w+" # (\d+)\d+<[\d\w]+:[\d\w]*>\d+.\d+.\w+;\d$/i"

pattern3 = r"/10.(\d{4,9})/[-._;()/:A-Za-z0-9]+$"
match3 = re.search(pattern3, text3)

print(match3.groups())
