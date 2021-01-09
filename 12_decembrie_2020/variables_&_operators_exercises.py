substantiv = "mere "
verb = "are"
name = "Iosif"
spatiu = " "

print(name + " " + verb + " " + (substantiv * 3))
print(name + spatiu + verb + spatiu + (substantiv * 3))
print(name, verb, substantiv.strip(), substantiv.strip(), substantiv.strip())

# String Formatting
# 1. Using %
print('%s %s %s' % (name, verb, substantiv*3))
# 2. Using .format()
print("{} {} {}".format(name, verb, substantiv*3))
# 3. Using f-string
print(f"{name} {verb} {substantiv * 3}")
