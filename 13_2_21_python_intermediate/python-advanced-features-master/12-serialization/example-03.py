import json


if __name__ == "__main__":
    with open("12-serialization/data/example.json") as f:
        data = json.load(f)
    for obj in data:
        print(obj)

    data.append(
        {
            "id": "6",
            "first_name": "Phillis",
            "last_name": "Late",
            "gender": "Female",
            "email": "plate0@loc.gov",
            "job_title": "Civil Engineer",
        }
    )
    with open("12-serialization/data/example.json", "w+") as f:
        json.dump(data, f)
