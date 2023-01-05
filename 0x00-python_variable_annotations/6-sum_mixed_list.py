#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


value = List[Union[str, float]]


def sum_mixed_list(mxd_lst: value) -> float:
    """
    function that returns their sum as a float.
    """
    return sum(mxd_lst)
