#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_uniq = set()
    total = 0
    for i in my_list:
        sum_uniq.add(i)
    for n in sum_uniq:
        total += n
    return total
