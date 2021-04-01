import requests
import json


def chuck():
    f = r"http://api.icndb.com/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)

    print(tt["value"]["joke"])


chuck()