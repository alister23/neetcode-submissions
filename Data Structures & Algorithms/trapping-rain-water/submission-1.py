class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        left_total = 0
        right_total = 0
        left_water = 0
        right_water = 0
        for bar in height:
            if bar > left_max:
                left_total += left_water
                left_water = 0
                left_max = bar
            else:
                left_water += left_max - bar
        # print(left_total)
        for bar in height[::-1]:
            if bar >= right_max:
                right_total += right_water
                right_water = 0
                right_max = bar
            else:
                right_water += right_max - bar
        # print(right_total)
        return left_total + right_total