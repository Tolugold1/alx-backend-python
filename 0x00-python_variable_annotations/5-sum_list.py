#!/usr/bin/env python3
"""
function sum_list which takes a list input_list
of floats as argument and returns their sum as a float
"""
from typing import List


value = list[float]


def sum_list(input_list: value) -> float:
    """return sum of list of floats"""
    j = 0.0
    for i in input_list:
        j += i
    return j
