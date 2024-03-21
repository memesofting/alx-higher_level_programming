#!/usr/bin/python3
if __name__ == "6-print_sorted_dictionary":
    def print_sorted_dictionary(a_dictionary):
        for name in sorted(a_dictionary):
            print(name, ":", a_dictionary[name])
