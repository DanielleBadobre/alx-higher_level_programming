#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) and ord(str[i]) <= 123:
            c = ord(str[i]) - 32
        else:
            c = ord(str[i])
        print("{}".format(chr(c)), end="")
    print("")
