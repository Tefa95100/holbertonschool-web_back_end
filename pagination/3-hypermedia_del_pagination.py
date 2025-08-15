#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a page from the dataset starting from the provided index,
        with deletion resilience.

        Args:
            index (int): The start index for the page. Must be in range.
            page_size (int): The number of items to return.

        Returns:
            dict: A dictionary with:
                - index (int): the original index
                - next_index (int): the next index to query
                - page_size (int): the page size used
                - data (list): the actual data page

        Raises:
            AssertionError: if index is out of range or not an integer
        """
        assert isinstance(index, int) and index >= 0
        indexed_dataset = self.indexed_dataset()
        assert index < len(self.dataset())

        data = []
        current_index = index
        collected = 0

        while collected < page_size and current_index < len(self.dataset()):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
                collected += 1
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
