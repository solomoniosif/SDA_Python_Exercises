# Fie variabilele:
name = "Maria"
verb = "are"
stuff = "mere"
# a) Folosind cele 3 tipuri diferite de formatare invatate formati propozitii in variabilele:
# phrase1 (printf style), phrase2 (str.format style) si phrase3 (f strings) printand de fiecare data rezultatul
# b) extrageti intr-o variabila noua numele din phrase3 folosind slices [:]


phrase1 = "%s %s %s" % (name, verb, stuff)
phrase2 = "{} {} {}".format(name, verb, stuff)
phrase3 = f"{name} {verb} {stuff}"
nume = phrase3[:5]

print(phrase1)
print(phrase2)
print(phrase3)
print(nume)
