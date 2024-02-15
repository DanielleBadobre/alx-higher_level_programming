#!/usr/bin/python3
""" Module to sort a list"""


class MyList(list):
    """class for sorting"""
    def print_sorted(self):
        """ function that sorts list"""
        sorted_list = sorted(self)
        print(sorted_list)
