#!/usr/bin/python3
"""Define a class FIFOCache that inherits from BaseCaching(caching system)"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Based caching system
    """

    def __init__(self):
        """INITIALIZE"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item
            keys = list(self.cache_data.keys())
            if len(keys) > BaseCaching.MAX_ITEMS:
                del self.cache_data[keys[0]]
                print("DISCARD:", keys[0])

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        if key:
            return self.cache_data.get(key)
