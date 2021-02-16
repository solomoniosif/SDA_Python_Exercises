"""
Knowing that json.loads() loads JSON from string instead of a file, load given JSON string and save it as CSV and JSON files.
[
 {"id":1,"lat":16.3112941,"long":104.8221147,"country":"Thailand","city":"Don Tan"},
 {"id":2,"lat":41.400351,"long":-8.5116191,"country":"Portugal","city":"Antas"}
]
"""
import csv
import json


if __name__ == "__main__":
    data_string = (
        "["
        '{"id":1,"lat":16.3112941,"long":104.8221147,"country":"Thailand","city":"Don Tan"},'
        '{"id":2,"lat":41.400351,"long":-8.5116191,"country":"Portugal","city":"Antas"}'
        "]"
    )
    data = json.loads(data_string)

    with open("12-serialization/data/exercise-02.csv", "w+") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writerows(data)
    with open("12-serialization/data/exercise-02.json", "w+") as f:
        json.dump(data, f)
