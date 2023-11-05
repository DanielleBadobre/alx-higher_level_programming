#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxn = 0
    if (my_list):
        for i in range(len(my_list) - 1):
            if my_list[i] > maxn:
                maxn = my_list[i]
    return maxn
