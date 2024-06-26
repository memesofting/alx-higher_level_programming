#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if my_list_1 is None or my_list_2 is None:
        return None
    if my_list_1 is not None and my_list_2 is not None:
        for i in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wrong type")
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            finally:
                new_list.append(result)
        return new_list
