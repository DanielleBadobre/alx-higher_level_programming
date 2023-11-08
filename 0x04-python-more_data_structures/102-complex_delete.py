#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_list = []
    for key, valu in a_dictionary.items():
        if valu = value:
            delete_list.append(key)
    for key in delete_list:
        del a_dictionary[key]
    return a_dictionary
