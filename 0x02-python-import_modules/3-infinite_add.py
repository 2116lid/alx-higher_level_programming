#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    length = len(argv)
    add = 0
    for i in range(length):
        add += int(argv[i])
    print(add)
