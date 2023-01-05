#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List


value = List[str, float]


def sum_mixed_list(mxd_lst: value) -> float:
    """
    function that returns their sum as a float.
    """
    j: float = 0.0
    for i in mxd_lst:
        j += i
    return j
