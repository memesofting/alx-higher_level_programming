#!/usr/bin/python3
"""
Module contains class that inherits from list
"""


class MyList(list):
    """MyList class that inherits from the list class"""

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        Returns:
            Sorted list
        """

        if not self:
            print(self)
        else:
            list_sorted = sorted(self)
            print(list_sorted)


if __name__ == "__main__":
    import doctest
    doctest.testfile()
