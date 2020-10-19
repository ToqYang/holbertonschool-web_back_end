#!/usr/bin/env python3
from typing import List
"""
    List of floats annotations
"""


def sum_list(input_list: List[float]) -> float:
    """
        Args:
            input_list: float numbers

        Return:
            Sum of the float numbers
    """

    result: float = 0

    for x in input_list:
        result += x

    return result
