#!/usr/bin/env python3
"""FIFO Caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This is an implementation of FIFO caching
    """
    def __init__(self):
        """Method that runs on instatiation
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = next(iter(self.cache_data))
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

    def get(self, key) -> str:
        """Get an item in the cache
        """
        return self.cache_data.get(key)
