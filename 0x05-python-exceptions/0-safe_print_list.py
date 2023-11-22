#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        list_new = [my_list[i] for i in range(x)]
    except IndexError:
        list_new = my_list
    finally:
        count = 0
        for num in list_new:
            print("{}".format(num), end="")
            count += 1
        print("")
        return count
