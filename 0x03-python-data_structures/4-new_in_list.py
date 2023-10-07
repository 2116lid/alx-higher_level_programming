#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    nw_li = my_list[:]
    if idx < 0 or idx >= length:
        return nw_li
    else:
        nw_li[idx] = element
        return nw_li
