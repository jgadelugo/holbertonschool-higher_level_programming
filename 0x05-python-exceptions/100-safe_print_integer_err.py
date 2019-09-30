#!/usr/bin/python3i
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as inst:
        print("Exception: {}".format(inst), file=stderr)
        return False
    return True
