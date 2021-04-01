import json


students = [
        {
                'name': "Adam",
                'surname': "Smith",
                'number of points': 20
        },
        {
                'name': "John",
                'surname': "Shadow",
                'number of points': 17
        }
]

with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)

with open('students.json', 'r') as f:
    data = json.load(f)
    for student in data:
        print(student)

with open('students.json', 'r') as f:
    content = f.read()
    # content += 'x'
    data = json.loads(content)
    # for student in data:
    #     print(student)

with open('students2.json', 'w') as f:
    data = json.dumps(students)
    data = json.loads(data)
    json.dump(data, f, indent=4)