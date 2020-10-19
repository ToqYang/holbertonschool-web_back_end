#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Union
"""
    Duck type and iteration
"""


def element_length(lst: Iterable[]) -> List[Tuple[Union[Sequence, int]]]:
    """
        Args:
            lst: Sequence of list

        Return:
            List of tuple of sequence of integers
    """

    return [(i, len(i)) for i in lst]
