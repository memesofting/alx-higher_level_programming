#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_n = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > max_n:
                max_n = my_list[i]
            else:
                continue
    return max_n
