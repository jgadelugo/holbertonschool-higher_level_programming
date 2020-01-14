#!/usr/bin/python3
""" Use requests to make a post and return body """
import requests
from sys import argv


if __name__ == "__main__":
    if len(sys.argv) < 2:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data)
    try:
        _json = res.json()
    except ValueError:
        print("Not a valid JSON")
    if len(_json) == 0:
        print("No result")
    else:
        print("[{}] {}".format(_json["id"], _json["name"]))
