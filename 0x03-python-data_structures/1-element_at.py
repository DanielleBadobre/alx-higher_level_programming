#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return none
    if idx >= len(my_list):
        return none
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
