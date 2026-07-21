class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        
        tall = 0
        for i in range(len(height)):
            left[i] = tall
            tall = max(tall, height[i])
        
        tall = 0
        for j in range(len(height)-1, -1, -1):
            right[j] = tall
            tall = max(tall, height[j])

        water = 0
        
        for i in range(len(height)):
            water += max(0, min(left[i], right[i])-height[i])

        return water

        

