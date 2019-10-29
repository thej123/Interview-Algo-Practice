from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tracker = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.tracker.remove(key)
            self.tracker.append(key)
            
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                res = deque(self.tracker) 
                popped = res.popleft()
                self.tracker = list(res)
                del self.cache[popped]
        else:
            self.tracker.remove(key)
        self.cache[key] = value
        self.tracker.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
