#!/usr/bin/python3
""" get data from starwars api """
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://swapi.co/api/people/"
    data = {"search": argv[1]}
    res = requests.get(url, params=data)
    _json = res.json()
    print("Number of results:", _json.get("count"))
    for name in _json.get("results"):
        print(name.get("name"))
