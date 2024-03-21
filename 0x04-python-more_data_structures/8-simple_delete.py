#!/usr/bin/python3
if __name__ == "8-simple_delete":
    def simple_delete(a_dictionary, key=""):
        if a_dictionary is None:
            return None
        if key in a_dictionary:
            del a_dictionary[key]
        return a_dictionary
