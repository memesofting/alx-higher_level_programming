#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    if str is None:
        return None
    else:
        for i in range(len(str)):
            if i == n:
                continue
            else:
                new += str[i]
    return new
