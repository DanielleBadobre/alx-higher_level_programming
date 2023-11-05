#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_mul = ()
    if len(sentence) == 0:
        tuple_mul = tuple_mul + (0, None)
    else:
        tuple_mul = tuple_mul + (len(sentence), sentence[0])
    return tuple_mul
