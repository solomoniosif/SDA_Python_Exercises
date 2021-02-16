"""
Using either a reader or a DictReader, load records from 12-serialization/data/people.csv file
Print the following information:
    Number of all records
    Number of people missing an e-mail address
    Number of people with middle name
    Save all the records with e-mail missing to a new file
"""
import csv


if __name__ == "__main__":
    missing_email_rows = []
    missing_middle_name = 0
    total = 0
    with open("12-serialization/data/people.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["email"] == "":
                missing_email_rows.append(row)
            if row["middle_name"] == "":
                missing_middle_name += 1
            total += 1
    print(f"Total rows: {total}")
    print(f"Rows with missing e-mail: {len(missing_email_rows)}")
    print(f"Rows with missing middle name: {missing_middle_name}")
    with open("12-serialization/data/people-no-email.csv", "w+") as f:
        writer = csv.DictWriter(f, fieldnames=missing_email_rows[0].keys())
        writer.writerows(missing_email_rows)
