import csv


if __name__ == "__main__":
    rows = []
    with open("12-serialization/data/example.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
            print(row)
    rows.append([6, "Phillis", "Late", "Female", "plate0@loc.gov", "Civil Engineer"])
    with open("12-serialization/data/example.csv", "w+") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(rows)
