#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_1 = [x for x in set_1 if x not in set_2]
    only_2 = [x for x in set_2 if x not in set_1]
    only_diff = only_1 + only_2
    return only_diff
