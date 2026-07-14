class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [1]*len(nums)
        from_right = [1]*len(nums)
        for i in range(len(nums)-1):
            from_left[i+1] = nums[i]*from_left[i]
            from_right[len(nums)-i-2] = nums[len(nums)-i-1]*from_right[len(nums)-i-1]
        output = [0]*len(nums)
        # print(from_left)
        # print(from_right)
        for i in range(len(nums)):
            output[i] = from_left[i] * from_right[i]
        return output