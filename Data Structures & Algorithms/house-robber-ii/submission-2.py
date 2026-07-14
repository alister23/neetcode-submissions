class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[-1]*len(nums) for _ in range(len(nums))]
        def recur(i,j):
            if i >= len(nums) or j >= len(nums):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if i > j:
                dp[i][j] = 0
                return 0
            if j-i == 0:
                dp[i][j] = nums[i]
                return nums[i]
            if j-i == 1:
                answer = max(nums[i], nums[i+1])
                dp[i][j] = answer
                return answer
            answer = max(recur(i+2,j)+nums[i], recur(i+1,j))
            dp[i][j] = answer
            return answer
        return max(nums[0]+recur(2,len(nums)-2), recur(1,len(nums)-1))
            