import csv


if __name__ == "__main__":
    with open("12-serialization/data/example.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(dict(row))
