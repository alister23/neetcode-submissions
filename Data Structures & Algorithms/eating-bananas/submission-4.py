class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def getN(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            # print(f"{k=} {hours=}")
            return h >= hours

        min_k = r
        while l <= r:
            mid = (l+r)//2
            if getN(mid):
                min_k = min(min_k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return min_k