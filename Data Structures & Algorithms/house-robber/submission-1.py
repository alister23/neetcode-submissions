class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        def recur(index):
            if dp[index] != -1:
                return dp[index]
            if index >= len(nums):
                dp[index] = 0
                return 0
            if index == len(nums)-1:
                dp[index] = nums[index]
                return nums[index]
            if index == len(nums)-2:
                answer = max(nums[index],nums[index+1])
                dp[index] = answer
                return answer
            answer = max(nums[index]+recur(index+2), recur(index+1))
            dp[index] = answer
            return max(nums[index]+recur(index+2), recur(index+1))
        return recur(0)