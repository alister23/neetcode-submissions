import math
class Solution:
    def canEat(piles, h, rate):
        if rate < 1:
            return False
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/rate)
        if hours <= h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        mid = (left+right)//2
        while left <= right:
            mid_eat = Solution.canEat(piles, h, mid)
            next_eat = Solution.canEat(piles, h, mid-1)
            if mid_eat and not next_eat:
                return mid
            elif mid_eat and next_eat:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
        
