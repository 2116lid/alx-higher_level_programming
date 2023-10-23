#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    track = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                track += 1
    except (TypeError):
        pass
    print("")
    return (track)
