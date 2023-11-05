#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_tuple = ()
    for i in range(2):
        if i < len(tuple_a) and i < len(tuple_b):
            add_tuple = add_tuple + (tuple_a[i] + tuple_b[i],)
        elif i < len(tuple_a):
            add_tuple = add_tuple + (tuple_a[i],)
        elif i < len(tuple_b):
            add_tuple = add_tuple + (tuple_b[i],)
        else:
            add_tuple = add_tuple + (0,)
    return add_tuple
