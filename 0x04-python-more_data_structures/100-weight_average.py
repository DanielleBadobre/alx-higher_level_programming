#!/usr/bin/python3
def weight_average(my_list=[]):
    divider = 0
    number = 0
    if my_list:
        for i in range(len(my_list)):
            number += my_list[i][0] * my_list[i][1]
            divider += my_list[i][1]
        return (number / divider)
    else:
        return 0
