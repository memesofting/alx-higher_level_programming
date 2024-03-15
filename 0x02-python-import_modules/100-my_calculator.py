#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    numargs = len(argv) - 1
    if numargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    '''operator = {"+" : add, "-" : sub, "*" : mul, "/" : div}
    if argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:'''
    if argv[2] == "+":
        result = add(a, b)
    elif argv[2] == "-":
        result = sub(a, b)
    elif argv[2] == "*":
        result = mul(a, b)
    elif argv[2] == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, argv[2], b, result))
