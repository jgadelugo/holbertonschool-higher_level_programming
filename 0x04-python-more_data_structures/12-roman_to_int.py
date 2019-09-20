#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    roman_nums = {"I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000}

    nextR = ""
    num = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_nums.keys():
            key = roman_string[i]
            if i < len(roman_string) - 1:
                nextR = roman_string[i + 1]
            if key == "I" and (nextR == "V" or nextR == "X"):
                num -= roman_nums[key]
            elif key == "X" and (nextR == "L" or nextR == "C"):
                num -= roman_nums[key]
            elif key == "C" and (nextR == "D" or nextR == "M"):
                num -= roman_nums[key]
            else:
                num += roman_nums[key]
    return num
