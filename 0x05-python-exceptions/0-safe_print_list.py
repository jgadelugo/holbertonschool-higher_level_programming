#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except:
            i -= 1
            break
    i += 1
    print()
    return i
