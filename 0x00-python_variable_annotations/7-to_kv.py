#!/usr/bin/env python3
from typing import Union, Tuple
"""
    Mixed Tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """
        Args:
            k: String
            v: Union: Can be int or float

        Return:
            Tuple with string and int or float
    """

    cncat: Tuple(str, Union[int, float])
    cncat = (k, v**2)

    return cncat
