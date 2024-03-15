#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numarg = len(argv) - 1
    if numarg == 0:
        print("0 arguments.")
    elif numarg == 1:
        print("{} argument.".format(numarg))
    else:
        print("{} arguments:".format(numarg))
    for a in range(numarg):
        print("{}: {}".format(a + 1, argv[a + 1]))
