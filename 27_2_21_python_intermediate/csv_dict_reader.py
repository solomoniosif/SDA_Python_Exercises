import csv


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


def write_csv(filename, data: dict):
    with open(filename, 'a') as f:
        writer = csv.DictWriter(f, ['First Name', 'Last Name', 'Age', 'Salary'], lineterminator='\n')
        writer.writerow(data)


if __name__ == '__main__':
    read_csv('employees.csv')

    katie = {'First Name': 'Katie', 'Last Name': 'Bauer', 'Age': 34, 'Salary': 4700}

    write_csv('employees.csv', katie)

    read_csv('employees.csv')
