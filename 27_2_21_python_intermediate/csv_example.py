import csv


def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def write_csv(filename, data: list):
    with open(filename, 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(data)


if __name__ == '__main__':
    read_csv('employees.csv')

    katie = ['Katie', 'Bauer', 34, 4700]

    write_csv('employees.csv', katie)

    read_csv('employees.csv')
