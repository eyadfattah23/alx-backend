#!/usr/bin/python3
"""Define a class LRUCache that inherits from BaseCaching(caching system)"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """least recently used Based caching system
    """

    def __init__(self):
        """INITIALIZE"""
        super().__init__()
        self.recencyDict = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.recencyDict[key] = 4
            keys = list(self.cache_data.keys())
            if len(keys) >= BaseCaching.MAX_ITEMS and key not in keys:
                min_recency = float('inf')
                lru_item = None
                for _item, recency in self.recencyDict.items():
                    if recency < min_recency:
                        min_recency = recency
                        lru_item = _item
                del self.cache_data[lru_item]
                del self.recencyDict[lru_item]
                print("DISCARD:", lru_item)

            self.cache_data[key] = item
            for recency_key in self.recencyDict.keys():
                if recency_key == key:
                    continue
                self.recencyDict[recency_key] -= 1

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        if key:
            if key in self.recencyDict:
                self.recencyDict[key] = 4
            return self.cache_data.get(key)
