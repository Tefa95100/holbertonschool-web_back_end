#!/usr/bin/env python3
"""
Provides a Server class to paginate data from a CSV file containing
popular baby names, as well as a helper function for pagination index calculation.
"""
import csv
from typing import List, Tuple

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

    Attributes:
        DATA_FILE (str): Path to the CSV data file.
        __dataset (List[List]): Cached dataset loaded from the CSV file.
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
