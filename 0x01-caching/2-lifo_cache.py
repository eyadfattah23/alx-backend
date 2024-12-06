#!/usr/bin/python3
"""Define a class LIFOCache that inherits from BaseCaching(caching system)"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFO Based caching system
    """

    def __init__(self):
        """INITIALIZE"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            keys = list(self.cache_data.keys())
            if len(keys) >= BaseCaching.MAX_ITEMS and key not in keys:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)
                self.cache_data[key] = item

            else:
                self.cache_data[key] = item

            self.last_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        if key:
            self.last_key = key
            return self.cache_data.get(key)
