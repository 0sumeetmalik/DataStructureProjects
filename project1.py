"""
Created a dictionary in init method in LRU Cache where we can store keys and Values
oldest_key = To keep track of which cache we used latest, it is list

# In Get method
we checked if key exist if yes, we removed the key from anywhere in
oldest_key list and moved it to number 1 position,

# In set method
First handled None inputs
Then added to cache if length of item has not not exceeded capacity

# if capacity is exceed, then we removed the oldest_item using POP
and added new cache item and then if statement added the key

Time Complexity O(1)
"""


class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.item = dict()
        self.oldest_key = []

    def get(self, key):
        if key in self.item:
            # Remove key from and append back at start
            self.oldest_key.remove(key)
            # Adding Key at Start, like shifting from somewhere to start
            self.oldest_key.insert(0, key)
            return self.item[key]
        else:
            return -1

    def set(self, key, value):
        # Handling None Values input or Empty
        if key is None or key == '':
            return -1

        if len(self.item) == self.capacity:
            # Now we need to remove from cache to add more
            key_remove = self.oldest_key.pop()
            self.item.pop(key_remove)

        if len(self.item) < self.capacity:
            if key not in self.item:
                self.item[key] = value
                self.oldest_key.insert(0, key)


if __name__ == '__main__':
    ## Out Test cases and its result

    our_cache = LRU_Cache(5)
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print('Get key is 1, value returned', our_cache.get(1))  # returns 1
    print('Get key is 2, value returned', our_cache.get(2))  # returns 2
    print('Get key is 9, value returned', our_cache.get(9))  # returns -1

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print('Get key is 3 and It has been autoremoved', our_cache.get(3))

    # More test cases
    # Test Case 1
    our_cache.set(None, None)
    print('Get key is None, value returned', our_cache.get(None))  # returns -1

    # Test Case 3
    our_cache.set(999, 1200)
    print(our_cache.item)
