#!/usr/bin/env python3
"""This script contains a function that calculates
the range of indexes to return in a list for the
given pagination parameters
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This function takes two pagination parameters
    as argument and returns a tuple containing the
    start and end index for the pagination of a certain
    list
    """
    end: int = page * page_size
    start: int = end - page_size
    return (start, end)
