#!/usr/bin/env python3
"""
Extends basic pagination by providing hypermedia-style metadata
for paginated results from a dataset of popular baby names.
"""
import csv
import math
from typing import List, Tuple, Dict, Any


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


class Server:
    """
    Server class to paginate a database of popular baby names.

    Provides methods to get a page of data and additional pagination metadata.

    Attributes:
        DATA_FILE (str): Path to the CSV data file.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server and prepare the dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset if not already loaded.

        Returns:
            List[List]: The dataset, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset based on pagination parameters.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination metadata and current page data.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - page_size (int): Number of items on the page
                - page (int): Current page number
                - data (List[List]): Page data
                - next_page (Optional[int]): Next page number or None
                - prev_page (Optional[int]): Previous page number or None
                - total_pages (int): Total number of pages
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
             'page_size': len(data),
             'page': page,
             'data': data,
             'next_page': page + 1 if page < total_pages else None,
             'prev_page': page - 1 if page > 1 else None,
             'total_pages': total_pages
             }
