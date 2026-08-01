class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append((value, timestamp))
        #print(f"set {key} to {value} at time {timestamp}")
        #print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        #print(f"retrieving {key} at {timestamp}")
        if key not in self.timemap:
            #print("not there")
            return ""
        vals = self.timemap[key]
        l = 0
        r = len(vals)-1
        max_time = -1
        max_time_val = ""
        while l <= r:
            m = (l+r)//2
            val, timestamp_prev = vals[m]
            if timestamp_prev <= timestamp:
                if timestamp_prev > max_time:
                    max_time = timestamp_prev
                    max_time_val = val
                l = m+1
            else:
                r = m-1
        #print(f"got at {max_time}: {max_time_val}")
        return max_time_val
