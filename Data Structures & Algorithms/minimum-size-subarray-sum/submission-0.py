class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        min_len = len(nums)+1
        left = 0
        right = 0

        while right < len(nums):
            total += nums[right]
            if total >= target:
                while nums[left] + target <= total:
                    total -= nums[left]
                    left += 1
                min_len = min(min_len, right-left+1)

            right += 1

        if min_len > len(nums): return 0
        return min_len