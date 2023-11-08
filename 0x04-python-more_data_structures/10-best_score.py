#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = 0
        for key, value in a_dictionary.items():
            if a_dictionary[key] > max_score:
                max_score = a_dictionary[key]
                best_score = key
        return best_score
    else:
        return None
