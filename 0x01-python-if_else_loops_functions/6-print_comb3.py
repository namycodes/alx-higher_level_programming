#!/usr/bin/python3
for f in range(10):
    for s in range(f + 1, 10):
        print("{:d}{:d}".format(f, s), end=", " if f < 8 else '\n')
