#!/usr/bin/env python3
"""Lifo Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class LRUCache that inherits from BaseCaching"""
    def __init__(self):
        """class constructor"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """adds item into a cache"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_2nd_last = len(self.cache_data_list) - 2
                key_last = self.cache_data_list.pop(key_2nd_last)
                del self.cache_data[key_last]
                print("DISCARD: {}".format(key_last))

    def get(self, key):
        """Retrieves an item from cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
