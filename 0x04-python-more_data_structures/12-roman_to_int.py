#!/usr/bin/pyhon3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    to_int = 0
    before = 0
    roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    for letter in roman_string[::-1]:
        value = roman_num.get(letter, 0)
        if value < before:
            to_int -= value
        else:
            to_int += value
        before = value
    return to_int 
