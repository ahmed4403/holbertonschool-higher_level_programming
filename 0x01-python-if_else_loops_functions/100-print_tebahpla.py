#!/usr/bin/python3
for le in range(122, 96, -1):
    print("{}".format(chr(le)) if le % 2 == 0 else chr(le).upper(), end="")
