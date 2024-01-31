#!/usr/bin/env python3
"""
BasicCache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from the BaseCaching module"""
    def __init__(self):
        """Initializes the class BasicCache"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """adds item to the caching system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns:
            item associated with the key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
