class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent = {}
        self.cache = {}
        self.time = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.time += 1
            self.recent[key] = self.time
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.time += 1
        self.cache[key] = value
        self.recent[key] = self.time
        if len(self.cache.keys()) > self.capacity:
            old_key, val = min(self.recent.items(), key=lambda x: x[1])
            print(self.recent.items())
            del self.cache[old_key]
            self.recent[old_key] = float("inf")


