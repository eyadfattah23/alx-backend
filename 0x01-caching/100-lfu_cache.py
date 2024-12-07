#!/usr/bin/python3
"""Define a class LFUCache that inherits from BaseCaching(caching system)"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """least frequently used Based caching system
    """

    def __init__(self):
        """INITIALIZE"""
        super().__init__()
        self.frequencyDict = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            keys = list(self.cache_data.keys())
            if key in keys:
                self.frequencyDict[key] += 1
            else:
                if len(keys) >= BaseCaching.MAX_ITEMS:
                    min_freq = float('inf')
                    lfu_item = None
                    for _item, freq in self.frequencyDict.items():
                        if freq < min_freq:
                            min_freq = freq
                            lfu_item = _item
                    del self.cache_data[lfu_item]
                    del self.frequencyDict[lfu_item]
                    print("DISCARD:", lfu_item)

                self.frequencyDict[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""

        if key:
            if key in self.frequencyDict:
                self.frequencyDict[key] += 1
            return self.cache_data.get(key)
