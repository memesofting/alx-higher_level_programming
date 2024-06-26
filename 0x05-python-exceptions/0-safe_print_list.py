#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        count = 0
        for i in range(x):
            try:
                print("{}". format(my_list[i]), end="")
                count += 1
            except IndexError:
                print()
                return count
        print()
        return count
