#!/usr/bin/python3
"""Defining a function"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    res = []

    if n <= 0:
        return []

    for i in range(n):
        if len(res) in [0, 1]:
            res.append([1] * (len(res) + 1))
            continue
        temp = [1, 1]
        for i in range(len(res[-1]) - 1):
            temp.insert(i+1, res[-1][i] + res[-1][i+1])
        res.append(temp)
    return res
