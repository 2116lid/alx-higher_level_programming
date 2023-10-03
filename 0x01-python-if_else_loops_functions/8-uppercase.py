#!/usr/bin/python3
def uppercase(str):
    res = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            res = res + chr((ord(char) - 32))
        else:
            res += char
    print("{}".format(res))
