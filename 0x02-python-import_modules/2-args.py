#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) > 1:
        count = 0
        print("{:d} arguments:".format(len(argv) - 1))
        for arg in argv:
            count += 1
            if count != 1:
                print("{:d}: {}".format(count - 1, arg))
    else:
        print("0 arguments.")
