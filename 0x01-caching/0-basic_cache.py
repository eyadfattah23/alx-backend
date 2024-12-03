#!/usr/bin/python3
"""Define a class BasicCache that inherits from BaseCaching (caching system)"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        if key:
            return self.cache_data.get(key)
