#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_add = set()
    sum_li = 0
    for i in my_list:
        if i not in new_add:
            new_add.add(i)
            sum_li += i
    return sum_li
