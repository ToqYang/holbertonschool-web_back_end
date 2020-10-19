#!/usr/bin/env python3
from typing import Union, List
"""
    Mixed lists
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: float-int numbers

        Return:
            Float base in int or float numbers
    """

    result: float = 0

    for x in mxd_lst:
        result += x

    return result
