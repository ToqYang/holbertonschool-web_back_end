#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Union, Tuple
"""
    Duck type and iteration
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Union[Sequence, int]]]:
    """
        Args:
            lst: Sequence of list

        Return:
            List of tuple of sequence of integers
    """

    return [(i, len(i)) for i in lst]
