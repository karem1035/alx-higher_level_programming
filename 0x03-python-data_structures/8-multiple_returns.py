#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    tuple_0 = a, sentence[0]
    if a == 0:
        tuple_0 = a, None
    else:
        tuple_0 = a, sentence[0]
    return tuple_0
