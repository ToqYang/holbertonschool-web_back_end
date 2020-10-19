#!/usr/bin/env python3
from typing import Callable
"""
    make_multiplier
"""


def make_multiplier(multiplier: Callable[[float, float] float]) -> float:
    """
        Args:
            multiplier: factor

        Return:
            multiplication in float
    """

    return multiplier * multiplier
