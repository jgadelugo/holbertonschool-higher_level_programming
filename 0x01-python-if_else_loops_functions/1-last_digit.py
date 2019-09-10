#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(str(number)[-1])

print("Last digit of {:d} is ".format(number), end='')
if number > 0 and lastdigit != 0:
    if lastdigit > 5:
        print("{:d} and is greater than 5".format(lastdigit))
    else:
        print("{:d} and is less than 6 and not 0".format(lastdigit))
elif number < 0 and lastdigit != 0:
    print("{:s} and is less than 6 and not 0".format("-" + str(lastdigit)))
else:
    print("{:d} and is 0".format(lastdigit))
