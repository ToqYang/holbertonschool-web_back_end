#!/usr/bin/env python3
from typing import Callable
"""
    make_multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Args:
            multiplier: factor

        Return:
            multiplication in float
    """

    def x(f: float) -> float:
        """ Get the second argument somthing like JS """
        return float(f * multiplier)

    return x
