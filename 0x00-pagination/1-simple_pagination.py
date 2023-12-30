#!/usr/bin/env python3
"""This script contains simple pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This function takes two pagination parameters
    as argument and returns a tuple containing the
    start and end index for the pagination of a certain
    list
    """
    end: int = page * page_size
    start: int = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This method retuns a page based on the
        page size and page passed as argument
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        idx: Tuple[int, int] = index_range(page, page_size)
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset: List[List] = [row for row in reader]
            dataset = dataset[1:]
        return dataset[idx[0]: idx[1]]
