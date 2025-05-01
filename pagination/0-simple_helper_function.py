#!/usr/bin/env python3
"""
Provides a utility function to calculate start and end indexes
for pagination based on a page number and page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given pagination page.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and the end index (exclusive) to slice a dataset.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
