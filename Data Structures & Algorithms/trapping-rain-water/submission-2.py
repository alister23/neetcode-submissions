class Solution:
    def trap(self, height: List[int]) -> int:
        tallest_left = [0]*len(height)
        tallest_right = [0]*len(height)
        max_left = height[0]
        max_right = height[-1]
        for i in range(1,len(height)):
            tallest_left[i] = max_left
            max_left = max(height[i], max_left)
        for i in range(len(height)-2,-1,-1):
            tallest_right[i] = max_right
            max_right = max(height[i], max_right)
        water = 0
        for i in range(len(height)):
            # print(f"{i=}")
            # print(f"{tallest_left[i]=}")
            # print(f"{tallest_right[i]=}")
            # print(f"{height[i]=}")
            # print("water here:", min(tallest_left[i],tallest_right[i])-height[i])
            water += max(0,min(tallest_left[i],tallest_right[i])-height[i])
        return water