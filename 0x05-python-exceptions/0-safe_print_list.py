#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    track = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            track += 1
    except IndexError:
        pass
    print("")
    return track
