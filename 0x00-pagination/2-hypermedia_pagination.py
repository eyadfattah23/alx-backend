#!/usr/bin/env python3
"""
Define index_range that takes two integer arguments page and page_size.

return a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
"""


import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index

    Args:
        page (int): 1-indexed, i.e. the first page is page 1.
        page_size (int)

    Returns:
        tuple
    """
    return (page_size*(page-1), page * page_size)


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
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        rng = index_range(page, page_size)
        return self.dataset()[rng[0]:rng[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            a dictionary containing the following key-value pairs:

            * page_size: the length of the returned dataset page
            * page: the current page number
            * data: the dataset page (equivalent to return from previous task)
            * next_page: number of the next page, None if no next page
            * prev_page: number of the previous page, None if no previous page
            * total_pages: total number of pages in the dataset as an integer

        """

        try:
            next_page = self.get_page(page + 1, page_size)
            next_page_idx = page + 1 if next_page != [] else None
        except AssertionError:
            next_page_idx = None

        try:
            prev_page = self.get_page(page - 1, page_size)
            prev_page_idx = page - 1
        except AssertionError:
            prev_page_idx = None

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page_idx,
            "prev_page": prev_page_idx,
            "total_pages": math.ceil(len(self.dataset()) / page_size),
        }
