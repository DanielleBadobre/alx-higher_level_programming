#!/usr/bin/python3
""" Module to say given name """


def say_my_name(first_name, last_name=""):
    """
    Function to print a name and last name
    :param first_name: first name to print
    :param last_name: last name to print
    :return: nothing
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
