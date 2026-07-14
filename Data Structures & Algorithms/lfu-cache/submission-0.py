class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.counter = {}
        self.recent = {}
        self.i = 0
        

    def get(self, key: int) -> int:
        if (key in self.cache):
            self.counter[key] += 1
            self.recent[key] = self.i
            self.i += 1
            return self.cache[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= len(self.cache):
            least = 300000
            least_key = None
            for k in self.cache:
                if self.counter[k] < least:
                    least_key = k
                    least = self.counter[k]
                elif self.counter[k] == least:
                    if self.recent[k] < self.recent[least_key]:
                        least_key = k
                        least = self.counter[k]
            del self.cache[least_key]
        self.cache[key] = value
        self.counter[key] = self.counter.setdefault(key, 1) + 1
        self.recent[key] = self.i
        self.i += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)