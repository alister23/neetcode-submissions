class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in num_set:
                count = 1
                i = num
                while i+1 in num_set:
                    count += 1
                    i += 1
                max_len = max(max_len, count)
        return max_len