#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print('{:02d}'.format(last_digit), end="")
