#!/usr/bin/env python3
"""
Basic Caching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This is a basic caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
    
    def get(self, key) -> str:
        """Get an item in the cache
        """
        return self.cache_data.get(key)

        