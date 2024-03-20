#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s == 0:
        sentence[0] = None
    else:
        tup_s = (len_s, sentence[0])
    return tup_s
