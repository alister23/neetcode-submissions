class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def checkDays(w):
            d = 0
            i = 0
            total = 0
            while i < len(weights):
                # print("checking", weights[i])
                if total+weights[i] <= w:
                    # print("adding to current load")
                    total += weights[i]
                    # print(f"{total=}")
                else:
                    # print("too much, calling it a day")
                    d += 1
                    total = weights[i]
                i+= 1
            if total != 0: d += 1
            print(f"{w=} {d=}")
            return d <= days

        least = r
        while l <= r:
            m = (l+l+(r-l))//2
            if checkDays(m):
                least = min(least, m)
                r = m-1
            else:
                l = m+1

        return least