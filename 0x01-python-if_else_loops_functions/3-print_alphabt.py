#!/usr/bin/python3
for n in range(97, 123):
    if chr(n) == 'e':
        continue
    elif chr(n) == 'q':
        continue
    else:
        print("{}".format(chr(n)), end="")
