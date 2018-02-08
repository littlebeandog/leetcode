# slow version
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.key_list = []
        self.cache = dict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            self.key_list.remove(key)
            self.key_list.append(key)
            return self.cache[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key] = value
            self.key_list.remove(key)
            self.key_list.append(key)
        elif self.size < self.capacity:
            self.cache[key] = value
            self.key_list.append(key)
            self.size += 1
        else:
            self.cache.pop(self.key_list[0])
            self.cache[key] = value
            self.key_list.remove(self.key_list[0])
            self.key_list.append(key)
        

# order dict slow version
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            v = self.cache.pop(key)
            self.cache[key] = v
            return v
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif self.size < self.capacity:
            self.cache[key] = value
            self.size += 1
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value


