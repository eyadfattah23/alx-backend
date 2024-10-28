#!/usr/bin/env python3
"""
Define index_range that takes two integer arguments page and page_size.

return a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index

    Args:
        page (int): 1-indexed, i.e. the first page is page 1.
        page_size (int)

    Returns:
        tuple
    """
    return (page_size*(page-1), page * page_size)
