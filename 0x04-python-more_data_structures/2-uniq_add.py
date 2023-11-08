#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_list = 0
    unik_list = list(set(my_list))
    for item in unik_list:
        add_list += item
    return add_list
