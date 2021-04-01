
students = {'Cosmin': 26, 'Andra': 21, 'Sorin': 22, 'Andrei': 31, 'Ana': 20}

sorted_by_name_students = sorted(students.items(), key=lambda x: x[0])
sorted_by_age_students = sorted(students.items(), key=lambda x: x[1])

print(sorted_by_name_students)
print(sorted_by_age_students)

names = ['Cosmin', 'Andra', 'Sorin', 'Andrei', 'Ana']
ages = [26, 21, 22, 31, 20]

new_students = {}
for name, age in zip(names, ages):
    new_students[name] = age

print(students)
print(new_students)