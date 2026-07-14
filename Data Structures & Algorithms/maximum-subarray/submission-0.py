class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float("inf")
        cur_sum = 0
        for num in nums:
            if cur_sum + num < 0:
                max_sum = max(cur_sum, max_sum)
                # print("it's joever, sorry :(", max_sum)
                cur_sum = 0
            else:
                cur_sum += num
                # print("nice!", cur_sum)
                max_sum = max(cur_sum, max_sum)
        if max(nums) < 0:
            return max(nums)
        return max_sum