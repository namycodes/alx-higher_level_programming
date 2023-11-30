#!/usr/bin/python3
if __name__ == "__main__":
    from calculator import add, sub, div, mult

    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, add(a, b)))
    print('{} + {} = {}'.format(a, b, sub(a, b)))
    print('{} + {} = {}'.format(a, b, mult(a, b)))
    print('{} + {} = {}'.format(a, b, div(a, b)))
