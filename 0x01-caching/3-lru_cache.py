#!/usr/bin/env python3
"""LRU Caching
"""

from base_caching import BaseCaching
from datetime import datetime
from typing import Union


class LRUCache(BaseCaching):
    """This is an implementation of LRU caching
    """
    def __init__(self):
        """Method that runs on instatiation
        """
        super().__init__()
        self.cache_data_time = {}

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            # check for the key with the min time
            discard_key = min(self.cache_data_time,
                              key=self.cache_data_time.get)

            # delete from the cache data and cache_data_time
            del self.cache_data_time[discard_key]
            del self.cache_data[discard_key]
            print(f"DISCARD: {discard_key}")

        # update the cache data and the cache_data_time with the current time
        self.cache_data.update({key: item})
        self.cache_data_time.update({key: datetime.today()})

    def get(self, key):
        """Get an item in the cache
        """
        if self.cache_data.get(key) is None:
            return
        # update the cache_data_time of key with current time
        self.cache_data_time.update({key: datetime.today()})

        # return the key
        return self.cache_data.get(key)
