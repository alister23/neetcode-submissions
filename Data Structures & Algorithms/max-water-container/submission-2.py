class Solution:
    def maxArea(self, heights: List[int]) -> int:
        global_max = 0
        left = 0
        right = len(heights)-1
        while left < right:
            # print(left, right)
            global_max = max((right-left)*min(heights[left],heights[right]), global_max)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return global_max