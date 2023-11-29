#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        i = chr(i - 32)
    else:
        i = chr(i)
    print("{}".format(i), end="")
