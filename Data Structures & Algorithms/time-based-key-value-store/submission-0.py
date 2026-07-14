class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        array = self.store[key]
        left = 0
        right = len(array)-1
        mid = (left+right)//2
        while left <= right:
            if array[mid][1] == timestamp:
                return array[mid][0]
            elif array[mid][1] < timestamp:
                if mid == len(array)-1 or array[mid+1][1] > timestamp:
                    return array[mid][0]
                else:
                    left = mid+1
            else:
                right = mid-1
            mid = (left+right)//2
        return ""