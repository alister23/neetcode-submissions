class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def delete(self):
        if self.next and self.prev:
            self.prev.next = self.next
            self.next.prev = self.prev
        elif self.next:
            self.next.prev = None
        elif self.prev:
            self.prev.next = None
        print("deleted previous instance of", self.val)
        self = None

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        # number of keys in cache
        self.count = 0
        # maps keys to values
        self.values = {}
        # maps keys to most recent nodes in cache
        self.nodes = {}
        # represents cache as linked list
        self.cache_head = Node()
        self.cache_cur = self.cache_head

    def get(self, key: int) -> int:
        print("accessing", key)
        # if key exists
        if key in self.values:
            # set latest node in recency cache to key
            self.cache_cur.val = key
            self.cache_cur.next = Node()
            self.cache_cur.next.prev = self.cache_cur
            self.cache_cur = self.cache_cur.next 
            print("deleting", key)
            # delete the previous node corresponding to the key
            if self.nodes[key] == self.cache_head:
                if not self.cache_head.next:
                    self.cache_head.next = Node()
                self.cache_head = self.cache_head.next
                self.cache_head.prev = None
            self.nodes[key].delete()
            # update using the new node
            self.nodes[key] = self.cache_cur.prev
            print(self.values[key])
            return self.values[key]
        print("key not found")
        return -1


    def put(self, key: int, value: int) -> None:
        print("adding new key value pair", key, value)
        if key not in self.values:
            self.count += 1
            if self.count > self.capacity:
                print("over capacity")
                print("deleting", self.cache_head.val)
                # no longer value associated with that key
                del self.values[self.cache_head.val]
                # delete the head node
                self.nodes[self.cache_head.val].delete()
                del self.nodes[self.cache_head.val]
                self.cache_head = self.cache_head.next
                self.count -= 1
        self.cache_cur.val = key
        self.cache_cur.next = Node()
        self.cache_cur.next.prev = self.cache_cur
        self.cache_cur = self.cache_cur.next
        if key in self.values:
            print("adding", key,", deleting old instance")
            if self.nodes[key] == self.cache_head:
                if not self.cache_head.next:
                    self.cache_head.next = Node()
                self.cache_head = self.cache_head.next
                self.cache_head.prev = None
            self.nodes[key].delete()
        self.nodes[key] = self.cache_cur.prev
        self.values[key] = value
            

        
