#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if sentence == "":
        tup_s = (0, None)
        return tup_s
    else:
        tup_s = (len_s, sentence[0])
        return tup_s
