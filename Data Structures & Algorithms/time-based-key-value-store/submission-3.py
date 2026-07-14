class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))
        # print("set",key,"to",value,"at", timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        # print("searching",key,"for value at",timestamp)
        values = self.time_map[key]
        # print(values)
        left = 0
        right = len(values)-1
        mid = (left+right)//2
        while left <= right:
            # print(f"{left=} {mid=} {right=}")
            if values[mid][0] <= timestamp and (mid == len(values)-1 or values[mid+1][0] > timestamp):
                # print("found at",mid)
                return values[mid][1]
            if values[mid][0] < timestamp:
                left = mid+1
            else:
                right = mid-1
            mid = (left+right)//2
        return ""
        
