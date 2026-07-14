class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        for num in nums:
            counts[num] += 1
        j = 0
        for i in range(3):
            for k in range(counts[i]):
                nums[j] = i
                j += 1
        
