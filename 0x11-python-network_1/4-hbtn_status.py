#!/usr/bin/python3
""" Use requests to get response and print """
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- type:", response)
