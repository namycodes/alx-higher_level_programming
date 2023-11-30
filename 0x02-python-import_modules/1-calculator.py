#!/usr/bin/python3
if __main__ == "__main__":
    from calculator import add, sub, div, mult

    a = 10
    b = 5
    print('{}'.format(add(a, b)))
    print('{}'.format(sub(a, b)))
    print('{}'.format(mult(a, b)))
    print('{}'.format(div(a, b)))
