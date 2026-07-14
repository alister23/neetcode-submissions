class Solution:
    def canEat(piles, h, speed):
        return h >= sum(math.ceil(pile/speed) for pile in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = math.ceil(sum(piles)/h)
        max_speed = max(piles)
        mid = (min_speed+max_speed)//2
        while min_speed <= max_speed:
            print(min_speed, mid, max_speed)
            if Solution.canEat(piles, h, mid):
                if mid == 1:
                    return mid
                if not Solution.canEat(piles, h, mid-1):
                    return mid
                else:
                    max_speed = mid-1
            else:
                min_speed = mid+1
            mid = (min_speed+max_speed)//2
        return max(piles)