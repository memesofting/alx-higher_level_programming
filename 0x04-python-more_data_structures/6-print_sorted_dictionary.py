#!/usr/bin/python3
if __name__ == "6-print_sorted_dictionary":
    def print_sorted_dictionary(a_dictionary):
        sort_dict = sorted(a_dictionary)
        for key in sort_dict:
            print(key, ":", a_dictionary[key])
