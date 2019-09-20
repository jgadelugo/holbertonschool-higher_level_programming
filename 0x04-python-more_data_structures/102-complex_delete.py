#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = {}
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            continue
        new_dic[key] = a_dictionary[key]
    a_dictionary = new_dic
    return a_dictionary