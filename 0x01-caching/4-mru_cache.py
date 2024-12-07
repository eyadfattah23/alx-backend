#!/usr/bin/python3
"""Define a class MRUCache that inherits from BaseCaching(caching system)"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """most recently used Based caching system
    """

    def __init__(self):
        """INITIALIZE"""
        super().__init__()
        self.recencyDict = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.recencyDict[key] = BaseCaching.MAX_ITEMS
            keys = list(self.cache_data.keys())
            if len(keys) >= BaseCaching.MAX_ITEMS and key not in keys:
                max_recency = float('-inf')
                mru_item = None
                for _item, recency in self.recencyDict.items():
                    if recency > max_recency:
                        max_recency = recency
                        mru_item = _item
                del self.cache_data[mru_item]
                del self.recencyDict[mru_item]
                print("DISCARD:", mru_item)

            self.cache_data[key] = item
            for recency_key in self.recencyDict.keys():
                if recency_key == key:
                    continue
                self.recencyDict[recency_key] -= 1

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        if key:
            if key in self.recencyDict:
                self.recencyDict[key] = BaseCaching.MAX_ITEMS
                for recency_key in self.recencyDict.keys():
                    if recency_key == key:
                        continue
                    self.recencyDict[recency_key] -= 1
            return self.cache_data.get(key)
